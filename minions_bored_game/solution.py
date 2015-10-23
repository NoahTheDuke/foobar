def solve(t, n):
    """
    Write a function answer(t, n), which given the number of dice rolls t, and the number of squares in the board n, returns the possible number of unique games modulo 123454321. i.e. if the total number is S, then return the remainder upon dividing S by 123454321, the remainder should be an integer between 0 and 123454320 (inclusive).

    n and t will be positive integers, no more than 1000. n will be at least 2.
    """
    m, m2 = [0]*n, [0]*n
    m[0] = 1

    for i in xrange(t):
        print('\nn, t: ' + str(n) + " " + str(t))
        print('m, m2', m, m2)
        m, m2 = m2, m
        print('m, m2', m, m2)
        print('\ni: ' + str(i))
        for j in xrange(n):
            print('\nj: ' + str(j))
            print('m: ', m)
            print('m2: ', m2)
            m[j] = int(j>0 and m2[j-1])
            print('m[j] = int(j>0 and m2[j-1]) -> %s' % m[j])
            m[j] += m2[j]
            print('m[j] += m2[j] -> %s' % m[j])
            m[j] += (j+1<n-1 and m2[j+1])
            print('m[j] += (j+1<n-1 and m2[j+1]) -> %s' % m[j])
        print('m: ', m)

    S = m[-1]
    return S % 123454321


#t = 1
#n = 2
#answer = 1
#t = 3
#n = 2
#answer = 3
t = 20
n = 5
answer = 19535230
ans = solve(t, n)
print(ans)
print(ans == answer)
