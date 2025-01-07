import copy
import sys

coins = []
cases = []

while True:
    current_coins = int(input(""))

    if current_coins == 0:
        break

    current_case = list(map(list, input("").split(" ")))

    for i in range(len(current_case)):
        current_case[i] = list(map(int, current_case[i]))


    coins.append(current_coins)
    cases.append(current_case)

def swap(current: list[list[int]], i, swap_to) -> list[list[int]]:
    result = copy.deepcopy(current)
    
    if len(result[i]) == 0:
        return copy.deepcopy(current)
    
    original = result[i][0]

    # Check if it is possible to swap to the left.
    if swap_to == -1 and i != 0:
        # Check if value on the left is less than new value. 
        if len(current[i-1]) != 0 and (current[i-1][0] < original):
            return copy.deepcopy(current)
        else:
            result[i-1].insert(0, original)
            result[i].pop(0)

            return result
    # Check if it is possible to swap to the right.
    elif swap_to == 1 and i + 1 < len(current):
        # Check if value on the right is less than new value. 
        if len(current[i+1]) != 0 and (current[i+1][0] < original):
            return copy.deepcopy(current)
        else:
            result[i+1].insert(0, original)
            result[i].pop(0)

            return result
    
    return copy.deepcopy(current)

def get_string_representation(current: list[list[int]]):
    result = [""]*len(current)

    for i in range(len(current)):
        result[i] = "".join(list(map(str, current[i])))
    
    return " ".join(result)

def dfs(current: list[list[int]], history: set[list[list[int]]], current_length: int = 0) -> int:
    one_dimensional = True

    flat = [item for sublist in current for item in sublist]
    soln = list(range(1, len(current)+1))

    for elem in current:
        if len(elem) != 1:
            one_dimensional = False

    # Win condition: it's sorted
    if one_dimensional and flat == soln:
        return current_length

    # detect cycle
    if get_string_representation(current) in history:
        return sys.maxsize
    
    new_history = copy.deepcopy(history)
    new_history.add(get_string_representation(current))

    results = []

    for i in range(len(current)):
        left_case = swap(current, i, -1)
        # print("left case", left_case)
        right_case = swap(current, i, 1)
        # print("right case", right_case)

        results.append(dfs(left_case, new_history, current_length+1))
        results.append(dfs(right_case, new_history, current_length+1))

    return min(results)

for case in cases:
    result = dfs(case, set())

    print(result if result != sys.maxsize else "IMPOSSIBLE")
    