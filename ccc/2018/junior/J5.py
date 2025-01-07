number_of_pages = int(input())
pages = []
attempts = []
flat_attempts = []
lowest_length = -1

for i in range(number_of_pages):
    tmp = input().split(" ")

    if len(tmp) == 0:
        pages.append([])
        break

    pages.append(list(map(int, tmp[1:])))

def recursiveFind(current, history):
    global lowest_length

    content = pages[current - 1]

    if not current in flat_attempts:
        flat_attempts.append(current)
    
    if current in history[:-1] or len(content) == 0:
        attempts.append(history)
        
        if lowest_length == -1 or lowest_length > len(history):
            lowest_length = len(history)

        return
    
    for elem in content:
        new_history = history.copy()
        new_history.append(elem)
        
        recursiveFind(elem, new_history)

recursiveFind(1, [1])

if number_of_pages == 0:
    lowest_length = 0

# print(attempts)
print("Y" if len(flat_attempts) == number_of_pages else "N")
print(lowest_length)
