import math

def f(x):
    return math.exp(-x) - math.cos(x)

def f_prime(x):
    return (-1*math.exp(-x) + math.sin(x))

x0 = 3

n = 0

max_n = 10000

ep = 10**(-6)

error = 1

while abs(error) > ep and n <= max_n:
    print("\n Iteration: ", n, "xn: ", x0, ", Error: ", error)
    fx = f(x0)
    dfx = f_prime(x0)

    if(dfx == 0):
        print("The derivative is 0.")
        break

    x1 = x0 - fx/dfx

    error = x1 - x0

    x0 = x1

    n = n+1