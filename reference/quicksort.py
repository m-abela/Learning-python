'''
quick sort works by taking the first element as the pivot and putting all smaller elements
on the left and larger ones on the right and then returns it

fastest case: O(log n)
worst case: O(n^2) - if the left side is empty then it will be sorting
mothing on the left and take up more time

'''
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

##rint(quicksort([10,5,2,3,20,45,11]))
