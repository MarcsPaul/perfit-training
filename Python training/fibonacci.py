# n1 = 0
# n2 = 1
# lim = int(input("enter the limit for the series"))
# count = 0
# while count < lim:
#     print(n1)
#     n = n2 + n1
#     n1 = n2
#     n2 = n
#     count += 1

lim = int(input("Enter the limit"))
f1 = 0
f2 = 1
print(f1, f2, end=" ")
for i in range(1, lim-1):
    fib = f1+f2
    f1 = f2
    f2 = fib
    print(fib, end=" ")