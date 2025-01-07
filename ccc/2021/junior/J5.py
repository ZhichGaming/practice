# N rows, M columns
board = []
gold = 0

columns = int(input(""))
rows = int(input(""))

for i in range(columns):
    column = []

    for j in range(rows):
        column.append("B")
    
    board.append(column)

paint_count = int(input(""))

for _ in range(paint_count):
    current_instruction = input("").split(" ")

    if current_instruction[0] == "R":
        for i in range(len(board[0])):
            if board[int(current_instruction[1]) - 1][i] == "B":
                board[int(current_instruction[1]) - 1][i] = "G"
                gold += 1
            else:
                board[int(current_instruction[1]) - 1][i] = "B"
                gold -= 1
    else:
        for i in range(len(board)):
            if board[i][int(current_instruction[1]) - 1] == "B":
                board[i][int(current_instruction[1]) - 1] = "G"
                gold += 1
            else:
                board[i][int(current_instruction[1]) - 1] = "B"
                gold -= 1


print(gold)
