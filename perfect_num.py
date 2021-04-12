def function(num):
    i=1
    sum=0
    while i<=num:
        a=num%i
        num=num//10
        sum=sum+a
        i=i+1
num=int(input("enter the num"))
function(num)
if sum==num:
    print("it is perfect num")
else:
    print("it is not perfect num")

