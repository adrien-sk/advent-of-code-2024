
file = open('input.txt', 'r')
words = []
excluded_chars = ['A', 'X']
res = 0

# First: Extract input into a Matrix : O(n)
for line in file:
    letters = []

    for letter in line.strip('\n'):
        letters.append(letter)
    
    words.append(letters)

rows, cols = len(words), len(words[0])

# Third: Verify if we have a X-MAS
def FindWord(i, j):
    # IF top-left and bottom-right characters are different AND top-right and bottom-left characters are different
    # AND IF they're not 'X' or 'A' character
    if (    words[i - 1][j - 1] != words[i + 1][j + 1] and 
            words[i + 1][j - 1] != words[i - 1][j + 1] and 
            words[i - 1][j - 1] not in excluded_chars and words[i + 1][j + 1] not in excluded_chars and words[i + 1][j - 1] not in excluded_chars and words[i - 1][j + 1] not in excluded_chars):
        return 1
    
    return 0

# Second: Look for the center letter (A) in the matrix : O(n)
for i in range(1,len(words) - 1):
    for j in range(1, len(words[0]) - 1):
        if words[i][j] == 'A':
            res += FindWord(i, j)

print(res)