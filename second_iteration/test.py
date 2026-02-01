def factorial(x):
    total = 0
    if x == 1:
        return 1
    return factorial(x-1) * x



print(factorial(2))