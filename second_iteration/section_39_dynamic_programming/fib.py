memo = [None] * 100



counter = 0



def fib(n):
    global counter
    counter += 1


    if memo[n] is not None:
        return memo[n]

    if n == 0 or n == 1:
        return n
    
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
n = 80
print("fib of:", n)
print(fib(n))
print("counter:", counter)
