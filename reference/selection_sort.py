## takes O(n^2) time - slow!!!
## adds smallest element to a new list and then removes it
def findsmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionsort(arr):
    newarr = []
    for i in range(len(arr)):
        smallest = findsmallest(arr)
        newarr.append(arr.pop(smallest))
    return newarr
