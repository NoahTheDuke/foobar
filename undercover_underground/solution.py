import math

# See: http://jacquerie.github.io/google-foobar-post-mortem/
# and: http://oeis.org/A123527
# and: http://oeis.org/A062734
def answer(n, k):
    return "{}".format(q(n, k))

choose_memo = {}
qq_memo = {}

def q(n, k):
    if (k < n - 1) or (k > (n * n - 1) // 2):
        return 0
    if (n, k) in qq_memo:
        return qq_memo[(n, k)]
    if k == n - 1:
        answer = long(n**(n - 2))
        qq_memo[(n, k)] = answer
        return answer

    first = choose(n * (n - 1) // 2, k)
    second = get_second(n, k)

    answer = long(first - second)
    qq_memo[(n, k)] = answer
    return int(answer)

def get_second(n, k):
    total = 0
    for m in xrange(0, n - 1):
        coeff = choose(n - 1, m)
        total2 = 0
        for p in xrange(0, k + 1):
            coeff2 = choose(((n - 1 - m) * (n - 2 - m)) / 2, p)
            temp = q(m + 1, k - p)
            total2 += coeff2 * temp
        total += coeff * total2
    return total

def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if (n, k) in choose_memo:
        return choose_memo[(n, k)]

    m = n
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        result =  long(ntok // ktok)
    else:
        result = 0

    choose_memo[(m, k)] = result

    return result

#for n in xrange(2, 21):
    #for k in xrange(n-1, (n * (n - 1)) // 2 + 1):
        #answer(n,k)

#n, k = 2, 1
#ans_str = "1"
n, k = 4, 3
ans_str = "16"
ans = answer(n, k)
print(ans)
print(ans_str)
print(ans == ans_str)
