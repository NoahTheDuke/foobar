def answer(matrix):
    # your code here
    return

#Write a function answer(matrix) which returns the minimum number of lights that need to be touched to unlock the lock, by turning off all the lights. If it is not possible to do so, return -1.

test = [[1, 1], [0, 0]]
test_ans = 2
test = [[1, 1, 1], [1, 0, 0], [1, 0, 1]]
test_ans = -1
ans = answer(test)
print(ans)
print(ans == test_ans)
