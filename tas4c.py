hh = int(input("time in hours format:"))
mm = int(input("time in min format:"))
ss = int(input("time in sec formag:"))
f = input("format")
print("%d:%d:%d"%(hh,mm,ss))
if f =="am":
    print("%d:%d:%d"%(hh,mm,ss))
else:
    print("%d:%d:%d"%(hh+12,mm,ss))
         
