#--------------list functions
#l1=[23,3,4,50,6,40,34.6,77,1]
#print(l1[7]) #---it will return the value at that index

#print(l1.index(4)) #----whereas this will return the index of the value mentioned
 
#-----deleting element from the list by mentioning index 
#del l1[5]
#print(l1)


#----deleting element without mentioning the index
#del l1[l1.index(77)]
#print(l1)

#----concatenation of two lists

#l3=l1+l2
#print(l3)
#l3.pop()
#print(l3)

#l1.sort()
#print(l1)
#l1.reverse()
#print(l1)
#d={1:10,2:20,3:40,5:20}
#print(d)

# x=5
# d={}
# for i in range(x+1):
#     d[i]=i**2
# # print(d)
# l1=[10,30,40,50]
# l2=[100,40,500,70]
# d={}
# if len(l1) == len(l2):
# 	 for i in range(len(l1)):
# 	 	d[l1[i]] = l2[i]
# else:
# 	print("unequal lengths of lists")
# print(d)
# stmt="python is easy"
# d={}
# ch=stmt.split()
# for i in ch:
# 	for j in i:

# print(ch)


# d={i:i**2 for i in range(10)}
# print(d)


# stmt="python is an easy programming language"
# d={word:len(word) for word in stmt.split() if len(word)>4}
# print(d)
# stmt="python is easy"
# ch=stmt.split()
# for i in ch:

# a=[(3,2),(7,4),(3,1)]
# a.sort()
# print(a)

# a=(1)
# print(type(a))
# a={'name':'ramesh','age':23}
# print(list(a.keys()))
# a={1:'a',2:'b',3:'c'}
# b={4:'d',5:'e'}
# a.update(b)
# print(a)
# a={1:5,2:8,3:10}
# print(a.pop(3),a)

# a={3,8,9}
# a.update([1,2,3])
# print(a)
##
##a=set([7,8,9])
##a.union([6,5])
##print(a)
##
##n=input("enter the string")
##for i in n:
##       if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
##           print(i)

n = input("enter a string")
outputstring=""
for i in range(0,len(n),2):
       outputstring+=n[i]
print(outputstring)







