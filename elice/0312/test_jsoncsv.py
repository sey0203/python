import json
import csv

# 문제1
# JSON 데이터 읽기
def load_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

# 문제2
# CSV 데이터 읽기
def load_csv(filename):
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

# 필터링 함수: 이름에 '김' 포함된 사용자만 출력
def filter_users_by_name(users, keyword="김"):
    return [user for user in users if keyword in user['name']]

# 데이터 출력 함수
def print_users(users):
    for user in users:
        print(f"{user['id']} - {user['name']} ({user['email']})")

# 메인 실행부
if __name__ == "__main__":
    print("📂 JSON 데이터 로딩")
    json_users = load_json("users.json")
    print_users(json_users)

    print("\n📂 CSV 데이터 로딩")
    csv_users = load_csv("users.csv")
    print_users(csv_users)

    print("\n🔎 이름에 '김'이 포함된 사용자 (JSON 기준)")
    filtered_json_users = filter_users_by_name(json_users, "김")
    print_users(filtered_json_users)

    print("\n🔎 이름에 '김'이 포함된 사용자 (CSV 기준)")
    filtered_csv_users = filter_users_by_name(csv_users, "김")
    print_users(filtered_csv_users)