#calculations
# def add(a,b):
#     return(a+b)
# def sub(a,b):
#     return(a-b)
# def mul(a,b):
#     return(a*b)
# def division(a,b):
#     return(a/b)


# a=int(input("enter a value:"))
# b=int(input("enter b value:"))
# if option==1:
#     print("a+b=",add(a,b))
# elif option==2:
#     print("a-b=",sub(a,b))
# elif option==3:
#     print("a*b=",mul(a,b))
# elif option==4:
#     print("a/b=",division(a,b))
# else:
#     print("YOU ARE ENTERED WRONG OPTION")





print("welcome to state bank of india")

n='''
1.deposite
2.withdraw
3.balance
4.exit
'''
username="naresh"
password=225
amount=5000
username=input("enter your username:")
password=input("enter your password")
if username==username and password==password:
    print(n)
    option=int(input("enter your option:"))
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

    
def deposite():
    a=int(input("enter deposite amount:"))
    b=a+amount
    print(b)
#deposite()
    
    
def withdraw():
    c=int(input("enter withdraw amount:"))
    d=amount-c
    print(d)
#withdraw()
    
def balance():
    print(amount)
    
def exit():
    print("exit")
    
if option==1:
    deposite()
elif option==2:
    withdraw()
elif option==3:
    balance()
elif option==4:
    exit()
else:
    print("INVALID OPTION")
    