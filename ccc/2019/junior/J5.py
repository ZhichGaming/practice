# Rule of Three

rules = []

for _ in range(3):
    rules.append(list(input().split()))

steps, initial, final = input().split()
steps = int(steps)
finished = False

previous = {}

def recursiveTraverse(current, operations):
    global steps, initial, final, rules, finished

    if finished:
        return

    # print(operations, steps)
    if len(operations) == steps and current == final:
        finished = True
        for operation in operations:
            print(operation)
        return

    if len(operations) > steps:
        return 
    
    try:
        if current in previous[len(operations)]:
            return
        
        previous[len(operations)].add(current)
    except:
        previous[len(operations)] = set()

    for i, rule in enumerate(rules):
        index = current.find(rule[0])

        while index < len(current):
            if index == -1:
                break

            new_operations = operations.copy()
            operation = str(i+1) + " " + str(index+1) + " " + current.replace(rule[0], rule[1], 1)
            new_operations.append(operation)

            recursiveTraverse(current.replace(rule[0], rule[1], 1), new_operations)
            index = current.find(rule[0], index+len(rule[0]))
            
recursiveTraverse(initial, [])
