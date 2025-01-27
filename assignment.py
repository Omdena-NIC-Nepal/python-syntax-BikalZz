def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    string = f"My name is {name} and I am {age} years old"
    return string

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    result = ""
    if number == 10:
        result = "Equal"
    elif number > 10:
        result = "Greater"
    elif number < 10:
        result = "Lesser"
    return result

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    summation = 0
    for i in range(1,n+1):
        summation += i
    return summation

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    if numbers:
        sum_of_numbers = sum(numbers)
        max_in_numbers = max(numbers)
        min_in_numbers = min(numbers)
    else:
        print("The list is empty.")
    tuple_of_numbers = (sum_of_numbers, max_in_numbers, min_in_numbers)
    return tuple_of_numbers

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    name_list = []
    for key, value in students_dict.items():
        if value > 80:
            name_list.append(key)
    return name_list

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    set1 = set(list1)
    set2 = set(list2)
    return set1 & set2

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    dictionary_arithmetic ={}
    dictionary_arithmetic["sum"] = a + b
    dictionary_arithmetic["difference"] = a - b
    dictionary_arithmetic["product"] = a * b
    try:
        dictionary_arithmetic["quotient"] = a / b
    except ZeroDivisionError:
        dictionary_arithmetic["quotient"] = "Cannot divide by zero."
    return dictionary_arithmetic

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    dictionary_logical = {}
    dictionary_logical["and"] = x and y
    dictionary_logical["or"] = x or y
    dictionary_logical["not_x"] = not x
    return dictionary_logical

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    dictionary_bitwise = {}
    dictionary_bitwise["and"] = a & b
    dictionary_bitwise["or"] = a | b
    dictionary_bitwise["xor"] = a ^ b
    return dictionary_bitwise