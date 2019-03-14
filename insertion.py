import random

def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key
        
print ("============Insertion Sort============")
print ("\nData before sorted:")
arr = [5, 26, 13, 25, 84, 23, 2, 36, 32, 64]

random.shuffle (arr)
print (arr, end=' ')

insertionSort(arr)
print ("\n\nData after sorted:")
print (arr, end=' ')
