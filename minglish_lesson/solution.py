def answer(words):
    rules = []
    maxlength = max(len(s) for s in words)
    result = set()
    for x in range(maxlength):
        rule = []
        for word in words:
            if x < len(word):
                if word[x] not in rule:
                    rule.append(word[x])
                result.add(word[x])
        rules.extend([x for x in chunker(rule)])
    result = list(result)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for (lt, gt) in rules:
            r_lt, r_gt = result.index(lt), result.index(gt)
            if r_lt > r_gt:
                result[r_lt], result[r_gt] = result[r_gt], result[r_lt]
                is_sorted = False
    return "".join(result)

def chunker(seq):
    return (seq[pos:pos + 2] for pos in range(0, len(seq)) if pos + 2 <= len(seq))

words = (["z", "yx", "yzx", "yxy", "azy", "aza"], "xzya")
#words = (["y", "z", "xy"], "yzx")
#words = (["ba", "ab", "cb"], "bac")
ans = answer(words[0])
print('answer', ans)
print(ans == words[1])
