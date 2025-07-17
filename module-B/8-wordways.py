#!/usr/bin/python3
def logger(func):
    def wrapper(s, word_dict):
        result = func(s, word_dict)
        print(f"Function {func.__name__} called with s='{s}', word_dict={word_dict}, result={result}")
        return result
    return wrapper


@logger
def word_break(s, word_dict):
    word_set = set(word_dict)  # for faster lookup
    n = len(s)

    # dp[i] means: can s[:i] be segmented into words from word_dict?
    dp = [False] * (n + 1)
    dp[0] = True  # empty string is always valid

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]

print(word_break("haywhy", ["hay", "why"])) 
print(word_break("applepenapple", ["apple", "pen"])) 
print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))  
