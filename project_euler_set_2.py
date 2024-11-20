"""
Here is a gathering of the problems + solutions 6 - 10 of projecteuler.
To run individual functions without running docstring tests, paste
if __name__ == "__main__": and then the specific function to do so.
"""

# Sum Square Difference
# Problem 6
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 =  385.
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025.
# Hence, the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

def sum_of_squares(num):
    """
    Calculate the difference between the square of the sum and
    the sum of the squares of the first 'num' natural numbers.

    The function computes:
    - The sum of the squares of the first 'num' natural numbers.
    - The square of the sum of the first 'num' natural numbers.
    It then returns the difference between the square of the sum and
    the sum of the squares.

    Args:
        num (int): The number of natural numbers to consider.

    Returns:
        None: The function prints the intermediate results, including:
              - The sum of the squares.
              - The sum of the numbers.
              - The square of the sum.
              - The final result (difference between the square of the sum
                and the sum of the squares).

    Example:
        >>> sum_of_squares(10)
        sum: 385
        sum2: 55
        sum_square: 3025
        result: 2640
    """

    sum = 0
    sum2 = 0
    for i in range(1, num+1):
        sum += i ** 2
        sum2 += i
    print(f'sum: {sum}')

    sum_square = sum2 ** 2
    print(f'sum2: {sum2}')
    print(f'sum_square: {sum_square}')

    result = sum_square - sum
    print(f'result: {result}')
# -----------------------------------------------------------------------------

# 10001st Prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
# What is the 10001st prime number?

def get_primes(num):
    """
    Generate all prime numbers up to a given limit using the
    Sieve of Eratosthenes.

    This function removes multiples of each prime, starting from 3,
    and keeps only the numbers that are prime.
    It handles odd numbers only (besides 2) for efficiency.

    Args:
        num (int): The upper limit for generating primes.

    Returns:
        set: A set of prime numbers up to the given limit.
    """

    # remove even numbers but 2
    primes = {x for x in range(3, num, 2)}
    primes.add(2)  # Include 2, which is the only even prime

    print(f'Number of potential primes: {len(primes)}')

    if num <= 1:
        print(f'{num} is not a prime!')
    else:
        for i in range(3,(int(num ** 0.5))+1,2):
            if i in primes:
                print(f'i: {i}')

                # remove the multiples of i
                j = i
                while i * j <= num:
                    multiple = i * j
                    print(f'j: {j}')
                    print(f'multiple: {multiple}')
                    if multiple in primes:
                        primes.remove(multiple)
                    j += 1

    print(f'Number of primes: {len(primes)}')
    my_primes = list(primes)
    my_primes.sort(reverse=False)
   # return my_primes[10000]
    return my_primes
# -----------------------------------------------------------------------------

# Largest Produkt in a Series
# Problem 8
# The four adjacent digits in the 1000-digit number that have the greatest
# product are 9 * 9 * 8 * 9= 5832.
# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450
# Find the thirteen adjacent digits in the 1000-digit number
# that have the greatest product. What is the value of this product?

def largest_product_in_series(series):
    """
    Finds the largest product of 'series' consecutive digits
    in a predefined large number.

    The function iterates over all possible consecutive substrings of length
    'series' within the given large number. For each substring, it calculates
    the product of the digits and keeps track of the maximum product found.

    Args:
        series (int): The length of consecutive digits for which the product
        is to be calculated.

    Returns:
        int: The maximum product of 'series' consecutive digits.

    Example:
        >>> largest_product_in_series(4)
        j: 7
        j: 3
        j: 1
        j: 6
        result: 126
        ...
        5832
    """
    max_value = 0
    num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    num_str = str(num)
    for i in range(len(num_str)+1-series):
        substring = num_str[i:series+i]

        result = 1
        for j in substring:
            print(f'j: {j}')
            result *= int(j)
        print(f'result: {result}')
        max_value = max(max_value, result)

        if i == len(num_str)-series:
            return max_value
# -----------------------------------------------------------------------------

# Special Pythagorean Triplet
# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 * b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc

def special_pythagorean_triplet():
    """
     Finds the special Pythagorean triplet (a, b, c) such that:
     - a^2 + b^2 = c^2 (Pythagorean theorem)
     - a + b + c = 1000

     The function iterates over all possible values of a, b, and c
     where a < b < c, checks if they form a Pythagorean triplet,
     and if their sum equals 1000.
     Once such a triplet is found, it calculates the product a * b * c
     and returns it.

     Returns:
         str: A string containing the Pythagorean triplet and the product
         of a, b, and c.

     Example:
         >>> special_pythagorean_triplet()
         'The product abc is 31875000'
     """
    for a in range(1, 1000):
        for b in range(1,1000):
            for c in range(1,1000):
                if a < b < c:
                    if a**2 + b**2 == c**2:
                        if  a + b + c == 1000:
                            print(f'a: {a}, b: {b}, c: {c}')
                            result = a * b * c
                            return f'The product abc is {result}'
# -----------------------------------------------------------------------------

# Summation of Primes
# Problem 10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17 .
# Find the sum of all the primes below two million.

def summation_of_primes():
    """
    Calculates the summation of all prime numbers below 2,000,000.

    The function first generates a list of prime numbers below 2,000,000
    using the `get_primes` function.
    It then sums these primes and returns the result.

    Returns:
        int: The sum of all prime numbers below 2,000,000.

    Example:
        >>> summation_of_primes()
        142913828922
    """
    primes = get_primes(2000000)
    result = 0
    for prime in primes:
        print(f'prime: {prime}')
        result += prime
    return result


if __name__ == "__main__":
    # sum_of_squares(100)
    #print(get_primes(150000))
    #print(largest_product_in_series(13))
    #print(special_pythagorean_triplet())
    #print(summation_of_primes())
    pass