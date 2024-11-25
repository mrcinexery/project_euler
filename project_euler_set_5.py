"""
Here is a gathering of the problems + solutions 21 - 25 of projecteuler.
To run individual functions without running docstring tests, paste
if __name__ == "__main__": and then the specific function to do so.
"""

import time
from datetime import timedelta
from string import ascii_lowercase

from audioop import reverse


# Amicable Numbers
# Problem 21
# Let d(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).
# If d(a) = b  and d(b) = a, where a != b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55 and 110;
# therefore d(220) = 284. The proper divisors of 284 1,2,4,71 and 142;
# so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

def amicable_numbers():
    """
    Finds and returns the sum of all amicable numbers below 10,000.

    Amicable numbers are two distinct numbers where the sum of the proper
    divisors (excluding the number itself) of one number is equal to the other,
    and vice versa.

    The function performs the following steps:
    1. Iterates through numbers from 1 to 10,000 to find their divisors and
        stores the sum of each number's divisors in a dictionary.
    2. Identifies pairs of numbers that are amicable by checking if the sum of
        divisors of one number matches the other and ensures the pair consists
        of distinct numbers.
    3. Collects all amicable numbers in a set and calculates the total sum.

    Returns:
        int: The sum of all amicable numbers below 10,000.
    """
    num_dict = dict()
    amicable_nums = set()
    for num in range(1, 10000):
        total = 0
        divisors = list()
        for i in range(1, int((num ** 0.5))+1):
            if num % i == 0:
                divisors.append(i)
                total += i
                if num / i != num:
                    divisors.append(int(num / i))
                    total += int(num / i)
        divisors.sort(reverse=False)
        num_dict[num] = total

    for key1 in num_dict:
       value1 = num_dict[key1]
       for key2 in num_dict:
           if key2 == value1:
               value2 = num_dict[key2]
               if key1 == value2 and key1 != key2:
                   amicable_nums.add(key1)
                   amicable_nums.add(key2)

    print(f'amicable_nums: {amicable_nums}')

    total_result = 0
    for x in amicable_nums:
        total_result += x

    return total_result
# -----------------------------------------------------------------------------

# Names Scores
# Problem 22
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a
# name score.
# For example, when the list is sorted into alphabetical order, COLIN, which
# is worth 3+15+12+9+14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 * 53 = 49714
# What is the total of all the name scores in the file?

def names_scores():
    """
    Calculates the total of all name scores from a file of names.

    The function reads a file containing names, sorts them alphabetically,
    and calculates a score for each name based on the sum of its letters'
    positions in the alphabet (A = 1, B = 2, ..., Z = 26).
    The name score is then calculated by multiplying the alphabetical position
    of the name in the sorted list with the name's letter score.

    The function performs the following steps:
    1. Reads the names from a text file, cleans and sorts them alphabetically.
    2. Defines a helper function `alphabet_name_score()` to calculate the sum
        of alphabetical positions for each name.
    3. Iterates through the sorted names, calculates the name score by
        multiplying its position in the list by its alphabetical score.
    4. Computes the total of all name scores.

    Returns:
        int: The total of all name scores from the list.
    """
    f = open('assets/0022_names.txt', 'r')
    content = f.read()
    f.close()
    names_list = [x[1:len(x)-1] for x in content.split(',')]
    names_list.sort(reverse=False)
    d = {v:k+1 for k,v in enumerate(ascii_lowercase)}

    def alphabet_name_score(name):
        total = 0
        for char in list(name.lower()):
            total += d[char]
        return total

    total_of_all_name_scores = 0
    for idx, name_in_list in enumerate(names_list):
        alpha_name_score = alphabet_name_score(name_in_list)
        name_score = (idx+1)*alpha_name_score
        total_of_all_name_scores += name_score

    return total_of_all_name_scores
# -----------------------------------------------------------------------------

# Non-Abundant Sums
# Problem 23
# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of 28
# would be 1+2+4+7+14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than
# n, and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1+2+3+4+6 = 16, the smallest number
# that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than
# 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even
# though it is known that the greatest number that cannot be expressed as the
# sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.

def non_abundant_sum():
    """
    Calculates the sum of all numbers that cannot be written as the sum of two
    abundant numbers up to a given upper limit (28,123 in this case).
    Abundant numbers are those whose proper divisors' sum exceeds the number
    itself.

    The function identifies all abundant numbers up to the upper limit,
    generates all possible sums of these numbers, and then subtracts these sums
    from the total set of numbers up to the upper limit.
    Finally, it returns the sum of the numbers that cannot be represented as the
    sum of two abundant numbers.
    """
    upper_limit = 28123
    compare_set = set([x for x in range(1,upper_limit+1)])

    def get_abundant_numbers(number):
        """
        Identifies all abundant numbers up to a given limit.

        An abundant number is a number whose proper divisors' sum exceeds the
        number itself.
        This function calculates the divisors for each number and returns a
        list of all numbers that are abundant.

        Args:
            number (int): The upper limit up to which abundant numbers are to
            be found.

        Returns:
            abundant_numbers (list): A list of abundant numbers up to the given
            limit.
        """
        abundant_numbers = []
        for num in range(1, number+1):
            temp_divisors = set()
            for x in range(1, int(num**0.5)+1):
                if num % x == 0:
                    temp_divisors.add(x)
                    if int(num/x) != num:
                        temp_divisors.add(int(num/x))
            if num < sum(temp_divisors):
                abundant_numbers.append(num)
        return abundant_numbers

    abundant_number_list = get_abundant_numbers(upper_limit)
    total_sum_set = set()

    for idx, num1 in enumerate(abundant_number_list):
        for num2 in abundant_number_list[idx:]:
            total = num1 + num2
            if total <= upper_limit and total not in total_sum_set:
                total_sum_set.add(total)
                i = 1
                while i < int(upper_limit**0.5)+1:
                    if total*i >= upper_limit:
                        break
                    if total * i not in total_sum_set:
                        total_sum_set.add(num1 * i)
                    i += 1

    result_set = compare_set.difference(total_sum_set)
    print(f'Result: {sum(result_set)}')
# -----------------------------------------------------------------------------

# Lexicographic Permutations
# Problem 24
# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order. The lexicographic permutations of 0, 1 and 2
# are: 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def lexicographic_permutations(nums):
    """
    Generates all lexicographic permutations of a given list of numbers and
    prints the millionth permutation.

    The function builds permutations iteratively by inserting each element of
    the input list into all possible positions of the existing permutations.
    It then sorts the list of permutations lexicographically and prints the
    total number of permutations as well as the millionth permutation
    (1-based index).

    Args:
        nums (list): A list of numbers for which lexicographic permutations are
        to be generated.

    Returns:
        perm_list (list): A list containing all lexicographically sorted
        permutations of the input list.
    """
    perm_list = [[]]

    for element in nums:
        perms = list()
        for p in perm_list:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, element)
                perms.append(p_copy)
        perm_list = perms
    perm_list.sort(reverse=False)
    print(f'No of Perms: {len(perm_list)}')
    print(f'millionth lexicographic permuation: {perm_list[999999]}')
    return perm_list


if __name__ == "__main__":
    start_time = time.perf_counter()
    #print(amicable_numbers())
    #print(names_scores())
    #non_abundant_sum()
    print(lexicographic_permutations([0, 1, 2, 3, 4, 5, 6,  7, 8 ,9]))
    duration = timedelta(seconds=time.perf_counter()-start_time)
    print('Job took: ', duration)
