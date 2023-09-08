"""
Simple quicksort algorithm
"""


def quicksort(arr):
    #  Is our array empty or with only one element?
    if len(arr) < 2:
        #  If so, then lets return it without further actions
        return arr
    else:
        #  Let's find our pivot for each array
        piv = arr[0]

        #  Now create array with smaller numbers than our pivot
        less_than_piv = [i for i in arr[1:] if i <= piv]

        #  And array with bigger numbers than pivot
        more_than_piv = [i for i in arr[1:] if i > piv]

        #  If you want to see, how is it working inside, 'uncomment' lower lined:
        #  print(f"Our pivot is {piv}. Now lets see array with numbers smaller than pivot: {less_than_piv}.\n"
        #  f"And array with numbers bigger than pivot: {more_than_piv}\n")

        #  In the end we return sorted lists added to each other, so we will have one sorted list. Check: "Divide and Conquer", for more Details.
        #  Remember we are using something called "stack". For more info go to: https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
        return quicksort(less_than_piv) + [piv] + quicksort(more_than_piv)


#  Now we want to check if everything is working like it should
array_to_sort = [123, 4, 90, 333, 21, 76, 5, 449, 999001, 23348, 128, 4459, 112, 0]
sorted_array = quicksort(array_to_sort)

#  Assert is perfect method for checking if our code is correct
assert sorted_array == [0, 4, 5, 21, 76, 90, 112, 123, 128, 333, 449, 4459, 23348, 999001]

#  Finally it's time to see results:
print(f"Our array: {array_to_sort}. \nAnd after quicksort: {sorted_array}")
