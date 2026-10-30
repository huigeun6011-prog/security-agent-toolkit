with open("check.txt", "w", encoding="utf-8") as f:
    f.write("점검 시작\n점검 끝")
with open("check.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line, end="")