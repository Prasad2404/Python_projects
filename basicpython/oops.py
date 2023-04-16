
# class sample:
#     def show(self):
#         print("I am Show")
#
#     def display(self):
#         print("I am Display")
#
# s1=sample()
# s1.show()
# s1.display()



#using construtor

# class student:
#     def __init__(self):
#         print("i am default construtor")
#
#     def info(self):
#         print("i am method")
#
# s1=student()
# s1.info()



#declaring value in construtor

# class person:
#     def __init__(self,id,name):
#         self.id=id
#         self.name=name
#
#     def student_info(self):
#         print(self.id)
#         print(self.name)

# p1=person(101,"prasad")
# # print(p1.id)
# # print(p1.name)

# p1.student_info()


# class vehical:
#     def __init__(self,max_speed,milage):
#         self.max_speed=max_speed
#         self.milage=milage

# v1=vehical(160,20)
# print("max speed of vehical is",v1.max_speed)
# print("milage of vehical is",v1.milage)


# class area:
#     def __init__(self,radius,lenght,breath,base,height):
#         self.radius=radius
#         self.lenght=lenght
#         self.breath=breath
#         self.base=base
#         self.height=height
#
#
#     def area_rectangle(self):
#         area_rectangle=self.lenght * self.breath
#         print(self.area_rectangle)
#
#     def area_triangle(self):
#         area_triangle=1/2 * self.base * self.height
#         print(self.area_triangle)
#
#     def area_circle(self):
#         area_circle=3.14 * self.radius * 2
#         print(self.area_circle)
#
# a1=area(10,20,30,40,50)
# a1.area_triangle()
# a1.area_rectangle()
# a1.area_circle()


# class employee:
#     pass
# e1=employee()




#multilevel inheritance

# class parent:
#     def display(self):
#         print("I am parent class method")

# class child(parent):
#     def show(self):
#         print("i am child class method ")

# class student(child):
#     def car(self):
#         print("hello")

# s1=student()
# s1.display()
# s1.show()
# s1.car()




#multiple inheritance

# class a:
#     def bike(self):
#         print("hello")
#
# class b:
#     def car(self):
#         print("hiii")
#
# class c(a,b):
#     def show(self):
#         print("byee")
#
#
# c1=c()
# c1.bike()
# c1.car()
# c1.show()



#hierarchical inheritance

# class main:
#     def a(self):
#         print("head branch")
#
# class sub1(main):
#     def b(self):
#         print("sub branch 1")
#
# class sub2(main):
#     def c(self):
#         print("sub branch 2")
#
# class sub3(main):
#     def d(self):
#         print("sub branch 3")
#
# b1=sub1()
# b1.a()
# b1.b()
#
# b2=sub2()
# b2.a()
# b2.c()
#
# b3=sub3()
# b3.a()
# b3.d()




#overlloding

# def add(a,b):
#     c=a+b
#     print(c)
#
# def add(x,y,z=0):
#     r=x+y+z
#     print(r)
#
# add(10,20)
# add(10,20,30)



# class parent:
#     def show(self):
#         print("I am parent class method")
#
# class child(parent):
#     def show(self):
#         parent.show(self)
#         print("i am child class method ")
#
# c1=child()
# c1.show()



class student:
    def swap(self,a,b):
        self.a=b
        self.b=a
        temp_var=self.a
        self.a=self.b
        self.b=temp_var
        print(self.a,self.b)
class person(student):
    def swap(self,x=0,y=0):
        self.x=x
        self.y=y
        person.swap()
        print(self.x=self.y,self.y=self.x)


s1=person()
s1.swap(10,20)








