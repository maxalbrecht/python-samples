from math import *
def polysum(n = 1,s = 1.0):
    area = (
        (
            (1.0/4.0)
            *n
            *(s**2)
        )
        /
        (
        tan(pi/n)
        )
    )
    perimeter = n*s
    ##
    return(
        round(
            (area+(perimeter**2))
            ,4
        )
    )
