import json

with open('gichan_input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    total = 0
    count = 0
    for item in data:
        total += 1
        if item["result"] == "FAIL":
            count += 1
    print(f'전체 {total}건, 실패 {count}건')