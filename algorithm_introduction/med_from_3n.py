# find median number from 3 integers
def med(a,b,c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a 
    elif b > c:
        return c
    else: 
        return b
    