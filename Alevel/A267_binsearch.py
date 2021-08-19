def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = low+high
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    binary_search(list.sort(), item)

def main(my_list, item):
    ans = binary_search(my_list, item)
    if ans == None:
        my_list.sort()
        ans = binary_search(my_list, 9)
    else:
        print("could not be found")
        return None
    print("element is: ", ans)
