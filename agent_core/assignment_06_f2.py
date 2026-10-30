try:
    with open("not-provided.txt", encoding="utf-8") as f:
        for line in f:
            print(line, end='')
except FileNotFoundError:
    print("파일 위치를 확인하세요")
