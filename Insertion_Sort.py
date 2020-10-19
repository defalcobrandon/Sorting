'''
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.
Algorithm
To sort an array of size n in ascending order:
1: Iterate from arr[1] to arr[n] over the array.
2: Compare the current element (key) to its predecessor.
3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.
'''
def insertion_sort(array):
    for x in range(1, len(array)):
        y = x

        while y > 0 and array[y] < array[y-1]:
            array[y-1], array[y] = array[y], array[y-1]
            y=y-1
    return array

array = [18, 97, 21, 0, 1, -12, 33]
print(insertion_sort(array))

#Output [-12, 0, 1, 18, 21, 33, 97]
