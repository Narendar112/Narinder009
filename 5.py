# program to accept price of 10 different items from user,calculate total amount provide discount on the basis of  total amount 
#if amount exceed 2000 apply discount 20%, display discount and final amount.otherwise no discount
a  = int(input("enter price of item 1:"))
b = int(input("enter price of item 2:"))
c  = int(input("enter price of item 3:"))
d  = int(input("enter price of item 1:"))
e  = int(input("enter price of item 5:"))
f  = int(input("enter price of item 6:"))
g  = int(input("enter price of item 7:"))
h  = int(input("enter price of item 8:"))
i = int(input("enter price of item 9:"))
j  = int(input("enter price of item 10:40"))
sum = a+b+c+d+e+f+g+h+i+j
discount = sum*0.20
if sum>= 2000:
    sum = sum-2000
    print("total=",sum)
else: print("total=",sum)