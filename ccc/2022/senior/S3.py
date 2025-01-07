'''
# When you pull out geometric sums, you know something has gone wrong.
import math

notes, maximum, required_samples = map(int, input().split())

def get_good_samples():
    current = 1
    piece = []

    def get_sample_count():
        cycles = len(piece) - maximum + 1
        print(piece, cycles)

        result = 0

        if cycles <= 0:
            result = (len(piece)*(len(piece)+1)/2)
        else:
            result = cycles * (maximum*(maximum+1)/2)

        print(result)
        return result

    sample_count = 0

    for i in range(notes):
        if current > maximum:
            current = 1
        
        piece.append(current)

        sample_count = get_sample_count()

        if sample_count > required_samples:
            break
        
        current += 1
    
    remaining_places = notes - len(piece)
    samples_to_remove = required_samples - sample_count - remaining_places

    print(required_samples, sample_count, remaining_places, samples_to_remove)
    print(piece[-1])

    starting_index = 1

    while samples_to_remove > 0:
        removal_amount = max(samples_to_remove, piece[-starting_index]) - 1
        piece[-starting_index] -= removal_amount
        samples_to_remove -= removal_amount

        starting_index += 1

    piece.extend([piece[-1] for _ in range(remaining_places)])
    
    return piece

print(get_good_samples())
'''

# This might be the correct solution but I'm redoing it.
'''
notes, maximum, required_samples = map(int, input().split())

def get_good_samples():
    global notes, maximum, required_samples

    result = []

    for i in range(notes):
        remainingPlaces = notes - (i + 1)

        # max count of samples placeable here, leaving at least 1 sample for every remaining place in the piece
        maxCurrentSamples = min(required_samples - remainingPlaces, maximum)

        if maxCurrentSamples <= 0:
            break

        tmp = 0

        if maxCurrentSamples > i:
            tmp = min(i + 1, maximum)
            maxCurrentSamples = tmp
        else:
            tmp = result[i - maxCurrentSamples]
        
        result.append(tmp)
        required_samples -= maxCurrentSamples
    
    if len(result) == notes and required_samples == 0:
        return " ".join(map(str, result))
    else:
        return "-1"

print(get_good_samples())
'''
N, M, K = map(int, input().split())

answer = []

for i in range(N):
    remaining_places = N - i - 1
    max_samples = K - remaining_places

    if max_samples < 0:
        break

    current_sample_count = min(M, max_samples)
    max_pitch_index = i - current_sample_count

    if max_pitch_index >= len(answer):
        break
    
    if max_pitch_index < 0:
        answer.append(i + 1)

        current_sample_count = i + 1
    else:
        answer.append(answer[max_pitch_index])
    
    K -= current_sample_count

if len(answer) == N and K == 0:
    print(" ".join(map(str, answer)))
else:
    print(-1)
