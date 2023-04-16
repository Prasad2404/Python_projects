# import os
# f=open("demo.txt","r")
# print(f.read())


import os
# f=open("demo.txt","w")
# f.write("welcome")

#open("demo1.txt","x")

# f=open("student_details.txt","w")
# name=int(input("enter the name"))
# f.write(name)
# f1=open("student_details.txt","r")
# print(f1.read())


#os.remove("demo.txt")

# if os.path.exists("demo1.txt"):
#     os.remove("demo1.txt")
# else:
#     print("Not Found")


with open("student_details.txt","w") as f:
    name=int(input("enter some thing"))
    print(name.read())