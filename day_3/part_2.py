import re

# Open file and regex to find all string like : mul(123,123)
file = open('input.txt', 'r').read()
pattern = r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"
mul_list = re.findall(pattern, file)
res = 0
enabled = True

# For each string, regex to get the 2 numbers using Group, and multiply + sum to the result
for mul in mul_list:
    if mul == 'don\'t()':
        enabled = False
        continue
    elif mul == 'do()':
        enabled = True
        continue

    if not enabled:
        continue

    pattern_groups = r"mul\((\d{1,3}),(\d{1,3})\)"
    match = re.match(pattern_groups, mul)
    num1, num2 = match.groups()
    res += int(num1) * int(num2)

print(res)