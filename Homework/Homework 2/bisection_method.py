import math

def f(x):
    return math.exp(-x) - math.cos(x)

a = 1
b = 4

fa = f(a)
fb = f(b)

c = (a + b)/2

n = 0

max_n = 10000

ep = 10**(-6)

print("\n Iteration: ", n, ", a: ", a, " b: ", b, ", c: ", c)
while b-c > ep and n < max_n:
    n = n+1
    fc = f(c)
    if fb*fc <= 0:
        a = c
        fa = fc
    else:
        b = c
        fb = fc

    c = (a+b)/2

    print("\n Iteration: ", n, ", a: ", a, " b: ", b, ", c: ", c)

