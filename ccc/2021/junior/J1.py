def boiling_water(temp):
    p = temp*5-400
    print(p)

    if p < 100:
        return 1
    elif p == 100:
        return 0
    else:
        return -1

temprature = int(input(""))
print(boiling_water(temprature))