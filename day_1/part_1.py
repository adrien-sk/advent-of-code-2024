def populateList():
    file = open('input.txt', 'r')

    for line in file:
        values = list(map(int, line.split('   ')))
        left_list.append(values[0])
        right_list.append(values[1])

    file.close()


left_list, right_list = [], []
populateList()      # Read each line in file : O(n)
left_list.sort()    # Sorting list : O(n Log n)
right_list.sort()   # Sorting list : O(n Log n)

total_distance = 0

# Traverse list : O(n)
for i in range(len(left_list)):
    total_distance += abs(left_list[i] - right_list[i])

print(total_distance)