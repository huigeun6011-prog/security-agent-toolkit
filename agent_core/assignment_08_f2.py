import json
logs = [{"user": "kim01", "count": 4}, {"user": "lee02", "count": 1}]

with open("assignment_08_f2.json", "w", encoding = "utf-8") as f:
    json.dump(logs[0]["user"], f)

with open("assignment_08_f2.json", "r", encoding = "utf-8") as f:
    print(json.load(f))