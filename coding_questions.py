# q1
# write a function to print "hello_username!"

def hello_name(user_name):
    """print a simple message of username"""
    print(f"hello_{user_name}!")

hello_name('USERNAME')




print('\n')



# q2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    """print out only odd number from 1-100"""
    for n in range(1, 101, 2):
        print(n)



first_odds()



# q3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
print('\n')
def max_num_in_list(a_list):
    """return the max number of a given list"""
    if not a_list:
        return None
    return max(a_list)

my_list = [1,2,3,4,5,6,7,8,9,10]
max_num = max_num_in_list(my_list)
print(max_num)



# q4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4,
#  but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """Return if a given year is a leap year."""
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

years_list = list(range(2020, 2025))

leap_years = [is_leap_year(year) for year in years_list]

print(leap_years)

# q5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5]
#  are not consecutive numbers. The return should be boolean Type

def is_consecutive(a_list):
    """Check to see if numbers are consecutive."""
    if not a_list or len(a_list) == 1:
        return True  # An empty list or a list with a single element is considered consecutive

    # Iterate through the list to check if each element is consecutive
    for i in range(len(a_list) - 1):
        if a_list[i] != a_list[i + 1] - 1:
            return False
    return True

# Example usage
consecutive_result = is_consecutive([2, 3, 4, 5, 6, 7])
print(consecutive_result)

non_consecutive_result = is_consecutive([1, 2, 4, 5])
print(non_consecutive_result)
