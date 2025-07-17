#!/usr/bin/python3
def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} called with args={args}, kwargs={kwargs}, result={result}")
        return result
    return wrapper


@logger
def coin_change(coins, amount):
    # DP array to store minimum coins for each amount
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins to make amount 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1



print(coin_change([1, 2, 5], 11))
