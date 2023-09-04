"""
Merge Sort algorithm
"""


def merge_sort(array):
    #  First lets store length of given array
    length_of_array = len(array)
    #  Then find the middle of array
    mid = length_of_array // 2

    #  If list has one or fewer elements, there is nothing to divide
    if length_of_array <= 1:
        return array
    #  Else we should create new arrays from divided halves
    else:
        #  Left side of the middle
        left_array = array[:mid]
        #  And right side of the middle
        right_array = array[mid:]

        #  Time for recursion, so we will keep dividing our arrays into smaller ones (check: 'Divide and Conquer')
        merge_sort(left_array)
        merge_sort(right_array)

        #  Merging arrays
        #  We should track each number in array by its index to do comparison for sorting
        i = 0  #  Index for left_array
        j = 0  #  Index for right_array
        k = 0  #  Index for merged array

        #  We will make comparison in while loop, but only if indexes are not smaller than their arrays
        while i < len(left_array) and j < len(right_array):
            #  If number in left array is smaller than one in the right, lets add it first to the sorted array
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                #  Then increase (increment) index, so we will check next number in left_array
                i += 1
            #  If number is bigger or equal, lets add that number from right_array to sorted array
            else:
                array[k] = right_array[j]
                #  And check next number by incrementing index
                j += 1
            #  Then we increase index of sorted array, so that we can add next number to the new empty spot
            k += 1
            #  And repeat until nothing left in either left_array or right_array

        #  If after sorting one of our array left empty, but other array still got some elements
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1


#  List for testing our code
test = [12, 333, 4, 2, 11, 0, 99, 7485, 54, 3, 13, 11, 99, 777, 666, 43, 128, 61]
len_of_unsorted_test = len(test)
print(f"Before merge sort: {test}.")
#  Now lets use merge sort
merge_sort(test)
#  We can check if results are as we intended by 'assert'
assert test == [0, 2, 3, 4, 11, 11, 12, 13, 43, 54, 61, 99, 99, 128, 333, 666, 777, 7485]
assert len(test) == len_of_unsorted_test
#  Finally it is time to see results on screen
print(f"After merge sort: {test}.")
