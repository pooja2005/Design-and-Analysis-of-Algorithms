'''a=input()
l=[]
for i in a:
    l.append(int(i))
print(len(l))
print(l)
    
l[0]=l[0]+2
print(l)'''
st=input("enter string:")
p=input("enter pattern:")
pat=[]
s=0
c=[]
c.append(0)
for i in p:
    pat.append(i)
j=0
for i in range(1,len(pat)):
    if(pat[j]==pat[i]):
        j=j+1
        s=s+1
        c.append(s)
    else:
        s=0
        if(j==0):
            c.append(0)
        else:
         while(j>0):
            j=c[j-1]
            if(pat[j]==pat[i]):
                c.append(j+1)
                break
            elif(j==0):
                c.append(0)
stn=[]
k=0
for i in st:
        stn.append(i)
for i in range(0,len(stn)):
            if(stn[i]==pat[k]):
             k+=1
             if(k==len(pat)):
               print("pattern found at:",i+2-len(pat),"position")
               k=c[k-1]
            else:
             k=c[k-1]
             if(stn[i]==pat[k]):
              k+=1
print("prefix matrix is:",c)
