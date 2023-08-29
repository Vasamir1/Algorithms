"""
Simple Binary Search with recursion
"""
import sys


def binary_search(arr, n, start, end):

    #  Find middle
    mid = (start + end) // 2
    
    #  Check if the list is empty...
    if arr == []:
        sys.exit("The array is empty.")
    else:
        try:
            #  ...if not check if we found our number in the middle
            if arr[mid] == n:
                return mid
            #   If not check if our number is bigger than the one in the middle...
            elif n > arr[mid]:
                return binary_search(arr, n, mid+1, end)
            #  ...or if smaller than middle
            elif n < arr[mid]:
                return binary_search(arr, n, start, mid-1)
            #  If we did not type number to search exit with message
        except TypeError:
            sys.exit("You can only search numbers.")

    return mid


test_example = [123, 323, 111, 213, 7, 8, 76655, 23, 9, 1, 313, 47, 82, 2, 1119, 666, 909, 89222, 143, 28]
guess = 666

#  Sort the array. Remember: binary search works with sorted arrays
test_example = sorted(test_example)

#  Storing function in variable
guess_index = binary_search(test_example, guess, 0, len(test_example)-1)

# Printing result. Remember, you can always check results of function with "assert"
print(f"The number {guess} is on the index number {guess_index}.")
