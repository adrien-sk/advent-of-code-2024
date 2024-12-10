
file = open('input.txt', 'r')
rules = {}
updates = []
res = 0

for line in file:
    if '|' in line:
        values = list(map(int, line.split('|')))

        if values[0] not in rules:
            rules[values[0]] = []
        rules[values[0]].append(values[1])
    elif ',' in line:
        updates.append(list(map(int, line.split(','))))


for update in updates:
    value = update[len(update) // 2]
    visited_pages = set()

    for page in update:
        if page in rules:
            for vp in visited_pages:
                if vp in rules[page]:
                    value = 0
                    break
        
        visited_pages.add(page)
    
    res += value

print(res)