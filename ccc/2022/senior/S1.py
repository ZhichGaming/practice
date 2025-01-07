n = int(input())

ans = 0
possibilities = set()

for number_of_fives in range(n):
    value_of_fives = 5 * number_of_fives
    value_of_fours = n - value_of_fives

    if value_of_fours < 0:
        break

    identifier = (value_of_fives, value_of_fours)

    if value_of_fours % 4 == 0 and identifier not in possibilities:
        possibilities.add(identifier)
        ans += 1

print(ans)
