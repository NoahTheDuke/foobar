def answer(minions):
    # n = numerator
    # d = denominator
    # r = reverse: denominator - numerator
    #result = [[time, n, d, d - n] for [time, n, d] in minions]
    #magic_number = [(time/(n/d)) for idx, [time, n, d, r] in enumerate(result)]
    magic_number = [(float(time)/(float(n)/float(d)), idx) for idx, [time, n, d] in enumerate(minions)]
    magic_number.sort()
    return [x for (_, x) in magic_number]

#minions = [[10, 1, 2], [5, 1, 5]]
#answer_order = [0, 1]
minions = [[10, 1, 2], [5, 1, 5], [2, 5, 7]]
answer_order = [2, 0, 1]
#minions = [[390, 185, 624], [686, 351, 947], [276, 1023, 1024], [199, 148, 250]]
#answer_order = [2, 3, 0, 1]

ans = answer(minions)
print(ans)
print(answer_order == ans)
