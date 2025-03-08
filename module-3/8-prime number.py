
#/usr/bin/python3
def is_prime(n):
    # Check if the number is less than 2
    if n < 2:
        return False
    # Check for factors other than 1 and n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_factors(n):
    # Find and return the factors of a number
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

# Loop through numbers from 1 to 50
for num in range(1, 51):
    if is_prime(num):
        print(f"{num} is prime and has no factors other than 1 and itself.")
    else:
        factors = find_factors(num)
        print(f"{num} is not prime and its factors are: {factors}")
