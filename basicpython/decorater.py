#
# def show():
#     def fun1():
#         print("hello")
#     def fun2():
#         print("bye")
#
#     fun1()
#     fun2()
#
# show()

# def display(func):
#     def inner_fun():
#         print("i got decorated")
#         func()
#     return inner_fun
# @display
# def show():
#     print("i am show")
#show()

def simple():
    for i in range(1,11):
        yield i

for i in simple():
    print(i)

