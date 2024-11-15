"""
Here is a gathering of the problems + solutions 1 - 5 of projecteuler.
"""

import time
from datetime import timedelta

# Multiples of 3 or 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def multiples_of_3_or_5(num):
    """
    Calculate the sum of all multiples of 3 or 5 that are less than a given
    number.

    This function iterates through all numbers from 0 up to (but not including)
    the given number and checks if each number is divisible by 3 or 5.
    It collects these multiples in a list and then computes their sum.

    Args:
        num (int): The upper limit (exclusive) for finding multiples of 3 or 5.

    Returns:
        int: The sum of all multiples of 3 or 5 below the given number.

    Example:
        >>> multiples_of_3_or_5(10)
        23  # The multiples of 3 or 5 below 10 are 3, 5, 6, and 9,
              and their sum is 23.

        >>> multiples_of_3_or_5(1000)
        233168  # The sum of all multiples of 3 or 5 below 1000.
    """
    multiples3or5 = []
    result = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            multiples3or5.append(i)

    for num in multiples3or5:
        result += num

    return result

#print(multiples_of_3_or_5(1000))
# -----------------------------------------------------------------------------

# Even Fibonacci Numbers
# Problem 2
# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

def even_fibonacci_numbers():
    """
    Calculate the sum of all even Fibonacci numbers that do not exceed
    4,000,000.

    This function generates Fibonacci numbers recursivly, stopping once a
    Fibonacci number exceeds 4,000,000.
    It then sums only the even-valued Fibonacci numbers from the sequence.

    Returns:
        int: The sum of all even Fibonacci numbers that are less than or equal
             to 4,000,000.

    Example:
        >>> even_fibonacci_numbers()
        4613732  # The sum of all even Fibonacci numbers below 4,000,000
    """
    result = 0

    def get_next_fibonacci(num):
        """
        Recursively calculate the Fibonacci number at the given position in the
        sequence.

        Args:
            num (int): The position of the Fibonacci number in the sequence.

        Returns:
            int: The Fibonacci number at the specified position.
        """
        if num == 1: return 1
        elif num == 2: return 2
        else:
            return get_next_fibonacci(num-1) + get_next_fibonacci(num-2)

    fib_arr = list()
    i = 1
    while True:
        fib = get_next_fibonacci(i)
        fib_arr.append(fib)
        i += 1
        if fib >= 4000000:
            break

    for num in fib_arr:
        if num % 2 == 0:
            result += num

    return result


#print(even_fibonacci_numbers())
# -----------------------------------------------------------------------------

# Largest Prime Factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600.851.475.143?

def largest_prime_factor(num):
    """
    Find the largest prime factor of a given number using the
    Sieve of Eratosthenes to generate primes.

    This function first generates all prime numbers up to the square root of
    the input number using a modified Sieve of Eratosthenes.
    Then, it checks which of these primes divide the input number and collects
    them as prime factors. The largest of these prime factors is
    effectively the largest prime factor of the number.

    Args:
        num (int): The upper limit for generating primes, typically set to the
                    square root of the number for which prime factors are
                    being found.

    Returns:
        None: The function prints the list of prime factors of the given number.

    Example:
        >>> largest_prime_factor(13195)
        [5, 7, 13, 29]  # Prime factors of 13195, the largest is 29

        >>> largest_prime_factor(600851475143)
        [71, 839, 1471, 6857]  # Prime factors of 600851475143, the largest is 6857
    """

    # Identify primes with sieve of eratosthenes
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
        return primes

    my_primes = list(get_primes(num))
    prime_factors = []
    number = 600851475143
    k = 0
    while k < len(my_primes):
        print(f'num: {num}')
        print(f'k: {k}')
        if number % my_primes[k] == 0:
            print(f'num: {number}')
            print(f'my_primes[k]: {my_primes[k]}')
            number = number / my_primes[k]
            prime_factors.append(my_primes[k])

        k += 1

    print(prime_factors)

#start_time = time.perf_counter()
#largest_prime_factor(600851475143)
#largest_prime_factor(800000)
#duration = timedelta(seconds=time.perf_counter()-start_time)
#print('Job took: ', duration)
# -----------------------------------------------------------------------------

# Largest Palindrome Product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def largest_palindrome_product(num):
    """
    Find the largest palindrome that is a product of two numbers with `num`
    digits.

    This function calculates the product of two numbers, each with up to `num`
    digits, and checks if the product is a palindrome.
    It keeps track of the largest palindrome found and the corresponding
    factors that produce it.

    Args:
        num (int): The number of digits of the factors whose product is checked
        for being a palindrome.

    Returns:
        None: The function prints the largest palindrome product and its
        factors.

    Example:
        >>> largest_palindrome_product(2)
        max_i: 91
        max_j: 99
        max_value: 9009  # 9009 is the largest palindrome product of two
        2-digit numbers

        >>> largest_palindrome_product(3)
        max_i: 913
        max_j: 993
        max_value: 906609  # 906609 is the largest palindrome product of two
        3-digit numbers
    """

    def is_palindromic_number(num):
        """
        Check if a number is palindromic by comparing the first half of the
        number with the reversed second half.

        Args:
            num (int): The number to check.

        Returns:
            bool: True if the number is a palindrome, False otherwise.
        """
        if len(str(num)) % 2 != 0:
            return False
        num_str = str(num)
        num_rev = str(num)[::-1]
        return num_str[:int(len(num_str) / 2)] == num_rev[
                                                  :int(len(num_str) / 2)]

    i = 10
    max_value = 0
    max_i = 0
    max_j = 0
    while len(str(i)) <= num:
        #print(f'i: {i}')
        j = 10
        while len(str(j)) <= num:
            product = i * j
            if is_palindromic_number(product):

                if product > max_value:
                    max_value = product
                    max_i = i
                    max_j = j
            j += 1
        i += 1
    print(f'max_i: {max_i}')
    print(f'max_j: {max_j}')
    print(f'max_value: {max_value}')

#largest_palindrome_product(3)
# -----------------------------------------------------------------------------

# Smallest Multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

def smallest_multiple(range_int):
    """
    Find the smallest positive number that is evenly divisible by all of the
    numbers from 1 to `range_int`.

    This function iteratively checks numbers, starting from 2, and tests if
    each number is divisible by all integers from 2 to `range_int`.
    It increments the number until it finds one that meets
    the condition of being divisible by all integers in the specified range.

    Args:
        range_int (int): The upper limit of the range of divisors
        (starting from 2).

    Returns:
        int: The smallest number that is evenly divisible by all numbers from 1
        to `range_int`.

    Example:
        >>> smallest_multiple(10)
        2520  # The smallest number divisible by all numbers from 1 to 10

        >>> smallest_multiple(20)
        232792560  # The smallest number divisible by all numbers from 1 to 20
    """
    smallest_number = 2
    smallest_number_found = False

    while not smallest_number_found:
        i = 2
        while i <= range_int:
            if smallest_number % i == 0:
                i += 1
            else:
                smallest_number += 1
                break

            if i == range_int:
                print(f'smallest_number: {smallest_number}')
                smallest_number_found = True
                break

    return smallest_number

# print(smallest_multiple(20))
# -----------------------------------------------------------------------------
