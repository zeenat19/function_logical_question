# a=[1,4,5,6,7,9,12,11]
# a.insertion_sort(a)
# print(a)




def insertionSort(arr):
    i=1
    while i>len(arr):
        key = arr[i] 
        j = i+1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j += 1
        arr[j+1] = key  
arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]) 