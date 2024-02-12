import numpy as np
import math

################################################
###             Fancy Math Stuff             ###
################################################

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


""" Prime Factorization
    - returns a List of all Prime Factors
"""
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


# is Prime in O(sqrt(n))
def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i) == 0:
            return False
    return True


################################################
###                Debugging                 ###
################################################

""" simple ProgressBar
    - dont forget to call print() after using the Bar
"""
def progressBar(done, total, length = 50):
    percent = (done / total) * 100
    filled_length = int(length * done // total)
    bar = '=' * filled_length + ' ' * (length - filled_length)
    print(f"\r[{bar}] {percent:.2f}%", end = "")


################################################
###              Numpy Stuff                 ###
################################################
    
# parse input strings into numpy Matrix
def np_lines2Matrix(lines):
    matrix = np.zeros((len(lines), len(lines[0])-1), dtype = int)
    for y, line in enumerate(lines):
        for x, char in enumerate(line[:-1]):
            matrix[y][x] = int(char)
    return matrix

# prints full Matrix without spaces
def np_fullPrint(matrix):
    for row in matrix:
        for num in row:
            print(num if num >= 0 else " ", end = "")
        print()