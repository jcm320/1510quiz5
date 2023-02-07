def is_sorted(integer_list):

    """
    Check if the integer_list is non-decreasing sorted.

    A function that checks if the integer_list is sorted in non-decreasing order.

    :param integer_list: a list of integers.
    :pre-condition: a list of integers that is in non-deceasing order (possibly-empty).
    :post-condition: define the non-decreasing sorted list correctly, and check on integer_list.

    :return: A boolean value displaying True if integer_list is sorted in non-decreasing order, and False if not.

    >>> is_sorted([1,2,3])
    True
    >>> is_sorted([3,2,1])
    False
    >>> is_sorted([])
    True
    >>> is_sorted([9,1,-3,7,4,3,7])
    False
    >>> is_sorted([-4,-2,-1,3,3,4,4,4,7,8])
    True

    """
    another_list = sorted(integer_list)
    if integer_list == another_list:
        return True
    else:
        return False





