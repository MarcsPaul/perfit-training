import math
num = int(input("Enter a number"))
np = []
isprime = []
for i in range(num + 1, num + 200):
    np.append(i)
for j in np:
    is_prime = True
    for x in range(2, j - 1):
        if j % x == 0:
            is_prime = False
            break
    if is_prime:
        isprime.append(j)
print(min(isprime))