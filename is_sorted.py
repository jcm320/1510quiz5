def is_sorted(integer_list):

    """
    Check if the integer_list is non-decreasing sorted.

    A function that checks if the integer_list is sorted in non-decreasing order,

    :param integer_list:
    :return:

    >>>integer_list = [1,2,3]
    True
    >>>integer_list = [3,2,1]
    False
    >>>integer_list = []
    True
    >>>integer_list = [4,6,5,9,4,8]
    False
    """
    another_list = sorted(integer_list)

    if integer_list == another_list:
        return True
    else:
        return False

def main():

if __name__ == "__main__":
    main()
