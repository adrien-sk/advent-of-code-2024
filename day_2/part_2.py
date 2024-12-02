file = open('input.txt', 'r')
safe_reports = 0

def validate_level(levels):
    tolerance = True
    
    # Check if level increment or decrement (Similar 2 first levels will be checked in the loop)
    increasing = False
    if levels[0] < levels[1]:
        increasing = True

    for i in range(1, len(levels)):
        # Unsafe : Same value for 2 level
        if levels[i - 1] == levels[i]:  
            if tolerance:
                tolerance = False
            else:
                return 0
        
        # Unsafe : Level difference > 3
        difference = abs(levels[i - 1] - levels[i])
        if difference > 3:
            if tolerance:
                tolerance = False
            else:
                return 0
        
        # Unsafe : Changing way
        if increasing and levels[i - 1] > levels[i]:
            if tolerance:
                tolerance = False
            else:
                return 0
        
        if not increasing and levels[i - 1] < levels[i]:
            if tolerance:
                tolerance = False
            else:
                return 0

    return 1
    

# Read each line in file : O(n)
for report in file:
    levels = list(map(int, report.split(' ')))

    # If level is safe, increment the counter
    safe_reports += validate_level(levels)
    
file.close()

print(safe_reports)