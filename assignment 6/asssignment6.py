#a=int(input("Enter a number "))
'''
#q1
if(a>0):
    print("Positive ")
else:
    print("Non-Positive ")
'''
#q2
'''
if (a%5==0):
    print("a is divisible by 5")
else:
    print("Numberis not divisible by 5 ")
'''
#q3
'''
if(a%2==0):
    print("a is divisible by 2")
else:
    print("Numberis not divisible by 2")
'''
#q4
'''
b=int(input("Enter the value of b "))
if (a>b):
    print("a is greater than b ",a)
elif (a==b):
    print("a is equal to b ")
else:
    print("b is greater than a",b)
'''
#q5 
'''
a="Ram"
b="shyam"
if a>b:
    print(a)
else:
    print(b)
    '''
    #q6
'''
a=int(input("Enter a number"))

if a//100>=1 and a//100<10:
    print("It is a three digit number ")
else:
    print("it is not a three digit number ")
    '''
    #q7
'''
  a=int(input("Enter a number "))
if a>0:
        print("Positive ")
elif a==0:
        print("Zero")
else:
        print("Negative ")
'''
#q8
'''
a=int(input("Enter the value of a  "))
b=int(input("Enter the value of b "))
c=int(input("Enter the value of c "))
d=((b*b)-(4*a*c))
if d>0:
    print("Real and distinct roots ")
elif d==0:
    print("Real and equal roots ")
else:
    print("Imaginary roots ")

'''



#q9
'''
a=int(input("Enter a number "))
if a%400==0:
    print("it is a leap year ")
elif a%100==0:
       print("It is not a leap year ")
elif a%4==0:
        print("it is a leap year ")
else:
    print("It is not a leap year ")
'''

   #q10
'''
a=int(input("Enter the value of a  "))
b=int(input("Enter the value of b "))
c=int(input("Enter the value of c "))
if a>=b and a>=c:
    print(a)
elif b>=c and b>=a:
    print(b)
else:
    print(c)
'''
#q11
'''
x=input("Enter month")
match x:
    case "january":
        print("0")
    case "february":
        print("1")
    case "march":
        print("3")
    case "april":
        print("4")
    case "may":
        print("5")
    case "june":
        print("6")
    case "july":
        print("7")
    case "august":
        print("8")
    case "september":
        print("9")
    case "october ":
        print(10")
    case "november":
        print("11")
    case "december":
        print("12")
    '''
    #q12
'''
a=int(input("Enter the real part "))
b=int(input("Enter the imaginary part"))
c=complex(a[b])
if a>b:
    print("real part is greater than imaginary part")
elif a==b:
    print("Real part is eaual to imaginary part ")
else:
    print("Real part is less than imaginary part ")
'''
