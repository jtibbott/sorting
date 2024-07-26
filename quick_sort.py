from random import randint
import time

def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index]
    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1
        while array[end] > pivot:
            end -= 1
        if start < end:
            array[start], array[end] = array[end], array[start]
    array[end], array[pivot_index] = array[pivot_index], array[end]
    return end
    
def quick_sort(start, end, array):
    if start < end:
        p = partition(start, end, array)
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)

if __name__ == "__main__":
    arr_length = 10
    arr = []
    
    for i in range(arr_length):
        arr.append(randint(0,100))
        
    print("Original array is: %s" % arr)   
    start_time = time.time() 
    quick_sort(0, len(arr)- 1, arr)
    print("Sorted array is: %s" % arr)
    print("--- %s seconds ---" % (time.time() - start_time))