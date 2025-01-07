columns = int(input(""))
tiles = []
result = 0

for i in range(2):
    row = input("").split()
    tiles.append(row)

def checkAround(row, column):
    tape = 0
    columnIsPair = column % 2 == 0
    rowIsPair = row % 2 == 0

    # check vertical
    if (row == len(tiles) - 1 or row == 0):
        if not columnIsPair:
            tape += 1
    if (row != 0 and (columnIsPair != rowIsPair)):
        if tiles[row-1][column] != "1":
            tape += 1
    if (row != len(tiles) - 1 and (columnIsPair == rowIsPair)):
        if tiles[row+1][column] != "1":
            tape += 1

    # check horizontal
    if (column == len(tiles[0]) - 1) or (column == 0):
        tape += 1
    if column != 0:
        if tiles[row][column-1] != "1":
            tape += 1
    if column != len(tiles[0]) - 1:
        if tiles[row][column+1] != "1":
            tape += 1

    return tape

for i in range(len(tiles)):
    for j in range(columns):
        if tiles[i][j] == "1":
            result += checkAround(i, j)

print(result)
