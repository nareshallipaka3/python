#n="python's"
#print(n)
#

#n="hello world"
#print(n.upper())
#print(n.lower())
#print(n.index("o"))
#print(n.find("o"))
#print(n.find("n"))
#print(n.startswith("world"))
#print(n.endswith("hello"))
#print(n.startswith("hello"))
#print(n.endswith("world"))
#a=["abc.com","xyz.in","pvr.com"]
#b=[]
#for i in a:
#    if i.endswith("com"):
#        b.append(i)
#print(b)
#h="hai {},how are you".format("naresh")
#print(h)

#names=["naresh","suresh","rajesh"]
#for i in names:
#    print("hai {}".format(i))

#s="naresh123"
#print(s.isalnum())
#s="hello"
#print(s.isalpha())
#print(s.isnumeric())

#a="hello hai friends"
#print(len(a))
##b=a.strip()
#print(len(b))
#c=a.lstrip()
#print(len(c))
#a="welcome to python to world"
#b=a.replace("to","TO")
#print(b)

#a="welcome to python to world"
#b=a.replace("to","TO",1)
#print(b)

#a="welcome to python to world"
#b=a.split()
#n=[]
#for i in a:
 #   if i=="to":
 ##       i="are"
#        n.append(i)
#    else:
#        n.append(i)
#    print(n)

#a="welcome to python to world"
#b=a.split()
#c="@".join(b)
#print(c)
n='''School is the place where we learn to read and write. 
It is the most crucial place for a student, 
and it helps us to learn new things. 
The teachers are always helpful and teach us important
things in life. We must always be regular to school as
missing classes can lead to problems during exams.'''
a=n.replace("is","are").replace("the","that")
print(a)



        