'''
print("Venkatesh!!How's things Going on!!")

a = 25

print("a:","\t",a)

print("2**2:",2**2)

#float b = 30.3

print("25**25:",a**a)

my_city = "NAMAA BENGALURU"

print(my_city)

print(my_city[2],my_city[0:4],len(my_city),my_city[7])

a = "is our own city"
print(my_city+"\t",a)

print (3*my_city)

#i = raw_input("enter the value:")
#print(i)

j=input("enter the same value:")
print(j)

a=(11,22,13,15)
#def myfunct(x):
for i in a:
  if(a%2==0):
       print(a,"is even")
       break
  else:
       print(a,"is odd")

#myfunct(22)


globalvar = 10
def myfunc(x):
  localvar = 5
  globalglobalvar = 20
  print(localvar)
  print(globalglobalvar)
  
print(localvar)
print(globalvar)

myfunc(25)

c=0

def myfunc(n1,f):
  if(f(n1)==f(-n1)):
    print("True")
  else:
    print("false")

def square(n):
  return n*n
 # print(a)

def cube(n):
  return n*n*n
 # print(b)

#x=2
#y=3

#square(2)
#cube(3)

myfunc(square,cube)

if(1+1==2):
  print("Correct")
else:
  print("wrong")

count = 0
for letter in "HELLO WORLD":
  if(letter=="L"):
    count =+ 1 
    print("count of L =",count)
 # else:
  #  if(i=='A'):
   #  count =- 1
    # print("count of A =",count)

cnt=0
i=0
while("HELLO WORLD"):
  if(i=="L"):
    cnt=+1
    print(cnt)


a = [10,20,30]
print(a)
print(a[1])
b=[40,50,60]
print(a+b)
print(a[0],"+",b[0])

c=a.append(200)
print(c)

del(a[1])
print(a)

x=[a,b]
print(x)

print("a befor delete")
del(a)
print("a after delete")
'''
'''
import re

line = "This is Venkatesh and my work is to verify the SoC work level Ip's work the help oh UVM "
sv = re.split("work",line)
for i in sv:
  print(sv)

ss = re.search("Venkatesh",line)
print(ss)

sc=re.match("This",line)
print(sc)

sk=re.findall("work",line)
print(sk)

q=[1,2,3]
q += ['numbers']
print(q)

b=[4,q,5,6]
print(b)
print(b[1][1])

dic = {'venkat':'student','siva':'employe','vamsi':'lecturer'}
print(dic)
print(dic['venkat'])
dic['venkat']='CEO'
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())

del dic['vamsi']
print(dic)

dic['muneeb']='instructor'
print(dic)

# print(dic.has_key('siva'))

print(dic.get('muneeb'))

x='hi'
y='hi'

print(x is y)

x=[]
y=[]
print(x is y)

a=[1,3,5]

b=a;

c=a[:]

b[0]=2
c[0]=3
print(a,b,c)
'''
'''
b=0
def my(): 
   a=[1,2,3]
   b=a.append(4)
 return(print(b))
'''   


def myfunc(n1,f):
  if(f(n1)==f(-n1)):
    return("True")
  else:
    return("false")

def square(n):
  return n*n
 # print(a)

def cube(n):
  return n*n*n
 # print(b)

#x=2
#y=3

#square(2)
#cube(3)

print(myfunc(2,square))
print(myfunc(2,cube))
