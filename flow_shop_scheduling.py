m2=[]
m1=[]
n=int(input("how many jobs:"))
print("enter time for machine 1:")
for i in range(n):
    m1.append(int(input()))
print("enter time for machine 2:")
for i in range(n):
    m2.append(int(input()))
a=sorted((e,i,1) for i,e in enumerate(m1))
b=sorted((e,i,2)for i,e in enumerate(m2))
c=sorted(a+b)
seq=[0]*n
q=0
p=0
for i in range(n):
    i=0
    m=c[i]
    if(m[2]==1):
        seq[p]=m[1]
        p=p+1
        c.remove(c[i])
        for l in c:
            no=l[1]
            if(m[1]==no):
                c.remove(l)
    elif(m[2]==2):
        seq[n-1-q]=m[1]
        q=q+1
        c.remove(c[i])
        for l in c:
            no=l[1]
            if(m[1]==no):
                c.remove(l)
        

'''q+=1
    else:
        seq[n-1-i]=m[1]'''
print(seq)
'''for i in range(n):
    if(a[i]<=b[i]):
        seq[i]=i
        seq[i+1]=i
    else:
        seq[n-1-i]=i
print(seq)'''
p=0
t1=[]
t2=[]

for i in seq:
    p=p+m1[i]
    t1.append(p)
k=1
l=seq[0]

t2.append(t1[0]+m2[l])
p=t2[0]
for i in seq[1:n]:
    '''if(t1[k]>p):
        t2.append(p)
        p=t1[k]'''
    if(t1[k]>p):
        p=t1[k]
        p=p+m2[i]
        t2.append(p)
    else:
        p=p+m2[i]
        t2.append(p)
    k=k+1
print("make span:",t2[n-1])
print(t1)
print(t2)
