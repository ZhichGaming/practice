prev_direction = ""
results = []

while True:
    str_input = input("")
    current_input = int(str_input)

    if str_input == "99999":
        break

    current_input_split = [str_input[0], str_input[1]]

    current_sum = 0
    for elem in current_input_split:
        current_sum += int(elem)

    last_three = str_input[len(str_input)-4:len(str_input)-1]

    if current_sum == 0:
        results.append(prev_direction + " " + last_three)
    elif current_sum % 2 != 0:
        prev_direction = "left"
        results.append("left" + " " + last_three)
    else: 
        prev_direction = "right"
        results.append("right" + " " + last_three)

for result in results:
    print(result)
