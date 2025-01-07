number_of_inputs = int(input(""))
inputs = []
max = []

for i in range(number_of_inputs):
    current_name = input("")
    current_bid = int(input(""))

    if len(max) != 0:
        if max[1] < current_bid:
            max = [current_name, current_bid]
    else:
        max = [current_name, current_bid]

    inputs.append([current_name, current_bid])

print(max[0])
