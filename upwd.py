import random
fr = open("upwd.txt","a+")
usr = input("enter username:")
users=[]

for x in fr:
    users.append(x)
if usr is users:
    print("user already exists!!!!")
else:
    n = input("enter your password length:")
    pwd = input("enter your password:")
    fr.write(usr + "    -    " + pwd+'\n')
