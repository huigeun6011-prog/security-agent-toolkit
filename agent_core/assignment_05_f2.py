values = ["2", "bad", "3"]
total = 0

for n in values:
    try:
        total += int(n)
    except:
        print("건너뜀",n)
        continue
print("합계",total)