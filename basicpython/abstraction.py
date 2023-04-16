

# from abc import ABC,abstractmethod
#
# class payment(ABC):
#     def print_slip(self,amount):
#         print("purchase of amount - ",amount)
#
#         @abstractmethod
#         def payment(self,amount):
#             pass

# class creditcardpayment(payment):
#     def payment(self,amount):
#         print("credit card payment of - ",amount)
#

# class mobilewalletpayment(payment):
#     def payment(self,amount):
#         print("mobile wallet payment of - ",amount)

# obj=creditcardpayment()
# obj.payment(1000)
# obj.print_slip(1000)

# obj=mobilewalletpayment()
# obj.payment(1000)
# obj.print_slip(1000)



# class Rectangle:
#     __lenght=0
#     __breath=0
#
#     def __init__(self):
#         self.__lenght=5
#         self.__breath=10
#
#         print(self.__lenght)
#         print(self.__breath)
#
# r=Rectangle()


class shape:
    __length=10
    __breath=20

class circle(shape):
    def __init__(self):
        print(self._length)
        print(self._breath)

c=circle()


