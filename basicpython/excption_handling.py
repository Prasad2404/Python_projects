
# try:
    # a =int(input("enter any number"))
    # b = int(input("enter any number"))
    # c=a/b
    # print(c)
# except Exception as e:
#     print(e)

# try:
#     num=input("enter your name")
# except Exception as a:
#      print(a)
#     prin("code executed sussefully")
#
#     tp=open("nothere")
# except IOError as e:
#     print(e)


try:
    n=int(input("enter any number"))

    if n>=0:
        print("No is Positive")
    else:
        raise ValueError

except ValueError:
    print("No is negative")
