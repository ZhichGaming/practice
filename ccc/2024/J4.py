keys_pressed = input()
keys_registered = input()

quiet_pressed = len(keys_pressed) != len(keys_registered)

quiet_key = ""
silly_key_input = ""
silly_key_output = ""

registered_index = 0

def registered_index_inbounds():
    return registered_index < len(keys_registered)

def pressed_index_inbounds(i):
    return i < len(keys_pressed)

def is_anomaly(j):
    return keys_pressed[j] != keys_registered[registered_index]

def quiet_key_case(i):
    global quiet_key
    if quiet_key != "":
        # print("quiet key conserved", quiet_key)
        return
    
    quiet_key = keys_pressed[i]
    # print("quiet key pressed:", quiet_key)

def silly_key_case(i):
    global silly_key_input, silly_key_output
    if silly_key_input == "":
        silly_key_input = keys_pressed[i]
    else:
        # print("silly_key_input conserved instead of",keys_pressed[i])
        pass

    if silly_key_output == "":
        silly_key_output = keys_registered[registered_index]
    else:
        # print("silly_key_output conserved instead of",keys_registered[registered_index])
        pass

    # print("silly_key_input/output:", silly_key_input, silly_key_output)

def next_different_character_index(i):
    tmp = i
    current = keys_pressed[i]

    while tmp < len(keys_pressed):
        if keys_pressed[tmp] != current:
            # print("next diff char", tmp)
            return tmp
        
        tmp += 1
    
    # print("what?", i+1)
    return i+1

skips = 0

for i in range(len(keys_pressed)):
    if skips > 0:
        skips -= 1
        continue

    # isn't normal case
    if registered_index_inbounds() and is_anomaly(i):
        # print("pressed_index/registered:", i, registered_index)
        # quiet key case
        next_diff_char_index = next_different_character_index(i)

        if pressed_index_inbounds(next_diff_char_index) and not is_anomaly(next_diff_char_index):
            skips = next_diff_char_index-i-1
            # print("skips:", skips)

            quiet_key_case(i)
            continue
        
        # silly key case
        silly_key_case(i)
        registered_index += 1
    # elif is_anomaly(i):
    #     quiet_key_case(i)
    #     print("this was case 2")
    #     break
    else:
        # print("key corresponds at index", i, registered_index, keys_pressed[i], keys_registered[registered_index])
        if registered_index < len(keys_registered):
            registered_index += 1
        else:
            quiet_key_case(i)
            # print("this was case 3")
            break

print(silly_key_input, silly_key_output)
print(quiet_key if quiet_pressed else "-")
# i'm going crazy wtf