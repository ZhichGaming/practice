swaps = 0
initial = input("")

# Get index of last L.
def getLastLIndex():
    reversed = initial[::-1]

    for i in range(len(reversed)):
        if reversed[i] == "L":
            return len(initial) - 1 - i
    
    return -1

# Get index of last sorted L. Returns -1 if none.
def getLastSortedLIndex():
    for i in range(len(initial)):
        if initial[i] != "L":
            return i-1

# Get the number of letters (L, S, M) depending on the input letter before an index. Ignores the Ls at the beginning.
def getNumberOfLetterBefore(letter, before):
    result = 0
    letters = initial.lstrip("L")

    for i in range(before):
        if letter == letters[i]:
            result += 1

    return result

# def replaceAtIndex(index, letter, variable):
#     print(variable[:index] + letter + variable[index+1:])
#     new_value = variable[:index] + letter + variable[index+1:]
#     initial = new_value

# Move all Ls
if getLastLIndex() != -1:
    while True:
        last_L_index = getLastLIndex()
        numberOfNonLetter = getNumberOfLetterBefore("M", last_L_index) + getNumberOfLetterBefore("S", last_L_index)
        numberOfLetter = getNumberOfLetterBefore("L", last_L_index)

        last_sorted_L_index = getLastSortedLIndex()

        if last_L_index == last_sorted_L_index:
            break

        # Swap first non-L character with last L if it's more efficient than moving them out.
        if numberOfNonLetter > numberOfLetter:
            tmp = initial[last_sorted_L_index+1]
            initial = initial[:last_sorted_L_index+1] + "L" + initial[last_sorted_L_index+2:]
            initial = initial[:last_L_index] + tmp + initial[last_L_index+1:]
            swaps += 1

# ----------------------------------------------------------------------------------------------------

# Get index of first S.
def getFirstSIndex():
    for i in range(len(initial)):
        if initial[i] == "S":
            return i
    
    return -1

# Get index of last sorted s.
def getFirstSortedSIndex():
    reversed = initial[::-1]

    if reversed[0] != "S":
        return -1
    
    for i in range(len(reversed)):
        if reversed[i] != "S":
            # Account -1 for index, +1 for because you're getting the index of the letter that is before the one which isn't S.
            return len(initial) - i

# Get the number of letters (L, S, M) depending on the input letter after an index. Ignores the Ss at the end.
def getNumberOfLetterAfter(letter, after):
    reversed = initial[::-1]
    result = 0
    letters = reversed.lstrip("S")

    for i in range(len(reversed) - after - 1):
        if letter == letters[i]:
            result += 1

    return result

# Move all Ss
if getFirstSIndex() != -1:
    while True:
        first_S_index = getFirstSIndex()
        numberOfNonLetter = getNumberOfLetterAfter("M", first_S_index) + getNumberOfLetterAfter("L", first_S_index)
        numberOfLetter = getNumberOfLetterAfter("S", first_S_index)

        first_sorted_S_index = getFirstSortedSIndex()

        if first_S_index == first_sorted_S_index:
            break

        # Swap last non-S character with first S if it's more efficient than moving them out.
        if numberOfNonLetter > numberOfLetter:
            if first_sorted_S_index == -1:
                tmp = initial[len(initial) - 1]
                initial = initial[:len(initial) - 1] + "S"
                initial = initial[:first_S_index] + tmp + initial[first_S_index+1:]
                swaps += 1
            else:
                tmp = initial[first_sorted_S_index-1]
                initial = initial[:first_sorted_S_index] + "S" + initial[first_sorted_S_index:]
                initial = initial[:first_S_index] + tmp + initial[first_S_index-1:]
                swaps += 1

print(swaps)
