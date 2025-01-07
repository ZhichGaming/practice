gates_count = int(input())
planes_count = int(input())
gates = [False] * gates_count
planes = []

for i in range(planes_count):
    planes.append(int(input()) - 1)

def start():
    result = 0

    for plane in planes:
        current_index = plane

        while current_index >= 0:
            if not gates[current_index]:
                gates[current_index] = True
                result += 1
                break
            
            current_index -= 1
        
        if current_index < 0:
            return result

    return result

print(start())
