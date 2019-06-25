def sg(a):
    l=a[0]
    for i in range(1,5):
        if(l<=a[i]):
            l=a[i]
    print("the largest no. is:",l)
    for i in range(1,5):
        if(l>=a[i]):
            l=a[i]
    print("the smallet no. is:",l)
def su(a):
    s=0
    for i in range(0,5):
        s=s+a[i]
    print("the sum of the numbers is:",s)
        
def avg(a):
    s=0
    for i in range(0,5):
        s=s+a[i]
    t=s/5
    print("the average of numbers is:",t)
    
def odd_ev(a):
    o=[]
    e=[]
    for i in range(0,5):
        l=a[i]
        
        if(l%2==0):
            e.append(l)
        else:
            o.append(l)
    print("the odd no.s are:",o)
    print("the even no.s are:",e)
def prime(a):
    p=[]
    h=0
    y=[]
    for i in range(0,5):
        l=a[i]
        for j in range(2,):
            if(l%j==0):
                y.append(l)
                h=1
                break
        if(h==0):
            p.append(l)
    print("the prime no are:",p)
    print("the non p no are:",y)


#n=int(input("enter how many numbers:"))

print("enter numbers:")
a=[]
for i in range(0,5):
    a.append(int(input()))

print("enter 1. to find smallest and greatest value:")
print("enter 2. to find sum of elements:")
print("enter 3. to find avgerage of elements")
print("enter 4. to find odd and even numbers")
print("enter 5. to find prime and non prime elements")
m=int(input("Select option from 1 to 5:"))
if(m==1):
    sg(a)
if(m==2):
    su(a)
if(m==3):
    avg(a)
if(m==4):
    odd_ev(a)
if(m==5):
    prime(a)

