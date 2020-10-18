'''
This is an example of the Quick Sort algorithm.
Methodology:
This is a recursive algorithm so you have a "Base Case" and "Recursion".
-The "Base Case" is what will cause the recursion to eventually stop, like a break in a loop.
-The "Recursion" will take a smaller subset of your data and that function will call itself.
Choose a pivot number. This can be any number, but this example uses the pop() method.
Compare each number in the list to the pivot and place that number into either the "smaller" or "larger" list.
The recursion will then do the same with the "smaller" and "larger" lists, eventually hitting the Base Case.
'''

def quick_sort(sequence):
    # Base Case
    if len(sequence) <= 1:
        return sequence
    else:
        pivot  = sequence.pop()
        larger = []
        smaller  = []
        for n in sequence:
            if n > pivot:
                larger.append(n)
            else:
                smaller.append(n)
        # Recursion
        return quick_sort(smaller) + [pivot] + quick_sort(larger)

sequence = [18, 97, 21, 0, 1, -12, 33]
print(quick_sort(sequence))

#Output: [-12, 0, 1, 18, 21, 33, 97]
