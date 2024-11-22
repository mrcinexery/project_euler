"""
Here is a gathering of the problems + solutions 16 - 20 of projecteuler.
To run individual functions without running docstring tests, paste
if __name__ == "__main__": and then the specific function to do so.
"""

import time
from datetime import timedelta

# Power Digit Sum
# Problem 16
# 2^15 = 32768 and the sum of its digits is 3+2+7+6+8=26.
# What is the sum of the digits of the number 2^1000?

def power_digit_sum(power):
    """
    Calculate the sum of the digits of the number 2 raised to the given power.

    Args:
        power (int): The exponent to raise 2 to.

    Returns:
        int: The sum of the digits of the number 2 ** power.

    Example:
        power_digit_sum(15) would calculate 2**15 = 32768,
        and return the sum of the digits: 3 + 2 + 7 + 6 + 8 = 26.
    """
    num = 2 ** power
    result = 0
    for x in str(num):
        result += int(x)
    return result
# -----------------------------------------------------------------------------

# Number Letter Counts
# Problem 17
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3+3+5+4+4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342
# (three hundred and forty-two) contains 23 letters and 115
# (one hundred and fifteen) contains 20 letters. The use of "and" when writing
# out numbers is in compliance with British usage.

def number_letter_counts():
    """
    Calculate the total number of letters used when writing out the numbers
    from 1 to 1000 (in English) without spaces or hyphens.

    The function follows these steps:
    1. It counts the letters for numbers from 1 to 9.
    2. It counts the letters for numbers from 10 to 19.
    3. It counts the letters for numbers from 20 to 99,
        including combinations like "twenty-one".
    4. It counts the letters for numbers from 100 to 999,
        including combinations like "one hundred and twenty".
    5. It counts the letters for numbers from 100 to 999 with specific cases
        for "hundred and" and numbers like "eleven".
    6. It counts "one thousand" separately.

    Prints the numbers being counted and the intermediate results.

    The result is the total number of letters used to write out all the numbers
    from 1 to 1000 in words.

    Returns:
        None. The function prints the final result.
    Hints:
        use python-module inflect to optimize code
    """

    under10 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
                'nine']
    under20 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
               'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    under100 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
                'eighty', 'ninety']
    under1000 = ['hundred']

    result = 0

    # one to nine
    for a in under10:
        print(a)
        result += len(a)

    print(f'result: {result}')

    # ten to nineteen
    for a in under20:
        print(a)
        result += len(a)

    print(f'result: {result}')

    # twenty to ninety-nine
    for b in under100:
        for c in under10:
            if c == 'one':
                print(f'{b}')
                result += len(b)
                print(f'{b}-{c}')
                result += len(b)
                result += len(c)
            else:
                print(f'{b}-{c}')
                result += len(b)
                result += len(c)

    print(f'result: {result}')

    # one hundred twenty to nine hundred ninety-nine
    for a in under10:
        for b in under1000:
            for c in under100:
                for d in under10:
                    if d == 'one':
                        print(f'{a} {b} and {c}')
                        result += len(a)
                        result += len(b)
                        result += len(c)
                        print(f'{a} {b} and {c}-{d}')
                        result += len(a)
                        result += len(b)
                        result += len(c)
                        result += len(d)
                        result += 6 # 2x 'and'
                    else:
                        print(f'{a} {b} and {c}-{d}')
                        result += len(a)
                        result += len(b)
                        result += len(c)
                        result += len(d)
                        result += 3 # 1x 'and'

    # one hundred ten, eleven, twelve, two hundred ten, elven, ...
    for a in under10:
        for b in under1000:
            for c in under20:
                print(f'{a} {b} and {c}')
                result += len(a)
                result += len(b)
                result += len(c)
                result += 3  # 1x 'and'


    print(f'result: {result}')
    # one hundred one - nine, two hundred one - nine, ...
    for a in under10:
        for b in under1000:
            for c in under10:
                print(f'{a} {b} and {c}')
                result += len(a)
                result += len(b)
                result += len(c)
                result += 3  # 1x 'and'

    # one hundred, two hundred, three hundred, ...
    for a in under10:
        for b in under1000:
            print(f'{a} {b}')
            result += len(a)
            result += len(b)

    result += len('one')
    result += len('thousand')

    print(f'result: {result}')
# -----------------------------------------------------------------------------

# Maximum Path Sum I
# Problem 18
# By starting at the top of the triangle below and moving to adjacent numbers
# on the row below, the maximum total from top to bottom is 23.
#           3
#          7 4
#         2 4 6
#        8 5 9 3
# That is, 3+7+4+9 = 23
# Find the maximum total from top to bottom of the triangle below:
#               75
#              95 64
#             17 47 82
#            18 35 87 10
#           20 04 82 47 65
#          19 01 23 75 03 34
#         88 02 77 73 07 63 67
#        99 65 04 28 06 16 70 92
#       41 41 26 56 83 40 80 70 33
#      41 48 72 33 47 32 37 16 94 29
#     53 71 44 65 25 43 91 52 97 51 14
#    70 11 33 28 77 73 17 78 39 68 17 57
#   91 71 52 38 17 14 91 43 58 50 27 29 48
#  63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by
# trying every route. However, Problem 67, is the same challenge with a triangle
# containing one-hundred rows; it cannot be solved by brute force,
# and requires a clever method! ;o)

def maximum_path_sum_I():
    """
        Calculates the maximum path sum from top to bottom of a triangle
        using dynamic programming.

        The triangle is represented as a list of lists, where each inner list
        corresponds to a row in the triangle.
        The function starts from the second-to-last row and works its way
        upwards, replacing each element with the sum of itself and the maximum
        of the two adjacent numbers in the row below.

        This approach ensures that by the time it reaches the top of the
        triangle, the element at the top will contain the maximum possible sum
        from top to bottom.

        Returns:
            str: The maximum path sum as a string.

        Example:
            For the following triangle:
                   3
                  7 4
                 2 4 6
                8 5 9 3
            The function will return '23' because 3 + 7 + 4 + 9 = 23.
        """
    triangle = [
        ['75'],
        ['95', '64'],
        ['17', '47', '82'],
        ['18', '35', '87', '10'],
        ['20', '04', '82', '47', '65'],
        ['19', '01', '23', '75', '03', '34'],
        ['88', '02', '77', '73', '07', '63', '67'],
        ['99', '65', '04', '28', '06', '16', '70', '92'],
        ['41', '41', '26', '56', '83', '40', '80', '70', '33'],
        ['41', '48', '72', '33', '47', '32', '37', '16', '94', '29'],
        ['53', '71', '44', '65', '25', '43', '91', '52', '97', '51', '14'],
        ['70', '11', '33', '28', '77', '73', '17', '78', '39', '68', '17',
         '57'],
        ['91', '71', '52', '38', '17', '14', '91', '43', '58', '50', '27', '29',
         '48'],
        ['63', '66', '04', '68', '89', '53', '67', '30', '73', '16', '69', '87',
         '40', '31'],
        ['04', '62', '98', '27', '23', '09', '70', '98', '73', '93', '38', '53',
         '60', '04', '23']
    ]

    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):

            triangle[row][col] = str(int(triangle[row][col]) + max(int(triangle[row + 1][col]), int(triangle[row + 1][col + 1])))
            print(
                f'max: {max(int(triangle[row + 1][col]), int(triangle[row + 1][col + 1]))}')

    return triangle[0][0]
# -----------------------------------------------------------------------------

# Counting Sundays
# Problem 19
# You are given the following information,
# but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September, April, June and November.
# All the rest have thirty-one, Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century
# unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?

def counting_sundays(first_weekday, year_from, year_to):
    """
    Counts how many Sundays fall on the first day of the month within a given
    year range.

    The function takes the day of the week for 1.Jan 1900, the starting year,
    and the ending year, and iterates through each month and year.
    It calculates the number of days in each month, taking leap years into
    account, and checks if the first day of each month is a Sunday.
    If so, it increments a counter.

    Leap years are determined by the rule:
    - A year is a leap year if it is divisible by 4,
    - However, years divisible by 100 are not leap years unless they are
    divisible by 400.

    Parameters:
        first_weekday (str): The weekday of the first day of the starting year
        (e.g., "Monday").
        year_from (int): The starting year of the range.
        year_to (int): The ending year of the range (exclusive).

    Returns:
        int: The total number of Sundays that fall on the first day of the
        month between the years `year_from` and `year_to`.

    Example:
        counting_sundays('Monday', 1901, 2001) will return the number of
        Sundays that fell on the first day of the month during the 20th century.

    Notes:
        - The function prints each day's weekday and date as it processes the
            calendar.
        - It assumes that the `first_weekday` parameter corresponds to the
            first day of January of `year_from`.
    """
    overview_month = {'1':('Jan', 31), '2':('Feb', 28), '3':('Mar', 31),
                  '4':('Apr', 30), '5':('May', 31), '6':('Jun', 30),
                  '7':('Jul', 31), '8':('Aug', 31), '9':('Sep',30),
                  '10':('Oct', 31), '11':('Nov', 30), '12':('Dec', 31)}

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                'Saturday', 'Sunday']

    index_weekday = weekdays.index(first_weekday)
    years_range = [x for x in range(year_from, year_to)]
    counter_sundays_first_month = 0

    for year in years_range:
        for month in range(1, 13):
            no_of_days = 0
            if (month == 2 and year % 4 == 0 and
                    ((not year % 100 == 0) or year % 400 == 0)):
                    no_of_days = 29
            else:
                no_of_days = overview_month[str(month)][1]
            for day in range(1, no_of_days+1):
                print(f'{weekdays[index_weekday]}'
                      f' - {day}.{overview_month[str(month)][0]} {year}')
                if (day == 1 and weekdays[index_weekday] == 'Sunday'
                        and year >= 1901):
                    counter_sundays_first_month += 1

                index_weekday += 1
                if index_weekday >= len(weekdays):
                    index_weekday = 0
    return counter_sundays_first_month
# -----------------------------------------------------------------------------

# Factorial Digit Sum
# Problem 20
# !n means n * (n-1) * ... * 3 * 2 * 1.
# For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
# and the sum of the digits in the number 10! is 3+6+2+8+8+0+0 = 27.
# Find the sum of the digits in the number 100!.

def factorial_digit_sum(num):
    """
        Calculates the sum of the digits of the factorial of a given number.

        The function first computes the factorial of the input number `num`,
        then sums the individual digits of the resulting factorial.

        Parameters:
            num (int): The number for which the factorial is to be calculated.

        Returns:
            None: The function prints the factorial and the sum of its digits,
            but does not return any value.

        Example:
            factorial_digit_sum(10) would compute 10! = 3628800 and return the
            sum of its digits, 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
    """
    factorial_digit = 1
    result = 0
    for x in range(num, 1, -1):
        factorial_digit *= x
    print(f'factorial_digit: {factorial_digit}')

    for x in str(factorial_digit):
        result += int(x)

    print(f'factorial_digit_sum: {result}')


if __name__ == "__main__":
    start_time = time.perf_counter()
    # print(power_digit_sum(1000))
    # number_letter_counts()
    #print(maximum_path_sum_I())
    #print(counting_sundays('Monday', 1900, 2001))
    factorial_digit_sum(100)
    duration = timedelta(seconds=time.perf_counter()-start_time)
    print('Job took: ', duration)
    pass