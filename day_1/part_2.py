from collections import defaultdict

left_list, right_collection = [], defaultdict(int)
file = open('input.txt', 'r')

# Read each line in file : O(n)
for line in file:
    values = list(map(int, line.split('   ')))
    left_list.append(values[0])
    right_collection[values[1]] += 1

file.close()

score = 0

# Traverse list : O(n)
for num in left_list:
    score += num * right_collection[num]

print(score)