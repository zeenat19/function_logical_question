# def function(num):
#     return("the book of elie")
# function(5)
# i=1
# while i<=5:
#     print("the book of elie")
#     i=i+1


# num_list=[24, 33, 44, 5, 21, 19, 23, 30]
# print("unsorted list:",num_list)
# for j in range (len(num_list)-1,0,-1):
# 	for i in range (j):
# 		if num_list[i]>num_list[i+1]:
# 			num_list[i],num_list[i+1]=num_list[i+1],num_list[i]
# 			list2=num_list
# 	else:
# 		list1=num_list
# print("sorted list:",num_list)


mainStr = "the quick brown fox jumped over the lazy dog the dog slept over the verandah."
newStr = mainStr.split(" ")
i=0
a = ""
while i < len(newStr):
	if newStr[i] == "over":
		a = a+  "on" + " "
	else:
		a = a + newStr[i] + " "
	i = i + 1		
print(a)
