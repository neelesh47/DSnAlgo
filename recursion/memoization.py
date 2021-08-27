factorial_memo = {}

def factorial(k):
    if k == 0:
        return 1
    if k not in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)
    return factorial_memo[k]


print(factorial(4))