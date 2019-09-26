##-------------tuple tasks
##---  1 ---------
##x=(24,56,79.6,"hello","good",5,6,[4,5])
##print(type(x))
##print(x)

##---   2 ----
##x=(24,56,79.6,"hello","good",5,6,[4,5])
##for i in x:
##    print(x.index(i),i)

##---  3 ----
##x=("hello","how","are", "you")
##if type(x)=='tuple':
##   

##----------

##CONTROL FLOW PROGRAMS
#1
##n = int(input("enter a number:"))
##for i in range(1,n+1):
##    if (i%3 == 0 or i%5 == 0):
##        continue
##    else:
##            print(i)


#2
##n = int(input("enter a number:"))
##for i in range(1,n+1):
##    if i%2 == 0:
##       i = i**2
##       print(i)
##    

#3
##n = 100
##for i in range(1,n+1):
##    if  i%7 == 0:
##        print(i)
##

#4
##n=input("enter the string")
##for i in n:
##       if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
##           print(i)
##---------------------------------------------------------------------------
##STRING
##1
##n = input("enter a string")
##outputstring=""
##for i in range(0,len(n),2):
##       outputstring+=n[i]
##print(outputstring)

##2
##n = input("enter a string")
##str = ''
##for i in range(len(n)-1,-1,-1):
##       str += n[i]
##print(str)      

##3
##string = input("enter a string : ")
##print()
##op = ''
##char = string[2]
##string = list(string)
##for z in range(len(string)):
##       if string[z] == char:
##              string[z] = '@'
##for z in string:
##       op += z
##print(op)
##print()
##

##4
##n = "python python python is a language"
##m = n.replace("python","java",2)
##print(m)
####

##5
##num1 = int( input("enter the number"))
##num2 = int(input("enter the number"))
##num1=num1+num2
##num2=num1-num2
##num1=num1-num2
##print(num1)
##print(num2)
##


#LOOOPING###---------
##1
##n = int(input())
##sum = 0
##temp = n
##while temp > 0:
##   digit = temp % 10
##   sum += digit ** 3
##   temp //= 10
##
##if n == sum:
##   print(n,"is an Armstrong number")
##else:
##   print(n,"is not an Armstrong number")
##


##2
def recur_fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))  

nterms = int(input("How many terms? "))  

if nterms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(recur_fibo(i)) 





##------ 4 -------









##------- 5 -------
x1=[1,2,3,4,5,(6,7)]
count=0
for i in x1:
    if type(i) is 'int' or type(i) is 'str':
          count1 = count+1
    elif type(i) is 'float':
          count1 = count+1
    else:
        break
print("the count is:", count1)
         






















             
        
