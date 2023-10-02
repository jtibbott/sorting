from random import randint
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key< arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key

if __name__ == "__main__":
    arr_length = 10
    arr = []
    
    for i in range(arr_length):
        arr.append(randint(0,100))
        
    print("Original array is: %s" % arr)   
    start_time = time.time() 
    insertion_sort(arr)
    print("Sorted array is: %s" % arr)
    print("--- %s seconds ---" % (time.time() - start_time))