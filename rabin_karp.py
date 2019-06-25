def func(j,shift):
    count=0
    for i in range(j,j+3):
        if(pat[count]==s[i]):
            count+=1
        if(count==len(pat)):
            break
    if(count==len(pat)):
            print("pattern matched at:",j+1,"position and shist is:",shift)
    '''if(count!=len(pat) and j==l-len(pat)-1):
        print("not present")'''
        





s=[]
pat=[]
for i in range(0,9):
 s.append(int(input("enter string:")))
for i in range(0,3):
 pat.append(int(input("enter pattern:")))
q=3
shift=0
l=len(s)
m=len(pat)
h=0
sm=0
for i in range(0,m):
    h=h+(pat[i])*(10**(m-1))
    sm=sm+(s[i])*(10**(m-1))
    m=m-1
for i in range(0,l-len(pat)):
    if((sm%3)==(h%3)):
        func(i,shift)
    sm=(sm-(s[i]*(100)))*10+s[len(pat)+i]
    shift+=1
if(i ==l-len(pat)):
    print("not present")
    
