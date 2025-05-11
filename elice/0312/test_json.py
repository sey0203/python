import json

data = [
    {"id": 1, "name": "김철수", "email": "kim@example.com"},
    {"id": 2, "name": "아이유", "email": "iu@example.com"}
]

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data[0]["name"])

json_str = json.dumps(data, ensure_ascii=False)
print(json_str)

parsed = json.loads(json_str)
print(parsed[1]["email"])

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

filtered = [d for d in data if d["name"].startswith("아")]
print(filtered)