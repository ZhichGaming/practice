rows = int(input())
columns = int(input())

objects = []
board = []

def replace_ten(elem):
    if elem == "L":
        return "10"
    return elem

for i in range(rows):
    current = list(map(replace_ten, list(input().replace("S", "1").replace("M", "5"))))
    board.append(current)
    objects += current

start_row = int(input())
start_col = int(input())

result = 0

# 1 point sol
# if rows*columns < 100:
#     for row in board:
#         if "*" in row:
#             break

#         result += sum(list(map(int, row)))

# def bfs_edge(current_level: list, visited: set, start_edge: str, end_edge: str = ""):
#     next_level = []
    
#     new_start_edge = start_edge
#     new_end_edge = end_edge

#     for coord in current_level:
#         if coord in visited:
#             continue

#         y, x = list(coord)

#         visited.add(y+x)
    
#     bfs_edge(next_level, visited, start_edge, end_edge)

# star_



def is_in_bounds(y, x):
    return x >= 0 and y >= 0 and len(board) > y and len(board[0]) > x

def format_to_str(y, x):
    return str(y)+ "," + str(x)

def look_at(y, x):
    if not is_in_bounds(y, x):
        return 0
    
    if board[y][x] == "*":
        return 0
    else:
        return int(board[y][x])

def get_available_spaces(y, x, visited):
    available_spaces = set()

    left = [y, x-1]
    right = [y, x+1]
    up = [y-1, x]
    down = [y+1, x]

    if is_in_bounds(*left) and (format_to_str(*left) not in visited):
        available_spaces.add(format_to_str(*left))
    if is_in_bounds(*right) and (format_to_str(*right) not in visited):
        available_spaces.add(format_to_str(*right))
    if is_in_bounds(*up) and (format_to_str(*up) not in visited):
        available_spaces.add(format_to_str(*up))
    if is_in_bounds(*down) and (format_to_str(*down) not in visited):
        available_spaces.add(format_to_str(*down))
    
    return available_spaces

def bfs(current_level: set[str], visited: set):
    global result
    next_level = set()

    for pos in current_level:
        if pos in visited:
            continue



        visited.add(pos)

        y, x = list(map(int, pos.split(",")))
        if board[y][x] == "*":
            continue

        left = look_at(y, x-1)
        right = look_at(y, x+1)
        up = look_at(y-1, x)
        down = look_at(y+1, x)
        # print(y, x)
        # print(left)
        # print(right)
        # print(up)
        # print(down)
        result += look_at(y, x)

        next_level = next_level | get_available_spaces(y, x, visited)

        # if left == 0:
        #     visited.add(format_to_str(y, x-1))
        # else:
        #     result += left
        #     new_spaces = get_available_spaces(y, x-1, visited)
        #     next_level = next_level | (new_spaces)
        
        # if right == 0:
        #     visited.add(format_to_str(y, x+1))
        # else:
        #     result += right
        #     new_spaces = get_available_spaces(y, x+1, visited)
        #     next_level = next_level | (new_spaces)

        # if up == 0:
        #     visited.add(format_to_str(y-1, x))
        # else:
        #     result += up
        #     new_spaces = get_available_spaces(y-1, x, visited)
        #     next_level = next_level | (new_spaces)
        
        # if down == 0:
        #     visited.add(format_to_str(y+1, x))
        # else:
        #     result += down
        #     new_spaces = get_available_spaces(y+1, x, visited)
        #     next_level = next_level | (new_spaces)
    
    if len(next_level) != 0:
        bfs(next_level, visited)

hmm = set()
hmm.add(format_to_str(start_row, start_col))
bfs(hmm, set())

print(result)
