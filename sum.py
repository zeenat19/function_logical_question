# def function(numbers):
#     i=0
#     print(sum(numbers))
# numbers = [1, 2, 3, 4, 5] 
# function(numbers)

# def insertion_sort(array, compare_function):
#     for index in range(1, len(array)):
#         currentValue = array[index]
#         currentPosition = index

#         while currentPosition > 0 and compare_function(array[currentPosition - 1], currentValue):
#             array[currentPosition] = array[currentPosition - 1]
#             currentPosition = currentPosition - 1

#         array[currentPosition] = currentValue


array = [4, 22, 41, 40, 27, 30, 36, 16, 42, 37, 14, 39, 3, 6, 34, 9, 21, 2, 29, 47]
insertion_sort(array)
print("sorted array: " + str(array))
