# pls let me code in peace...
current_size = int(input())

while True:
    enemy = int(input())

    if enemy < current_size:
        current_size += enemy
    else:
        break

print(current_size)
