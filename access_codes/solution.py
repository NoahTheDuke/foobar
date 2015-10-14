def answer(x):
    result = []
    for item in x:
        if item not in result:
            if item[::-1] not in result:
                result.append(item)
    return len(result)

#test = ["abc", "cba", "bac"]
#test = ["foo", "bar", "oof", "bar"]
test = ["x", "y", "xy", "yy", "", "yx"]
print answer(test)
