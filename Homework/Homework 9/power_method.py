import numpy as np

n = 3

index = -1

err_tol = 10^(-8)

max_iters = 10^(5)

A = np.array([[2.0, 3.0, 4.0],
     [7.0, -1.0, 3.0],
     [1.0, -1.0, 5.0]])

x0 = np.random.rand(n, 1)

lam = np.zeros(max_iters)


max_x = max(abs(x0))

z = x0/max_x

print(z)

if index == -1:
     spec_vec = np.random.rand(n,1)

error = 1000

it_count = 0

while abs(error) > err_tol and it_count < max_iters:
     w = np.dot(A, z)

     max_w = max(abs(w))

     if index == -1:
          lam[it_count] = (spec_vec.transpose() @ w)/(spec_vec.transpose() @ z)

     else:
          lam[it_count] = w[index]/z[index]

     if it_count > 0:
          error = lam[it_count] - lam[it_count - 1]

     z = w/max_w
     final_lambda = lam[it_count]

     it_count += 1

print(z)
print(final_lambda)

print(np.dot(final_lambda, z))

print(np.dot(A, z))