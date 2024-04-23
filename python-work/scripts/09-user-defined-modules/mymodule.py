def checkprime(n):
    flag = True
    for i in range(2, n):
        if(n % i == 0):
            flag = False
            break
    return flag

def factorial(n):
    if(n == 1):
        return 1
    else:
        return n * factorial(n - 1)
    
def binarySearch(arr, start, end, item):

    if start <= end:

        # calculate the middle value
        mid = (start + end) // 2
        #print("Current mid: ", mid, arr[mid])
        
        # check if the item is present in the middle itself
        if(arr[mid] == item):
            #print("Found ->", mid)
            return mid

        # if the item is less than the mid, item can only be present in the left
        # reset the end to point to mid and repeat the process
        elif arr[mid] > item:
            return binarySearch(arr, start, mid - 1, item)

        # if the item is greater than the mid, item can only be present in the right
        # reset the start to point to mid and repeat the process
        elif arr[mid] < item:
            return binarySearch(arr, mid + 1, end, item)

    else:
        return -1
    
def insertionSort(arr):

    n = len(arr)

    if n <= 1:
        return

    # Iterate for n - 1 times: start from index = 1
    for i in range(1, n):

        # store the current element in temp
        temp = arr[i]

        # set the value for j -> supporting variable for going backwards
        j = i-1

        # Start comparing backwards until j reaches the 0th index and also until temp < arr[i] - while
        while j >= 0 and temp < arr[j]:
        
            # Shifting elements 
            arr[j + 1] = arr[j]
            j -= 1

        # Replace the array item by temp -> actual insert position
        arr[j + 1] = temp


# ------------------------------------------------------------------------------------
print("mymodule.py -> __name__ =", __name__)

if __name__ == "__main__":
    L = [23, 12, 56, 34, 45]
    insertionSort(L)
    print(L)