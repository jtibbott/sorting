from random import randint
import time

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    
if __name__ == "__main__":
    arr_length = 10
    arr = []
    
    for i in range(arr_length):
        arr.append(randint(0,100))
        
    print("Original array is: %s" % arr)   
    start_time = time.time() 
    selection_sort(arr)
    print("Sorted array is: %s" % arr)
    print("--- %s seconds ---" % (time.time() - start_time))