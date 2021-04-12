# def function(shorting_list):
#     i=0
#     shorting_list.sort()
#     print(shorting_list)
# shorting_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15] 
# function(shorting_list)


# my_list = [15, 26, 15, 1, 23, 64, 23, 76]
def function(list):
    new_list = []
    while num:
        min = num[0]  
        for x in num: 
            if x < min:
                min = x
        new_list.append(min)
        num.remove(min)  
    print(new_list)
num = [15, 26, 15, 1, 23, 64, 23, 76]
function(num)  
