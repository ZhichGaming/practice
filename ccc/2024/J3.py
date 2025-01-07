# lmfao he can't find his file from
participant_count = int(input())
scores = []

for i in range(participant_count):
    scores.append(int(input()))

scores.sort()


last = -1
current_medal = 0
bronze_score = 0
bronze_people = 0

for score in scores[::-1]:
    if last != score:
        current_medal += 1
    
    if current_medal == 3:
        bronze_score = score
        bronze_people += 1
    elif current_medal > 3:
        break

    last = score

print(bronze_score, bronze_people)
# ez, it's now 6:56