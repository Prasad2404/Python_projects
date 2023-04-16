'''
num=int(input("enter any number"))

if num>=0:
    if num%2==0:
        print("number is even")
    else:
        print("number is odd")
else:
    print("number is negative")
'''

#for loop

#for i in range(1,11):
 #   print(i)

#for i in range(11,0,-1):
#   print(i)

#to print even numbers
#for i in range(0,100,2):
#   print(i)


'''
sum=int(input("enter any number"))
total=0
for i in range(1,sum+1):
    total=total+i
print(total)
'''


'''
for i in range(1,10):
    num=i/2
    if(num%2==0):
        print(i)
    else:
        print(i)
'''


#while loop

#i=1
#while i<=10:
#    print(i)
#    i=i+1


#sum of digit
'''
sum=int(input("enter any number"))
total=0
while(sum>0):
    dig=sum%10
    total=total+dig
    sum = sum // 10
print(total)
'''

#do while

# i=1
# while True:
#     print(i)
#     i=i+1
#     if i>10:
#         break

a=50
b=100

print("prime numbers between 50 and 100 are")

for i in range(a,b +1):
    if i > 1:
        for num in range(2,i):
            if(i % num) == 0:
                break

        else:
            print(i)
