from math import factorial
from collections import Counter
from operator import mul
from functools import reduce

# See: http://jacquerie.github.io/google-foobar-post-mortem/
# and: http://oeis.org/A123527
# and: http://oeis.org/A062734
def answer(n, k):
    if (k < n - 1) or (k > (n * n - 1) / 2):
        return 0
    elif k == n - 1:
        result = n**(n - 2)
    else:
        result = qq(n, k)
    return str(result)

def qq(n, k):
    res = choose(n * (n - 1) / 2, k)
    for m in range(n - 2 + 1):
        res1 = 0
        for p in range(max(0, k - 1/2 * (m + 1) * m), k - m + 1):
            res1 = res1 + choose((n - 1 - m) * (n - 2 - m) / 2, p) * qq(m + 1, k - p)
        res = res - choose(n - 1, m) * res1
    return res

memoization = {}

def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if (n, k) in memoization:
        return memoization[(n, k)]

    m = n
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        result =  ntok // ktok
    else:
        result = 0

    memoization[(m, k)] = result

    return result

def prod(iterable):
    return reduce(mul, iterable, 1)

def gf2(n):
    s = 0
    a = accelAsc(n)
    for p in a:
        q = len(p)
        mcf1 = factorial(n)/prod(factorial(li) for li in p)
        cntr = Counter(p)
        mcf2 = factorial(q)/prod(factorial(li) for _, li in cntr.items())
        u = 1 # WHERE DOES u COME FROM
        s = s + ((-1)**(q + 1)) / q * mcf1 * mcf2 * (1 + u) ** sum((li * (li - 1) / 2) for li in p)
    return str(s)

def accelAsc(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2*x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]

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
