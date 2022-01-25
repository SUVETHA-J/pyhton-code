#4file extension
file=input("filename:")
extension=file.split(".")
print("extension of file:",str(extension[-1]))
#calculator
def get():
    a=int(input("entera value"))
    b=int(input("enter a value"))
    return a,b
a=int(input("enter 1)add,2)sub,3)multi,4)division"))
if(a==1):
    s,ss=get()
    add=s+ss
    print(add)
elif(a==2):
    s,ss=get()
    sub=s-ss
    print("sub",sub)
elif(a==3):
    s,ss=get()
    multi=s*ss
    print("multi",multi)
elif(a==4):
    s,ss=get()
    div=s/ss
    print("division",div)
elif(a>4 or a<=0):
    print("enter no from  to 4")

#descending order
s=[2,5,6,88,8,90]
s.sort(reverse=True)
print(s)
#create a set
#unorderd sequence
a={"curly brace","unordered","immutable"}
print(type(a))

#methods for dictionary
d=(1,2,3,4)
c=0
ss=dict.fromkeys(d,c)
print(ss)
car={"one":1,"two":2,"three":3}
c=car.copy()
print("copy into anoter",c)
c=car.get("one")
print(c)
car.pop("one")
print(car)
car.update({"four":4})
print("update",car)
s=car.values()
print("values",s)
s=car.keys()
print("keys",s)
s=car.clear()
print("clear",s)
