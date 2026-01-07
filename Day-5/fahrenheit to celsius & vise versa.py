choice=int(input("enter 1 for celsius->fahrenheit, 2 for fahrenheit->celsius:"))
if choice==1:
    c=float(input("enter temperature in celsius"))
    f=(c*9/5)+32
    print("temperature in fahrenheit=",f)
elif choice==2:
    f=float(input("enter temperature in fahrenheit:"))
    c=(f-32)*5/9
    print("temperature in celsius=",c)
else:
    print("invalid choice!")