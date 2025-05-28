from pathlib import Path
import subprocess
import pytest

# run_db_scripts.py가 conftest.py와 같은 디렉토리에 있으므로,
# 스크립트 파일의 디렉토리 자체가 run_db_scripts.py가 있는 디렉토리입니다.
RUN_SCRIPT_DIR = Path(__file__).resolve().parent

@pytest.fixture(autouse=True)
def prepare_db(request):
    # RUN_SCRIPT_DIR 아래의 run_db_scripts.py 파일 경로
    run_script_path = RUN_SCRIPT_DIR / "run_db_scripts.py"
    cmd = ["python", str(run_script_path)]

    if "no_cleanup" in request.keywords:
        cmd.append("--no-cleanup")

    if "seed_likes" in request.keywords:
        cmd.append("--seed-likes")

    # seed_comments 마커
    if "seed_comments" in request.keywords:
        cmd.append("--seed-comments")

    subprocess.run(cmd, check=True)