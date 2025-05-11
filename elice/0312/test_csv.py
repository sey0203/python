import csv

data = [
    {"id": 1, "name": "김철수", "email": "kim@example.com"},
    {"id": 2, "name": "아이유", "email": "iu@example.com"}
]

# with open("data.csv", "w", encoding="utf-8", newline="") as f:
#     writer = csv.DictWriter(f, fieldnames=["id", "name", "email"])
#     writer.writeheader()
#     writer.writerows(data)

# with open("data.csv", "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row["id"], row["name"], row["email"])
    #return list(reader)

# with open("data.csv", "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#     filtered = [d for d in reader  if d["name"].startswith("김")]
# print(filtered)

def filter_users_by_name(users, keyword="김"):
    return [user for user in users if keyword in user["name"]]

filter_csv_users = filter_users_by_name(data, "아")
print(filter_csv_users)