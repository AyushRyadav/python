p=int(input("enter principal amount:"))
r=int(input("enter rate of interest:"))
t=int(input("enter time(in years):"))
si=(p*r*t)/100
ci=p*((1+r/100)**t)-p
print("simple interest=",si)
print("compound interest=",ci)