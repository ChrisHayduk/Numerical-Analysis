import numpy as np


# Simpson function definition
# Takes in a function f and a number m representing the number of intervals
def Simpson(f, m):
   # Initialize h
    h = (1 - (0)) / m

    # Initialize integral value
    integral = 0.0

    # Create list of points to evalue function at
    x = []

    for i in range(m + 1):
        x.append(0 + i * h)

    # Run Simpson's rule algorithm
    for i in range(len(x)):
        if i == 0 or i == len(x) - 1:
            integral += f(x[i])
        elif i % 2 == 0:
            integral += 2 * f(x[i])
        else:
            integral += 4 * f(x[i])

    integral = integral * (h / 3)

    return (integral)


print(Simpson(lambda x: np.exp(-(x)**2), 51))