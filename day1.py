# https://adventofcode.com/2024/day/1

a = [3, 4, 2, 1, 3, 3]
b = [4, 3, 5, 3, 9, 3]

def find_minimal_and_calculate():
    min_val_a = min(a)
    min_val_b = min(b)
    del(a[a.index(min_val_a)])
    del(b[b.index(min_val_b)])

    return abs(min_val_a - min_val_b)

total = 0

while len(a) > 0:
    total += find_minimal_and_calculate()

print(total)
