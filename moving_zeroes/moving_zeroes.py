'''
Input: a List of integers
Returns: a List of integers (with zeroes at end of list without switching order of numbers)
Need to iterate through loop
'''


def moving_zeroes(arr):
    # Your code here

    for i in range(len(arr))[::-1]:
        if arr[i] == 0:
            arr.pop(i)
            arr.append(0)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
