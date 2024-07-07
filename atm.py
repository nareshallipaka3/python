#
a='''
1.debit
2.credit
3.mini statement
4.exit
   '''
name="n"
password=123
username=input("enter username:")
password=input("enter password:")
amount=1000
if name==username and password==password:
    print(a)
    option=int(input("enter option:"))
    if option==1:
        debit=float(input("enter amount:"))
        print("amount after debit:",amount-debit)
    elif option==2:
        credit=float(input("enter amount:"))
        print("amount after credit:",amount+credit)
    #elif option==3:
    #    print("amount:",amount)
    #elif option==4:
    #    print("exit")
else:
   print("incorrect")
   
   
   
   
   
   
   

# print("incorrect")

# print("incorrect")

n='''
1.deposite
2.withdraw
'''
user="naresh"
passcode=225
username=input("enter username:")
passcode=input("enter passcode:")
amount=500
if user==username and passcode==passcode:
    print(n)
    option=int(input("enter option"))
    if option==2:
        withdraw=float(input("enter withdraw:"))
        print("withdraw after amount:",amount-withdraw)
    elif option==1:
        deposite=float(input("enter deposite:"))
        print("after deposite total rs:",amount+deposite)
    
else:
    print("error")