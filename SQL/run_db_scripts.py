import psycopg2
import os
import sys
import traceback # 스택 트레이스를 위해 추가

# --- 데이터베이스 연결 설정 ---

# 환경 변수가 설정되지 않았을 경우를 대비한 기본값 (필요시 수정하거나 env 설정을 확인하세요)
# 운영 환경에서는 환경 변수 설정이 필수입니다.
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# 환경 변수 누락 체크 (필수 정보 확인)
if not all([DB_NAME, DB_USER, DB_PASSWORD]):
    print("오류: 데이터베이스 연결에 필요한 환경 변수(DB_NAME, DB_USER, DB_PASSWORD)가 설정되지 않았습니다.", file=sys.stderr)
    sys.exit(1) # 필수 정보 누락 시 즉시 종료

# --- SQL 파일 실행 함수 ---
def execute_sql_script(script_file_path):
    """
    지정된 경로의 SQL 스크립트 파일을 읽어와 데이터베이스에 실행합니다.
    오류 발생 시 해당 오류를 다시 발생(re-raise)시켜 호출자에게 알립니다.
    """
    conn = None
    cur = None
    script_name = os.path.basename(script_file_path)
    print(f"\n--- 스크립트 실행 시작: {script_name} ---")

    try:
        # 데이터베이스 연결
        print(f"데이터베이스 연결 시도: {DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cur = conn.cursor()
        print("데이터베이스 연결 성공.")

        # SQL 파일 내용 읽기
        print(f"SQL 스크립트 파일 '{script_name}' 읽는 중...")
        # 파일 인코딩이 UTF-8인지 확인하고 읽습니다.
        try:
            with open(script_file_path, 'r', encoding='utf-8') as f:
                sql_script = f.read()
            print("스크립트 파일 읽기 완료.")
        except FileNotFoundError:
            print(f"오류: 스크립트 파일 '{script_file_path}'을 찾을 수 없습니다.", file=sys.stderr)
            # 파일을 찾을 수 없는 경우 DB 연결은 필요 없으므로 바로 raise
            raise # 파일 찾기 오류는 여기서 다시 발생

        # SQL 스크립트 실행
        print("SQL 스크립트 실행 중...")
        # 참고: psycopg2의 execute는 기본적으로 여러 SQL 명령을 세미콜론으로 구분하여 실행할 수 있으나,
        # 복잡한 스크립트(예: $$ 블록, 주석 내 세미콜론 등)의 경우 파싱 문제가 발생할 수 있습니다.
        # 대부분의 DDL/DML 스크립트는 잘 작동합니다.
        cur.execute(sql_script)
        print("SQL 스크립트 실행 완료.")

        # 변경사항 커밋
        conn.commit()
        print("트랜잭션 커밋 완료.")
        print(f"--- 스크립트 실행 성공: {script_name} ---")
        return True # 성공 시 True 반환

    except (Exception, psycopg2.Error) as error:
        # 데이터베이스 연결 및 실행 중 발생한 오류 처리
        print(f"\n오류: 스크립트 '{script_name}' 실행 중 데이터베이스 작업 오류 발생:", file=sys.stderr)
        print(f"오류 상세: {error}", file=sys.stderr)
        # 선택 사항: 자세한 디버깅을 위해 스택 트레이스 출력
        # traceback.print_exc(file=sys.stderr)
        if conn:
            conn.rollback() # 오류 발생 시 변경사항 롤백
            print("트랜잭션 롤백 완료.", file=sys.stderr)
        # 오류 발생 시 예외를 다시 발생시켜 호출자(main 블록)에게 알립니다.
        raise # 중요: 오류를 다시 발생시킴

    finally:
        # 연결 종료
        if cur:
            cur.close()
            
        if conn:
            conn.close()
            print("데이터베이스 연결 종료.")

# --- 메인 실행 로직 ---
if __name__ == "__main__":
    print("데이터베이스 데이터 준비 스크립트 실행 자동화 시작.")

    # --- 설정 ---
    # SQL 스크립트 파일들이 위치한 디렉토리 경로를 설정합니다.
    # 기본값: 이 Python 스크립트와 같은 디렉토리
    # 다른 디렉토리를 사용하려면 아래 변수를 수정하거나 환경 변수 등으로 설정하세요.
    # 예: SQL_FILES_DIR = "/path/to/your/sql/scripts"
    # 예: SQL_FILES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sql") # 스크립트 하위 sql 폴더
    SQL_FILES_DIR = os.path.dirname(os.path.abspath(__file__))

    # '데이터 삽입' 단계에서 실행할 SQL 파일들의 목록
    sql_files_to_run = []

    default_cleanup = ['cleanup_all_likes.sql', 'cleanup_all_comments.sql']
    args = sys.argv[1:]
    skip_cleanup = '--no-cleanup' in args

    if skip_cleanup:
        sql_files_to_run = []
    else:
        sql_files_to_run = default_cleanup

    if '--seed-likes' in args:
        sql_files_to_run.append('setup_all_likes.sql')

    # 댓글 시드 플래그 처리
    if '--seed-comments' in args:
        sql_files_to_run.append('setup_all_comments.sql')

    # --- 설정 끝 ---

    all_scripts_succeeded = True # 모든 스크립트가 성공했는지 추적

    for sql_file in sql_files_to_run:
        script_path = os.path.join(SQL_FILES_DIR, sql_file)

        # 파일 존재 여부 확인 (execute_sql_script에서도 하지만, 여기서 미리 체크하면 더 빠르게 알 수 있음)
        if not os.path.exists(script_path):
            print(f"\n오류: 스크립트 파일 '{sql_file}'을 찾을 수 없습니다.", file=sys.stderr)
            print(f"예상 경로: {script_path}", file=sys.stderr)
            all_scripts_succeeded = False # 실패 상태로 표시
            break # 파일을 찾을 수 없으면 더 이상 진행하지 않고 중단

        try:
            execute_sql_script(script_path)
            # execute_sql_script 함수에서 오류 발생 시 예외를 다시 발생시키므로,
            # 이 부분이 실행된다는 것은 해당 스크립트가 성공했음을 의미합니다.
        except Exception:
            # execute_sql_script 함수 내에서 이미 오류 메시지를 출력했으므로
            # 여기서는 추가 메시지를 출력하고 반복을 중단합니다.
            print(f"\n--- 스크립트 실행 실패: {sql_file}. 후속 스크립트 실행을 중단합니다. ---", file=sys.stderr)
            all_scripts_succeeded = False # 실패 상태로 표시
            break # 오류 발생 시 중단

    if all_scripts_succeeded:
        print("\n데이터베이스 데이터 준비 스크립트 실행 자동화 성공적으로 종료.")
        sys.exit(0) # 성공 시 0 반환
    else:
        print("\n데이터베이스 데이터 준비 스크립트 실행 자동화 오류 발생 후 종료.")
        sys.exit(1) # 실패 시 1 반환