a=int(input("enter a starting number:"))
b=int(input("enter ending number:"))
 for i in range(a,b+1):
    if i%2 == 0:
        print(i,"is even number")
    else:
        print(i,"is odd number")
