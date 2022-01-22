#comparision and assignment operators with 4 diff values in function
def get():
    a=int(input("enter a value"))
    b=int(input("enter a value"))
    return a,b
s,ss=get()#1
if(s>ss):
    s+=ss
    print("the value of s is :",s)
elif(s<ss):
    ss-=s
    print("the value of s is :",ss)
l,m=get()#2
if(l<=m):
    m**=l
    print("the value of l is :",m)
elif(l>=m):
    l*=m
    print("the value of l is:",l)
v,w=get()#3
if(v==w):
    v=w
    print(" both values are equal")
elif(v!=w):
    v^=w
    print("the value of v is:",v)
b,a=get()#4
b//=a
print("the value of b is",b)

