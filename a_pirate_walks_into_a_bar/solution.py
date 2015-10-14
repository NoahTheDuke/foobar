from random import shuffle

def answer(numbers):
    idx = 0
    seen = []
    while numbers[idx] not in seen:
            seen.append(numbers[idx])
            idx = seen[-1]
    else:
        seen.append(numbers[idx])
        seen = seen[numbers[idx]:]
    return len(seen)

test = [1, 3, 0, 1]
print answer(test)
