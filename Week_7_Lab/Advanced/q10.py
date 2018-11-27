def rec_power(a,n):
    # if n is 1 then return a
    if n == 1:
        return a
    # recursively call this function for n/2 and call it factor
    n = n/2
    factor = rec_power(a, n)
    # if n/2 is even return the square of factor
    if (n/2) % 2 == 0:
        return factor * factor
    # if n/2 is odd then return the square of factor multiplied by a
    if (n/2) % 2 == 1:
        return factor * factor * a
print(rec_power(10, 4))
