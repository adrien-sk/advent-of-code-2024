
file = open('input.txt', 'r')
words = []
directions = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
word_to_search = 'XMAS'
res = 0

# First: Extract input into a Matrix : O(n)
for line in file:
    letters = []

    for letter in line.strip('\n'):
        letters.append(letter)
    
    words.append(letters)

rows, cols = len(words), len(words[0])

def SearchLetters(i, j, dir_i, dir_j):
    depth = 1
    for word_i in range(2, len(word_to_search)):
        new_i = i + dir_i * depth
        new_j = j + dir_j * depth

        if (    new_i < 0 or 
                rows <= new_i or
                new_j < 0 or 
                cols <= new_j or
                word_to_search[word_i] != words[new_i][new_j]):
            return 0

        depth += 1
        
    return 1


def FindWord(i, j):
    # Third: Search all 8 directions for the 2nd letter M
    res = 0

    for dir_i, dir_j in directions:
        new_i, new_j = i + dir_i, j + dir_j

        if (    0 <= new_i < rows and
                0 <= new_j < cols and
                words[new_i][new_j] == word_to_search[1]):
            # Fourth, If found M, look in the same direction for the remaining letters A and S
            res += SearchLetters(new_i, new_j, dir_i, dir_j)
    
    return res


# Second: Look for the 1st letter (X) in the matrix : O(n)
for i in range(len(words)):
    for j in range(len(words[0])):
        if words[i][j] == word_to_search[0]:
            res += FindWord(i, j)

print(res)