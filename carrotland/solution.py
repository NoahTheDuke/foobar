from fractions import gcd
def answer(vertices):
    # Shoelace Formula
    # Find the area of the triangle:
    # Take a triangle with coordinates [2, 1], [4, 5], [7, 8]].
    # Take the first x-coordinate and multiply it by the second y-value,
    # then take the second x-coordinate and multiply it by the third y-value,
    # and repeat, and repeat again, until you do it for all points.
    # --
    # GCD
    # Cound border points with Greatest Common Divisor
    # --
    # Pick's Theorem
    # Interior points = Area - (Border points / 2) + 1
    x1, y1 = vertices[0]
    x2, y2 = vertices[1]
    x3, y3 = vertices[2]
    A = (1.0/2.0) * abs(x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3)
    B =  (gcd(abs(x1 - x2), abs(y1 - y2))
        + gcd(abs(x2 - x3), abs(y2 - y3))
        + gcd(abs(x3 - x1), abs(y3 - y1)))
    I = int(A - B/2 + 1)
    return I

#vertices = [[2, 3], [6, 9], [10, 160]]
#answer_num = 289
vertices = [[91207, 89566], [-88690, -83026], [67100, 47194]]
answer_num = 1730960165
ans = answer(vertices)
print(ans)
print(ans == answer_num)
