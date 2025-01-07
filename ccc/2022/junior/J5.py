size = int(input())
number_of_trees = int(input())

board = [[False for i in range(size)] for j in range(size)]
trees = []

def minus1(number):
    return int(number) - 1

def boardIsTree(location):
    if location[0] >= len(board) and location[1] >= len(board[0]):
        return

    return board[location[0]][location[1]]

def boardIsTree(y, x):
    if y >= len(board) and x >= len(board[0]):
        return

    return board[y][x]

def squareContainsTree(y, x, length):
    if x+length > len(board) or y+length > len(board[0]):
        return True
    
    small_board = [row[x:(x+length)] for row in board[y:(y+length)]]

    # print(y, x, length)
    # print(small_board)

    return (True in [item for sub_list in small_board for item in sub_list])

for i in range(number_of_trees):
    tmp = (input().split(" "))
    trees.append(list(map(minus1, tmp)))
    board[(int(tmp[0]) - 1)][(int(tmp[1]) - 1)] = True

trees.append([0, 0])
# trees.append([len(board) - 1, len(board) - 1])

biggest_size = 0

for tree in trees:
    size = 0

    if not boardIsTree(tree[0]+1, tree[1]):
        length = 1

        while True:
            tmp = squareContainsTree(tree[0]+1, tree[1], length)

            if tmp == True:
                break
            else:
                length += 1

        size = length-1

    if not boardIsTree(tree[0], tree[1]+1):
        length = 1

        while True:
            tmp = squareContainsTree(tree[0], tree[1]+1, length)

            if tmp == True:
                break
            else:
                length += 1
        
        if length > size:
            size = length
    
    if size > biggest_size:
        biggest_size = size

print(biggest_size)
