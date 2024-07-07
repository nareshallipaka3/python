#def naresh(a,b):
#    print("hello",a,b)
#naresh(1,2)

 
# def naresh(name):
#      print("hello",name)
# n=input("enter your name:")
# naresh(n)

# def naresh(*a):
#     print("hello",a)
# naresh(1,2,3,4)

# def naresh(**a):
#     print("hello",a)
# naresh(a=1,b=3,c=2)

# def naresh():
#     print("hello")
#     def vijay():
#         print("hai")
#     vijay()
# naresh()

# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)

# lambda fuction
# n=lambda a,b,c:a+b+c
# print(n(2,4,5))
    
# a=[1,2,3,4]
# b=[]
# for i in a:
#     c=lambda n:n+1
#     b.append(c(i))
# print(b)

# hello=[35,54,12,14]  #filter
# def naresh(n):
#     if n>20:
#         return True
#     else:
#         return False
# hai=filter(naresh,hello)
# print(list(hai))


# n=(1,2,3,4)   #map
# def naresh(a):
#     return a+a
# b=map(naresh,n)
# print(list(b))



# from functools import reduce
# b=reduce(lambda m,n:m+n,[12,43,56,122])
# print(b)


# def simplegeneratorfun():
#     yield 1
#     yield 2
#     yield 3
# x=simplegeneratorfun()
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())



# def naresh():
#     yield 1
#     yield 2
#     yield 3
# x=naresh()
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())


#calculations
def add(a,b):
    return(a+b)
def sub(a,b):
    return(a-b)
def mul(a,b):
    return(a*b)
def division(a,b):
    return(a/b)

option=int(input("enter option:"))
a=int(input("enter a value:"))
b=int(input("enter b value:"))

if option==1:
    print("a+b=",add(a,b))
elif option==2:
    print("a-b=",sub(a,b))
elif option==3:
    print("a*b=",mul(a,b))
elif option==4:
    print("a/b=",division(a,b))
else:
    print("YOU ARE ENTERED WRONG OPTION")


# print("welcome to state bank of india")

# n='''
# 1.deposite
# 2.withdraw
# 3.balance
# 4.exit
# '''
# username="naresh"
# password=225
# amount=5000
# username=input("enter your username:")
# password=input("enter your password")
# if username==username and password==password:
#     print(n)
#     option=int(input("enter your option:"))
#     if option==1:
#         deposite=float(input("enter deposite amount:"))
#         print("after deposite total amount:",amount+deposite)
#     elif option==2:
#         withdraw=float(input("enter withdrar amount:"))
#         print("withdraw after total amount:",amount-withdraw)
#     elif option==3:
#         print("display of amount:",amount)
#     elif option==4:
#         print("THANK YOU VISIT AGAIN")
#     else:
#         print("invalid option")
# else:
#     print("INCORRECT OPTION")

    