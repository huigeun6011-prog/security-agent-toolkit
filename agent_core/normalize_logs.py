# 서버 로그(raw_logs.txt)를 같은 칸 이름의 딕셔너리로 바꿔 저장한다.
import re
import json

# 시각 · 등급 · 계정 · IP 네 곳에 이름을 붙인 패턴 (한 번만 적는다)
PATTERN = r"(?P<time>[\d:]+) (?P<level>\w+) \w+ login for (?P<user>[\w.]+) from (?P<ip>[\d.]+)"


def parse_raw_logs(line):
    # 줄 하나를 딕셔너리로 바꾼다. 패턴에 안 맞으면 None
    m = re.search(PATTERN, line)
    if m:
        return m.groupdict()
    return None


rows = []       # 맞은 줄
unmatched = []  # 안 맞은 줄

with open("raw_logs.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        row = parse_raw_logs(line)
        if row:
            rows.append(row)
        else:
            unmatched.append(line)

with open("normalized_logs.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)

with open("unmatched_logs.txt", "w", encoding="utf-8") as f:
    for line in unmatched:
        f.write(line + "\n")

print(f"정규화 {len(rows)}건 / 안 맞음 {len(unmatched)}건")
