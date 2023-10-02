from random import randint
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
if __name__ == "__main__":
    arr_length = 10
    arr = []
    
    for i in range(arr_length):
        arr.append(randint(0,100))
        
    print("Original array is: %s" % arr)   
    start_time = time.time() 
    bubble_sort(arr)
    print("Sorted array is: %s" % arr)
    print("--- %s seconds ---" % (time.time() - start_time))