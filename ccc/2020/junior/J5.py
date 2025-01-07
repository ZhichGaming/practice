board = []
flatboard = []

rowNums = int(input())
colNums = int(input())

for i in range(rowNums):
    item = map(int, input().split(" "))
    board.append(list(item))

flatboard = [item for sublist in board for item in sublist]
is_possible = False
history = []

def findPrevious(x, y):
    global is_possible

    if (x, y) in history:
        return
    
    if (x == 0 and y == 0):
        is_possible = True
        return

    num = (y+1)*(x+1)
    current_flatboard = flatboard
    location = 0

    # print("num", num)

    try:
        location = current_flatboard.index(num)
    except:
        # print(y, x)
        return

    while True:
        current_flatboard[location] = -1

        new_y = 0
        tmp = location - colNums

        while tmp > 0:
            new_y += 1
            tmp -= rowNums

        history.append((x, y))
        findPrevious(tmp + colNums, new_y)

        try:
            location = current_flatboard.index(num)
        except:
            break

findPrevious(rowNums-1, colNums-1)

if is_possible:
    print("yes")
else:
    print("no")
