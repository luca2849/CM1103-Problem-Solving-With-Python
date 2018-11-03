#Gauss' algorithm to find easter for a given year

y = int(input("Enter a year to find the date of easter for >>"))

def find_easter(y):
    a = y % 19
    b = y // 100
    c = y % 100
    d = b // 4
    e = b % 4
    g = (8 * b + 13) // 25
    h = (19 * a + b - d - g + 15) % 30
    j = c // 4
    k = c % 4
    m = (a + 11 * h) // 319
    r = (2 * e + 2 * j - k - h + m + 32) % 7
    n = (h - m + r + 90) // 25
    p = (h - m + r + n + 19) % 32
    p = str(p)
    if len(p) == 1:
        p = "0" + p
    return str(p) + "/0" + str(n)
