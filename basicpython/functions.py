'''
def info():
    print("it is default function")
info()

def addition(a,b):
    c=a+b
    print("Addition",c)
a=int(input("enter any number"))
b=int(input("enter any number"))

addition(a,b)
'''


'''
def hello(a,b):
    c=a+b
    return c

print("addition",hello(20,30))

result=hello(30,40)
print("addition =",result)
'''

#using lambda
#to print table
'''
table=lambda num,i:num*i
num=int(input("enter the number"))
for i in range(1, 11):
   print(num, 'x', i,'=', table(num,i))
'''

#to print area of triangle
#area = 0.5 * b * h

'''
area=lambda b,h:0.5*b*h
b=int(input("enter the base"))
h=int(input("enter the height"))
print(area(b,h))
'''

#factorial

'''
def factorial(n):
    if n<=10:
    print(n)
    factorial(n+1)

factorial(1)
'''

