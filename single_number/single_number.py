'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here
    # need to pull out integer that is not a duplicate from list
    # will need to iterate through list somehow and pull out item that only shows up once
    # we can use set to provide us with all unique elements

    return 2 * sum(set(arr)) - sum(arr)


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
