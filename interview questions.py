# #question-1:
# the given number positive,negative or 0
# number=float(input("enter any number:"))
# if number<0:
#     print('negative')
# elif number>0:
#     print("positive")
# elif number==0:
#     print("zero")
# else:
#     print("hello")



#question-2:
# find out even or odd numbers
# naresh=int(input("enter number:"))
# if naresh%2==0:
#     print("{0} is even".format(naresh))
# else:
#     print("{0} is odd ".format(naresh))



#question-3:
# find out leap year
# def checkyear(year):
#     return((year % 4==0) and(year % 100 !=0) or (year % 400==0))
# year=int(input("enter year:"))
# if(checkyear(year)):
#     print("leap year")
# else:
#     print("not a leap year")


#question-4:
# find largest number

# a=int(input("enter a number:"))
# b=int(input("enter b number:"))
# c=int(input("enter c number:"))
# if (a>=b and a>=c):
#     largest=a
# elif (b>=a and b>=c):
#     largest=b
# else:
#     largest=c
#     print("largest number:",largest)

# if (a>=b and a>=c):
#     largest=a
# elif (b>=a and b>=c):
#     largest=b
# else:
#     largest=c
#     print("largest number:",largest)
    
    
    

#question-5:
# def permutation(string,i=0):
#     if i==3:
#         print("".join(string))
#     for j in range(i,len(string)):
#         words=[c for c in string]
#         words[i],words[j]=words[j],words[i]
#         permutation(words,i+1)
        
# permutation("hai")
        
#question-6
# def is_prime(number):
#     if number>1:
#         for num in range(2,number):
#             if number%num==0:
#                 return "not a prime"
#         return "is prime"
#     return "not a prime"
# print(is_prime(59))

#question-7
#armstrong or not
# n=int(input("enter number:"))
# s=n
# b=len(str(n))
# #print(b)
# sum=0
# while n!=0:
#     r=n%10
#     sum=sum+(r**b)
#     n=n//10
# if s==sum:
#     print("armstrong")
# else:
#     print("not a armstrong")

    
            
#question-8
# s="mom"
# def poly(s):
#     return s==s[::-1]
# ans=poly(s)
# if ans:
#     print("polyndrome")
# else:
#     print("not a polyndrome")

#question-9
# def sum(numbers):
#     total=0
#     for x in numbers:
#         total+=x
#     return total
# print(sum([1,2,3,4])) 

#question-10
# a=[1,2,3]
# b=[4,5,6]
# results=map(lambda x,y:x+y,a,b)
# print(list(results))


#question-11
#remove punctuation
# punctuation="'',./@#$%&*"
# string=input("enter sring:")
# new=" "
# for i in string:
#     if i not in punctuation:
#         new+=i
#     print(new)

#question-12
#reverse number
# num=12345
# a=str(num)[::-1]
# print(a)
  
#question-13
#half pyramid using with *
# row=4
# for i in range(row):
#     for j in range(i+1):
#         print("*",end="")
#     print()


#question-14
#how to access keys and values in dictionary
# details={'name':'naresh','roll':25}
# for i,j in details.items():
#     print(i,j)


#question-15
#multiplication
# num=int(input("enter any number:"))
# for i in range(1,11):
#     print(num,"*",i,"=",num*i)




# st='narayana tech house'
# print(st.endswith('e'))

# i=1
# while i<4:
#     i+=1
#     print(i,end=',')

# i=1
# list=[]
# while i<4:
#     list.append(i)
#     i+=1
# print(list)


# st='Narayana'
# print(st.split('a'))



# list=[]
# for i in range(1,6):
#     # print(i)
#     if i%2==0:
#         continue
#     list.append(i)
# print(list)


st='Narayana'
print(st.replace('a','_',2))