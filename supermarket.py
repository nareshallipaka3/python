from datetime import datetime
name=input("enter your name:")

list='''
rice 60/kg
dal 50/kg
'''
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
finalamount=[]
items={'rice':60,"dal":50}
option=int(input("for list of items press 1:"))
if option==1:
    print(list)
for i in range(len(items)):
    opt=int(input("if you want buy press 1or exit for 2:"))
    if opt==2:
        break
    if opt==1:
        item=input("enter item:")
        quantity=int(input("enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice)*5/100
            finalprice=totalprice+gst
            #print(finalprice)
        else:
            print("sorry you entered item is not available")
            
    else:
        print("you entered wrong number")
        
    opt=input("can i bill the items yes or no:")
    if opt=='yes':
       pass
       if finalamount!=0:
             
           
           
           for i in range(len(pricelist)):
               print(i,ilist[i],qlist[i],plist[i])
               
               
            
    
            
        
            
            
            
            
            