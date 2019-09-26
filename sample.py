##n=int(input("enter a number"))
##p=int(input("enter a number"))
##for j in range(n,p+1):
##     c=0
##    for i in range(1,j+1):
##        if j%i == 0:
##           c=c+1
##    if c>2:
##        print(str(j)+"is composite")
##    else:
##         print(str(j)+"is prime")
##           





##
##n=5
##for i in range(1,n+1):
##   for j in range(1,i+1):
##       print(j,end="")
##   print()




##pattern ---- characters
##n=5
##for j in range(ord("a") , ord("a")+n):
##      for i in range(ord("a") , j+1):
##           print(chr(i),end="")
##      print()
    


##pattern
##n=5
##for i in range(1,n+1):
##    print(" "*(n-i)+"*"*i)



##multiplication table
##n=int(input("enter a number:"))
##for i in range(1,11):
##  print(n,"x",i,"=",n*i)


##pattern - pyramid
##n=5
##for i in range(1,n+1):
##    print(" "*(n-i)+"*"*i)
##for j in range(4,0,-1):
##    print(" "*(n-j)+"*"*j)
   


####pattern - pyramid
##n=7
##for i in range(1,n+1):
##    print("*"*i)
##for j in range(6,0,-1):
##    print("*"*j)



##for loop with strings:
##tech="python"
##for i in tech:
##       print(i)




##stmnt="python is a EASY language"
####print only the vowels
##vowels="aeiou"
##for i in stmnt:
##    if i.lower() in vowels:
##          print(i)



##stmt=input("enter a statement:")
##char=input("enter a character:")
##for i in stmt:
##    if (ord(i.lower())<ord(char.lower())):
##         
##        print(i)




##user=input("enter a float number:")
##task pending


##
##stmt = "python and machine learning"
##char = "n"
##ind = -1
##for i in stmt:
##    if i == char:
##         ind = stmt.index(char , ind+1)
##         print(ind)
##


##
##x=int(input("enter a number"))
##char=input("enter a character:")
##for x in range(ord(char), ord(char)+x):
##       print(str[x],end="")
##       print()        
##

##---------------------------------------
##i=0
##while i <= 10:
##    if i == 5:
##        break
##    print(i)
##    i=i+1
##

##---------------------------------------
##x=100
##y=5
##for i in range(5,100,5):
##  print(i, end=" ")
##---------------------------------------

##x=100
##y=5
##for i in range(1,100):
##   if i%y == 0:
##        print(i,end=" ")

##---------------------------------------

##x=100
##y=5
##for i in range(1,100):
##     if i%y != 0:
##          continue
##     else:
##      print(i, end=" ")
##   
##---------------------------------------
##
##x=5
##y=5
##while (x<100 and x%y == 0):
##    print(x,end=" ")
##    x=x+5

##---------------------------------------
##x=5
##y=5
##while (x<100 and x%y == 0):
##     if x == 5:
##         continue
##     print(x,end=" ")
##     x=x+5


##------------------------------------------
## ---------------- lists -----------------
##
##ll = [[[[[[[[[[10]]]]]]]]]]
##print(ll[0][0][0][0][0][0][0][0][0][0])
##
##l1=[10,20,30,40,50,60,"hello",78.9,"hiii"]
##del l1[7]
##print(l1)

##
####---------------------
##l1=[21,3,56,4,5,6,7,87,8,7,5,32,5,3,354,56,7,6,21]
##uni=[]
##for i in l1:
##    if (i not in uni):
##         uni.append(i)
##print(uni)
        
##
#### -------------------------
##l1=[21,[3,56,4],"python","hyd",[87,8,7],5,32,[5,3,354],21]
####----------unpack the lists
##l2=[]
##for i in l1:
##     if type(i) is int or type(i) is str:
##           l2.append(i)
##     else:
##          for j in i:
##               l2.append(j)
##print(l2)
###-----------------------need to practice:


##l1=[21,[3,56,4],"python","hyd",[87,8,7],5,32,[5,3,354],21]
##l2=[]
##l3=[]
##for i in l1:
##     if type(i) is int:
##         l2.append(i)
##     if type(i) is list:
##         for j in i:
##             if type(j) is int:
##                  l2.append(j)
##             else:
##                l3.append(j)
##     else:
##         l3.append(i)
##print(l2)
##print(l3)
## ------------------------ look into it once again


##l1=[21,3,56,4,"python","hyd",87,8,5,32,5,3,354,21]
##nums=[3,5,0,2,7]
##op=[]
##for i in nums:
##     op.append(l1[i])
##print(op)
##--------------look into it once again

##
##snum=12
##endnum=15
##x1=[]
##x2=0
##for i in range(snum,endnum+1):
##      for j in range(1,i+1):
##           if (i%j==0):
##               x1.append(j)
##               x2=len(x1)
##      if x2 > 2:
##        print(x1,"composite")
##        x1.clear()
##      else:
##        print(x1,"prime")
##        x1.clear()

##------------------------------------------------
##a= int(input("enter a number:"))
##x1=[]
##x2=[]
##x3=[]
##x4=[]
##
##for i in range(1,a+1):
##      x1.append(i)
##print(x1)
##for i in range(2,a+1):
##      if i%2 == 0:
##         x2.append(i)
##print(x2)
##for i in range(1,a+1):
##      x3.append(i**2)
##print(x3)
##for i in range(2,a+1):
##      if i%2==0:
##          x4.append(i**2)
##print(x4)
      
##
##stmt = "python is an easy language"
##x1 = [i for i in stmt.split()  if len(i)>3]
##print(x1)


##
##stmt="pyhton is an easy language"
##chars=[ch for ch in stmt if ord(ch)>ord('m')]
##print(chars)
##
##nums=([1,2,3,4],[10,20,30])
##num1=()
##for i in nums:
##    if type(nums(i)) == 'list':
##        nums(i)=tuple(nums(i))
##print(nums)

##
##nums=([1,2,3,4],[10,20,30])
##nums=list(nums)
##for i in range(len(nums)):
##    nums.insert(i,tuple(nums[i]))
##    nums.pop()
##print(tuple(nums))

##t1=(1,2,13,(4,3),565,(67,8,9),3,0,[32,4],5,6)
##t2=()
##for i in t1:
##    if type(i) is tuple or type(i) is list:
##        for j in i:
##            t2.append(i)
##    else:
##           t2.append(i)
##print(tuple(t2))
##        

##
##num1 = int( input("enter the number"))
##num2 = int(input("enter the number"))
##print(num1)
##print(num2)
##num1=num1^num2
##num2=num1^num2
##num1=num1^num2
##print(num1)
##print(num2)

##x=int(input("enter a number"))
##d={}
##for i in range(x+1):
##    dict[i]=i**2
##print(d)
##
##
##num = input("enter a number")
##file = open('chars.txt', 'a')
##file.write(num)
##file.close


##TASK ON FILES:  also include password validation - 1 uppercase 1 lowercase 1 special symbol and length should be 8

def checkname(name):
    users = []
    fr = open("demo.txt","r")
    data = fr.readlines()
    for i in data:
        users.append((i.split("-")[0]).rstrip(" "))
        print(fr.read())
    if name in users:
             return 1
    else:
            return 0
def writename():
    usr = input(" enter the username:")
    psw = input(" enter the password:")
checkname("user")


            
    











































   



