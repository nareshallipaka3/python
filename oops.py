# class naresh():
#     print("hello")
# naresh()

# class naresh():
#    
#     def n(self):
#         print("hello")
# b=naresh()
# b.n()
        
# class naresh():
#     a=10
#     def n(self):
#         print(self.a)
# b=naresh()
# b.n()

# class naresh():
#     a=2
#     def output(self):
#         print("hello")
# ram=naresh()
# raju=naresh()
# ram.output()
# raju.output()

# class mobile():
#     def __init__ (self,mobilename,ram,battery,price):
#         self.a=mobilename
#         self.b=ram
#         self.c=battery
#         self.d=price
#     def data(self):
#         print("mobilename:",self.a)
#         print("ram:",self.b)
#         print("battery:",self.c)
#         print("price:",self.d)
#     while True:
#         mobilenames=input("enter mobilename:")
#         rams=input("enter ram:")
#         batterys=input("enter battery:")
#         prices=int(input("enter price:"))
# features=mobile("mobilename","ram","battery","price")
# features.data()
# # features=mobile("lenova","8gb","4500mah",12000)
# # features.data()

# class bike():
#     def __init__ (self,bikename,ingine,milage):
#         self.a=bikename
#         self.b=ingine
#         self.c=milage
#     def data(self):
#         print("bikename:",self.a)
#         print("ingine:",self.b)
#         print("milage:",self.c)
#     while True:
#         bikename=input("enter bikename:")
#         ingine=input("enter ingine:")
#         milage=input("enter milege:")
# features=bike("bikename","ingine","milege")    
# features.data() 
# # features=bike("yamaha",100cc,70/1ltr)    
# # features.data()   



# #single inheritance:
# class father():
#     def outputf(self):
#         print("hello world")
# class child(father):
#     def outputc(self):
#         print("welcome")
# obj=child()
# obj.outputc()
# obj.outputf()


#multiple inheritance:
# class grandfather():
#     def outputgf(self):
#         print("hello")
# class father(grandfather):
#     def outputf(self):
#         print("welcome")
# class child(father):
#     def outputc(self):
#         print("hai")
# obj=child()
# obj.outputc()
# obj.outputf()
# obj.outputgf()

# #multilevel inheritance:
# class grandfather():
#     def outputgf(self):
#         print("hello")
# class father(grandfather):
#     def outputf(self):
#         print("welcome")
# class child(father):
#     def outputc(self):
#         print("hai")
# obj=child()
# obj.outputc()
# obj.outputf()
# obj.outputgf()

# #multiple inheritance:
# class father():
#     def outputf(self):
#         print("father")
# class mother():
#     def outputm(self):
#         print("mother")
# class child(father,mother):
#     def outputc(self):
#         print("son")
# obj=child()
# obj.outputc()
# obj.outputf()
# obj.outputm()

#hirarchial inheritance:
# class father():
#     def outputf(self):
#         print("father")
# class child1(father):
#     def outputc1(self):
#         print("child1")
# class child2(father):
#     def outputc2(self):
#         print("child2")
# m=child1()
# n=child2()
# m.outputc1()
# m.outputf()
# n.outputc2()
# n.outputf()


#polymorphism:
#methodoverloading
# class hai():
#     def naresh(self,a=None,b=None,c=None):
#         print(a,b,c)
# obj=hai()
# obj.naresh(1)
# obj.naresh(1,2)
# obj.naresh(1,2,3)
# obj.naresh()

#methodoverriding
# class naresh():
#     def hello(self):
#         print("welcome")
# class vijay(naresh):
#     def hello(self):
#         print("python world")
#         super().hello()
# obj=vijay()
# obj.hello()

#
# protected 
# class gfather():
#     def __init__(self,a):
#         self._y=a
#         print(self._y)
# class father(gfather):
#     def outputf(self):
#         print(self._y)
# class child(father):
#     def outputc(self):
#         print("hai",self._y)
# obj=child(225)
# obj.outputc()
# obj.outputf()
    
#private
# class gfather():
#     def __init__(self,a):
#         self.__y=a
#         print(self.__y)
# class father(gfather):
#     def outputf(self):
#         print(self.__y)
# class child(father):
#     def outputc(self):
#         print("hai",self.__y)
# obj=child(225)
# obj.outputc()
# obj.outputf()

# from abc import ABC,abstractmethod
# class cars():
#     @abstractmethod
#     def mileage(self):
#         pass
# class maruthi(cars):
#     def mileage(self):
#         print("mileage is 25")  
# class suzuki(cars):
#     def mileage(self):
#         print("mileage is 35")
# class tata(cars):
#     def mileage(self):
#         print("mileage is 45") 
# a=tata()  
# a.mileage()
# b=suzuki()  
# b.mileage()
# c=maruthi()  
# c.mileage()    


string=input("enter string:")

a=string[::-1]
if string==a:
    print("polyndram")
else:
    print("not polyndram")
    
    