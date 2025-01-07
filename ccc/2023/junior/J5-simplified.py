word = input("")
rows = int(input(""))
columns = int(input(""))
grid = []
starts = []
result = 0

for _ in range(rows):
    row = input("")
    grid.append((row.split()))

def isInBounds(row, col):
    return row >= 0 and col >= 0 and row < rows and col < columns

up = [0, -1]
down = [0, 1]
left = [-1, 0]
right = [1, 0]
leftUp = [-1, -1]
leftDown = [1, -1]
rightUp = [-1, 1]
rightDown = [1, 1]

left.extend([up, down])
right.extend([up, down])
up.extend([left, right])
down.extend([left, right])
leftUp.extend([leftDown, rightUp])
leftDown.extend([leftUp, rightDown])
rightUp.extend([leftDown, rightUp])
rightDown.extend([leftUp, rightDown])

def hasDirection(letter, row, col, direction):
    return isInBounds(row + direction[0], col + direction[1]) and grid[row + direction[0]][col + direction[1]] == letter

def checkDirection(letterIndex, row, col, direction, hasTurned = False):
    if letterIndex+1 >= len(word):
        global result
        result += 1
        return
    
    if not hasTurned and letterIndex != 0:
        if hasDirection(word[letterIndex+1], row, col, direction[2]):
            checkDirection(letterIndex+1, row + direction[2][0], col + direction[2][1], direction[2], True)
        if hasDirection(word[letterIndex+1], row, col, direction[3]):
            checkDirection(letterIndex+1, row + direction[3][0], col + direction[3][1], direction[3], True)
    
    if hasDirection(word[letterIndex+1], row, col, direction):
        checkDirection(letterIndex+1, row + direction[0], col + direction[1], direction, hasTurned)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == word[0]:
            checkDirection(0, i, j, left)
            checkDirection(0, i, j, right)
            checkDirection(0, i, j, up)
            checkDirection(0, i, j, down)
            checkDirection(0, i, j, leftUp)
            checkDirection(0, i, j, leftDown)
            checkDirection(0, i, j, rightUp)
            checkDirection(0, i, j, rightDown)

print(result)
