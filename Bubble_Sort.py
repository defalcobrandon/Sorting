'''
This is an example of the Bubble Sort algorithm.
Methodology:
Traverse through the array over and over, comparing one number to the following number.
If they are not sorted, switch their positions.
When you reach the end, if any swaps were made, repeat.
The largest number will always end up at the end, and the second to last, etc
 so we don't have to go through the entire array each time.
Bubble Sort is "in-place"
'''

def bubble_sort(array):
    edge = len(array) - 1
    while True:
        changes_made = False
        for x in range(0, edge):
            if array[x] > array[x + 1]:
                array[x], array[x + 1] = array[x + 1], array[x]
                changes_made = True
        if not changes_made:
            break

    return array

array = [18, 97, 21, 0, 1, -12, 33]
bubble_sort(array)
print(array)
#Output [-12, 0, 1, 18, 21, 33, 97]
