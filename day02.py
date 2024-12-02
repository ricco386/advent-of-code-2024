# https://adventofcode.com/2024/day/2

reports = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]

def find_safe_report_and_calculate(report):
    safe = True
    min_adjustment = 0
    max_adjustment = 4

    for i, value in enumerate(report):

        if i == 0:
            if value > report[1]:
                rtype = 'DE'
            else:
                rtype = 'IN'
            continue

        elif not(min_adjustment < abs(value - report[i-1]) < max_adjustment):
            safe = False
            continue
        elif value > report[i-1] and rtype == 'DE':
            safe = False
            continue
        elif value < report[i-1] and rtype == 'IN':
            safe = False
            continue

    return int(safe)

total = 0

for r in reports:
    total += find_safe_report_and_calculate(r)

print(total)
