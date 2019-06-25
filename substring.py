n=int(input("enter the size of string"))
a=[]
count=0
c=0
p=[]
print("enter string:")
for i in range(0,n):
    a.append(input())
l=int(input("enter the size of substring"))
print("enter substring")
m=[]
for i in range(0,l):
    m.append(input())
for i in range(0,n-l+1):
    count=0
    for j in range(0,l):
        if(a[i]!=m[j]):
            break;
        else:
            p.append(i+1)
            i=i+1
            count=count+1
    if(count==l):
        c=c+1
print("the no. of times substring appear in string is:",c)
s=len(p)
for i in range(0,s,l):
 print(p[i])
 
 
