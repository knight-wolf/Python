print("1.arithmetic \n2.comparision \n3.logical")
a=int(input("enter a category:"))
if a==1:
    print("1.add\n2.sub\n3.mul\n4.div")
    b=int(input("enter a operation:"))
    if b==1:
        x=int(input("enter a number:"))
        y=int(input("enter a number:"))
        print(x+y)
    elif b==2:
        x=int(input("enter a number:"))
        y=int(input("enter a number:"))
        print(x-y)
    elif b==3:   
        x=int(input("enter a number:"))
        y=int(input("enter a number:"))
        print(x*y)
    elif b==4:
         x=int(input("enter a number:"))
         y=int(input("enter a number:"))
         print(x/y)
    else:
          print("please enter option correctly!!")
if a==2:
    print("1.>\n2.<\n3.>=\n4.<=")
    b=int(input("enter a operation:"))
    if b==1:
        x=int(input("enter a number:"))
        y=int(input("enter a number:"))
        print(x>y)
    elif b==2:
        x=int(input("enter a number:"))
        y=int(input("enter a number:"))
        print(x<y)
    elif b==3:   
        x=int(input("enter a number:"))
        y=int(input("enter a number:"))
        print(x>=y)
    elif b==4:
         x=int(input("enter a number:"))
         y=int(input("enter a number:"))
         print(x<=y)
    else:
          print("please enter option correctly!!")
if a==3:
    print("1.and\n2.or\n")
    b=int(input("enter a operation:"))
    if b==1:
        x=int(input("enter a number:"))
        y=int(input("enter a number:"))
        print(x and y)
    elif b==2:
        x=int(input("enter a number:"))
        y=int(input("enter a number:"))
        print(x or y)
    else:
        print("enter option correctly!!")
        


          
          
