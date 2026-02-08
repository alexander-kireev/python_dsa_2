



# counter = 0

# def fact(n):
#     global counter
#     counter += 1
#     if n == 1:
#         return 1
    
#     return n * fact(n - 1)


# n = 500
# print("factorial of", n, "is", fact(n))
# print("number of functional calls:", counter)


memo = [None] * 10000

counter = 0
def fib_3(n):
    global counter
    counter += 1

    if memo[n] is not None:
        return memo[n]

    if n < 3:
        return 1
    
    memo[n] = fib_3(n - 1) + fib_3(n - 2) + fib_3(n - 3)
    return memo[n]

print(fib_3(99))
print(counter)