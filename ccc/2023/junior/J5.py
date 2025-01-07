word = input("")
rows = int(input(""))
columns = int(input(""))
grid = []
result = 0

for _ in range(rows):
    row = input("")
    grid.append((row.split()))

def isInBounds(row, col):
    return row >= 0 and col >= 0 and row < rows and col < columns

def hasLeft(letter, row, col):
    return isInBounds(row, col-1) and grid[row][col - 1] == letter
def hasRight(letter, row, col):
    return isInBounds(row, col+1) and grid[row][col + 1] == letter
def hasUp(letter, row, col):
    return isInBounds(row-1, col) and grid[row - 1][col] == letter
def hasDown(letter, row, col):
    return isInBounds(row+1, col) and grid[row + 1][col] == letter
def hasLeftUp(letter, row, col):
    return isInBounds(row-1, col-1) and grid[row - 1][col - 1] == letter
def hasLeftDown(letter, row, col):
    return isInBounds(row+1, col-1) and grid[row + 1][col - 1] == letter
def hasRightUp(letter, row, col):
    return isInBounds(row-1, col+1) and grid[row - 1][col + 1] == letter
def hasRightDown(letter, row, col):
    return isInBounds(row+1, col+1) and grid[row + 1][col + 1] == letter

def checkLeft(letterIndex, row, col, hasTurned = False):
    if letterIndex+1 >= len(word):
        global result
        result += 1
        return
    
    if not hasTurned and letterIndex != 0:
        if hasUp(word[letterIndex+1], row, col):
            checkUp(letterIndex+1, row-1, col, True)
        if hasDown(word[letterIndex+1], row, col):
            checkDown(letterIndex+1, row+1, col, True)
    
    if hasLeft(word[letterIndex+1], row, col):
        checkLeft(letterIndex+1, row, col-1, hasTurned)

def checkRight(letterIndex, row, col, hasTurned = False):
    if letterIndex+1 >= len(word):
        global result
        result += 1
        return
    
    if not hasTurned and letterIndex != 0:
        if hasUp(word[letterIndex+1], row, col):
            checkUp(letterIndex+1, row-1, col, True)
        if hasDown(word[letterIndex+1], row, col):
            checkDown(letterIndex+1, row+1, col, True)
    
    if hasRight(word[letterIndex+1], row, col):
        checkRight(letterIndex+1, row, col+1, hasTurned)

def checkUp(letterIndex, row, col, hasTurned = False):
    if letterIndex+1 >= len(word):
        global result
        result += 1
        return
    
    if not hasTurned and letterIndex != 0:
        if hasLeft(word[letterIndex+1], row, col):
            checkLeft(letterIndex+1, row, col-1, True)
        if hasRight(word[letterIndex+1], row, col):
            checkRight(letterIndex+1, row, col+1, True)
    
    if hasUp(word[letterIndex+1], row, col):
        checkUp(letterIndex+1, row-1, col, hasTurned)

def checkDown(letterIndex, row, col, hasTurned = False):
    if letterIndex+1 >= len(word):
        global result
        result += 1
        return
    
    if not hasTurned and letterIndex != 0:
        if hasLeft(word[letterIndex+1], row, col):
            checkLeft(letterIndex+1, row, col-1, True)
        if hasRight(word[letterIndex+1], row, col):
            checkRight(letterIndex+1, row, col+1, True)
    
    if hasDown(word[letterIndex+1], row, col):
        checkDown(letterIndex+1, row+1, col, hasTurned)

def checkLeftUp(letterIndex, row, col, hasTurned = False):
    if letterIndex+1 >= len(word):
        global result
        result += 1
        return
    
    if not hasTurned and letterIndex != 0:
        if hasLeftDown(word[letterIndex+1], row, col):
            checkLeftDown(letterIndex+1, row+1, col-1, True)
        if hasRightUp(word[letterIndex+1], row, col):
            checkRightUp(letterIndex+1, row-1, col+1, True)
    
    if hasLeftUp(word[letterIndex+1], row, col):
        checkLeftUp(letterIndex+1, row-1, col-1, hasTurned)

def checkLeftDown(letterIndex, row, col, hasTurned = False):
    if letterIndex+1 >= len(word):
        global result
        result += 1
        return
    
    if not hasTurned and letterIndex != 0:
        if hasLeftUp(word[letterIndex+1], row, col):
            checkLeftUp(letterIndex+1, row-1, col-1, True)
        if hasRightDown(word[letterIndex+1], row, col):
            checkRightDown(letterIndex+1, row+1, col+1, True)
    
    if hasLeftDown(word[letterIndex+1], row, col):
        checkLeftDown(letterIndex+1, row+1, col-1, hasTurned)

def checkRightUp(letterIndex, row, col, hasTurned = False):
    if letterIndex+1 >= len(word):
        global result
        result += 1
        return
    
    if not hasTurned and letterIndex != 0:
        if hasLeftUp(word[letterIndex+1], row, col):
            checkLeftUp(letterIndex+1, row-1, col-1, True)
        if hasRightDown(word[letterIndex+1], row, col):
            checkRightDown(letterIndex+1, row+1, col+1, True)
    
    if hasRightUp(word[letterIndex+1], row, col):
        checkRightUp(letterIndex+1, row-1, col+1, hasTurned)

def checkRightDown(letterIndex, row, col, hasTurned = False):
    if letterIndex+1 >= len(word):
        global result
        result += 1
        return
    
    if not hasTurned and letterIndex != 0:
        if hasLeftDown(word[letterIndex+1], row, col):
            checkLeftDown(letterIndex+1, row+1, col-1, True)
        if hasRightUp(word[letterIndex+1], row, col):
            checkRightUp(letterIndex+1, row-1, col+1, True)
    
    if hasRightDown(word[letterIndex+1], row, col):
        checkRightDown(letterIndex+1, row+1, col+1, hasTurned)

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == word[0]:
            checkLeft(0, i, j)
            checkRight(0, i, j)
            checkUp(0, i, j)
            checkDown(0, i, j)
            checkLeftUp(0, i, j)
            checkLeftDown(0, i, j)
            checkRightUp(0, i, j)
            checkRightDown(0, i, j)

print(result)