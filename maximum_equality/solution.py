from collections import Counter

def answer(x):
    result = x
    equal = False
    if sum(x) % len(x) > 0:
        spread = sum(x) - 1
        for idx in xrange(len(x)):
            result[idx] = spread % len(x)
        result[-1] -= 1
    else:
        while not equal:
            for idx, item in enumerate(x):
                result[idx] = sum(x)/len(x)
            equal = True
    if equal:
        return len(result)
    else:
        print "odd", result
        a = Counter(result)
        return a.most_common(1)[0][1]

x = [1, 4, 1, 1, 1, 3]
print answer(x)
