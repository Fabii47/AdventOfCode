import math

def least_common_multiple(numbers):
    # get Primes
    primes = [prime_factorization(x) for x in numbers]
    prim_dir = {}
    
    # put Primes in Dictionary
        # key is prime, item is amount
    for list in primes:
        for p in list:
            try:
                prim_dir[p] = max(prim_dir[p], list.count(p))
            except KeyError:
                prim_dir[p] = list.count(p)
    
    # multiplie max amount of primes
    product = 1
    for key, item in prim_dir.items():
        product *= int(math.pow(key, item))

    return product
    
def prime_factorization(num : int):
    if num <= 1:
        return 1

    primes = []
    
    while not is_prime(num):
        for i in range(2, num):
            if not is_prime(i):
                continue
            if num % i == 0:
                primes.append(i)
                num //= i
                break
        
    primes.append(num)
    return primes

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i) == 0:
            return False
    return True