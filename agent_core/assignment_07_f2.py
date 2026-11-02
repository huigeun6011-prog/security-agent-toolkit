groups = [[2, 1], [3, 0]]

for inner_box in groups:
    sum = 0
    for item in inner_box:
        sum += item
    print(sum)