
#list1=[1,2,"abc","xyz",90]

#print(list1)   #to print list at is it.

#print(list1[1])  #to print list of specific address

#print(list1[0:3])   #to print list from 0 to 3

#for i in list1:
#    print(i)       #to print list using for loop

#print(type(list1[3]))   #to check the type of values



#to accept the list from user
'''
list1=[]
n=int(input("how many elements"))

for i in range(0,n):
    ele=int(input())
    list1.append(ele)

print(list1)

#to check the number in the list

a=int(input("enter any number"))
if a in list1:
    print("present")
    if a in list1:
        ans=a*10
        print(ans)
else:
    print("not present")
'''
#print only unique number in list 2
#eg-list2={1,2,3,4}

# list1={1,2,3,4}
# list2=['a','b','c','d']
# for str1 in list2:
#     str1=list1.isdisjoint(list2)
#
# print(str1)


a={1,2,3,4}
b={'a','b','c','d'}
# dict={1 : 'a',2 : 'b',3 : 'c',4 : 'd'}
# print(dict)

d={}

for keys in a:
    for values in b:
        d[keys]=values
        break

print(d)