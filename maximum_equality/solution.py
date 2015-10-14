from collections import Counter
from random import randrange

def most_common(lst):
    data = Counter(lst)
    return data.most_common(1)[0][1]

def answer(x):
    """The goal is to take all of the rabbits in list x and distribute
    them equally across the original list elements."""
    total = sum(x)
    length = len(x)
    # Find out how many are left over when distributing niavely.
    div, mod = divmod(total, length)
    # Because of the variable size of the list, the remainder
    # might be greater than the length of the list.
    # I just realized this is unnecessary.
    while mod > length:
        div += length
        mod -= length
    # Create a new list the size of x with the base number of rabbits.
    result = [div] * length
    # Distribute the leftovers from earlier across the list.
    for i in xrange(mod):
        result[i] += 1
    # Return the most common element.
    return most_common(result)

#for y in range(1000):
l = randrange(2, 100)
x = [randrange(0, 1000000) for _ in xrange(l)]
#x = [1, 2]
print(answer(x))
