#arithmetic operator
def value():
    a=int(input("enter a value"))
    b=int(input("enterr a value"))
    return a,b
s,su=value()
add=s+su
print("add",add)
s,su=value()
sub=s-su
print("sub",sub)
s,su=value()
mul=s*su
print("multi",mul)
s,su=value()
div=s/su
print("div",div)
s,su=value()
floor=s//su
print("floor division",floor)
s,ss=value()
exponent=s**ss
print("exponential",exponent)
#area of circle
import math
r=float(input("enter a radius"))
area=math.pi*r**2
print("area of circle",area)
#floating point is a number representaion which include both integer and fractional part
