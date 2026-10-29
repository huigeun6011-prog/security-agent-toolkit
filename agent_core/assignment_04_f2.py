counts = [0, 4, 2, 5]
selected = 0
total = 0

for n in counts:
    if n >= 3:
        selected += 1
        total += n

print(selected, total)