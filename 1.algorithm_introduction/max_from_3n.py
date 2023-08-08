# find max number from three integers
def max_from_3n(a,b,c):
    max_n = a
    if b > max_n :
        max_n = b
    if c > max_n :
        max_n = c
    return max_n

print(f'max(3,2,1) = {max_from_3n(3,2,1)}')


# what is algorithm? -> you can get exactly same answer with same input with a sequence of system