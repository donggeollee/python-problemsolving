
def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num-1) + fibonacci(num-2)

print(fibonacci(50))

def fibonacci_dp(num):
    cache = [0 for i in range(num+1)]
    cache[0], cache[1] = 0,1 
    for i in range(2, num+1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[num]

print(fibonacci_dp(10))

memo = [None for i in range(100)] # 숫자에 따라 값을 memoization 할 때  
# memo = dict() # 문자에 따라 값을 memoization 할 때 
def fibonacci_memo(n):
    if n == 0:
        return 0
    if n == 1 :
        return 1
    if memo[n] :
        return memo[n]
    memo[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    return memo[n]

print(fibonacci_memo(10))