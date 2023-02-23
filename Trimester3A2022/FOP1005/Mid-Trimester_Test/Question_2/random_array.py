import random
import numpy as np

A = np.array([random.randint(1, 5) for _ in range(19)])
B = np.array([random.randint(1, 5) for _ in range(19)])

C = A * B
D = A / B

min_A = A.min()
mean_A = A.mean()
min_B = B.min()
mean_B = B.mean()

print(f"Array A: {A}")
print(f"Array B: {B}")
print(f"Array C (A * B): {C}")
print(f"Array D (A / B): {D}")
print(f"Minimum of array A: {min_A}")
print(f"Mean of array A: {mean_A}")
print(f"Minimum of array B: {min_B}")
print(f"Mean of array B: {mean_B}")
