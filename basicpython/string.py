
# str="\"string\" is the collection of the character"
#
# print(str)

#to print str2 in between str1
# str1="adcdef"
# str2="xyz"
# middle=int(len(str1)/2)
# print(str1[:middle]+str2+str1[middle:])


#to print the str firstletter capital
# str="welcome"
# str1=str.capitalize()
# print(str1)

#to print string in lower case
# str="welcome"
# str1=str.islower()
# print(str1)

#to print the string in capital letter
# str="WELCOME"
# str1=str.isupper()
# print(str1)

# str="java is programming language"
# str1=str.replace("java","python")
# print(str1)
#
# str="1,2,3,4"
# list=['a','b','c','d']
# str1=str.join(list)
# print(str1)
#
# str="welcome"
# str1=str.index("m")
# print(str1)

# str="python is programming language"
# str1=str.partition("programming")
# print(str1)

# str="python is programming language"
# str1=str.split()
# print(str1)

# str="prasad tupe"
# str1=str.zfill(20)
# print(str1)


str="python is a programming language"
words=str.split()
for w in words:
    if w[-1]=="e":
        print(w)

#
# str1="adcdefghi"
#
# middle=int(len(str1)/2)
# print(str1[middle-1:middle+2])


# str=[1,2,3,4]
# list1=['a','b','c','d']
# str1=str.join(list1)
#
# print(str1)