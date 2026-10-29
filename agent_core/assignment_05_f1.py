raw = "abc"

try:
    print(int(raw))
except:
    print("숫자가 아닙니다")
finally:
    print("확인 끝")