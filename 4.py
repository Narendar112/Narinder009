#write a program to accept marks of 5 subjects from user calculate total,calculate percentage,print result pass or fail
Hindi =int(input("enter marks of Hindi"))
English = int(input("enter marks of English"))
Maths = int(input("Enter marks of Maths"))
Science = int(input("Enter marks of Science"))
History = int(input("Enter marks of History"))
Percentage = (Hindi+English+Maths+Science+History)/500*100
if Percentage>=50:
    print("pass")
else:("fail")