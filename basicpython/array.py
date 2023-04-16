#type 1
# from array import *
# a=array('i',[10,20,30,40,50])

# #print(a)

# for i in a:
#     print(i)


# #type 2
# import array as arr
# a=arr.array('i',[10,20,30,40,50])

# for i in a:
#     print(i)

# from array import *
# num=array('i',[10,20,30,40,50])

# num[2:5]=array('i',[300,400,500])

# #print(num)
# for i in num:
#     print(i)
#from array import ArrayType

from array import  *
a=array('i',[1,2,3,4,5])
b=array('i',[1,2,3,4,5])
c=array('i',[0,0,0,0,0])


for i in range(0,5):
    c[i]=a[i]+b[i]
    print(c[i])

#
# def check(e):
#     return len(e)

#cars=["aa","bbb","c"]

#cars.sort(key=check)   #for asscending order
#cars.sort(reverse=True,key=check)      #for desscnding order
#print(cars)

# def checkduplicate(array_nums):
#     nums_set = set(array_nums)
#     return len(array_nums) != len(nums_set)
# print(checkduplicate([1,2,3,4,5]))
# print(checkduplicate([1,2,3,4,4]))


#file handling

# import os


# f=open("deom.txt","r")
# print(f.read)