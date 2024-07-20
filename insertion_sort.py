"""
Insertion Sort algorithm
"""

# Example that need sorting:
arr = [0, -1, 90, -12, 4, 9]


# Insertion sort itself:
def insertion_sort(arr):
    arr_lngth = len(arr)  # Let's store length of our array for better access
    if arr_lngth <= 1:  # If our list is empty, there is nothing to sort
        return
    for i in range(1, arr_lngth):  # Iteration for our array to compare numbers
        key = arr[i]  # We need to pick a key number to compare the one with others
        j = i - 1 # And variable which will help us with iteration of other numbers that we will compare key with
        while j >= 0 and arr[j] > key:  # "While" loop to compare our key with every other number
            arr[j + 1] = arr[j]  # And if previous number is larger, swap them
            j -= 1  # Then let's compare our key with another number on the left and reapat our loop
        arr[j + 1] = key  # When there is nothing to compare with, we need to place our key on ther right spot

print(f"Before: {arr}")
insertion_sort(arr)
print(f"After: {arr}")
