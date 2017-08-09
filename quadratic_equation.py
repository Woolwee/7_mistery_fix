from math import sqrt
#from cmath import sqrt as csqrt  # I thought i should write a solution for
                                  # for complex cases


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        #root1 = (-b - csqrt(discriminant)) / (2 * a)
        #root2 = (-b + csqrt(discriminant)) / (2 * a)
        #return root1, root2
        return None, None
    else:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
        if discriminant == 0:
            return root1, None
        else:
            return root1, root2
