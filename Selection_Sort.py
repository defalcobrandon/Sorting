'''
This is an example of the Selection Sort algorithm.
Methodology:
Figuratively divide the array into sorted and unsorted sections.
Don't actually create 2 arrays; just use variables to mark their boundaries.
Traverse through the array over and over, and find the smallest number.
Swap the smallest number with the beginning of the unsorted section's first number.
ie.
[3,47,2,98] - 2 is the smallest
[2,47,3,98] - 2 is now the end of the sorted section and 47 is the beginning of unsorted
[2,3,47,98] - 3 and 47 have switched and 3 is the end of the sorted section and so on
'''

def selection_sort(array):
    changes_made = True

    while changes_made:
        changes_made = False

    for x in range(len(array)):
        smallest_index = get_smallest_index(x, array)

        if smallest_index != x:
            array[x], array[smallest_index] = array[smallest_index], array[x]
            changes_made = True


def get_smallest_index(unsorted_index, array):
    smallest_index = unsorted_index
    for x in range(unsorted_index, len(array)):
        #print(smallest_index, array[smallest_index])
        if array[x] < array[smallest_index]:
            smallest_index=x

    return smallest_index

array = [18, 97, 21, 0, 1, -12, 33]

selection_sort(array)
print(array)

#output [-12, 0, 1, 18, 21, 33, 97]
