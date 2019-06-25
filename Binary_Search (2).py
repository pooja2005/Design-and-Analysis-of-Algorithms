def recur(k,a,low,high):
 if(low==high and k!=a[low]):
  print("the element is not in the list")
 else:
  if(high>=low):
   mid=int((low+high)/2)
   if(k==a[mid]):
        print("the element is present in the list")
        exit(0)
   else:
       
        if(k>a[mid]):
            low=mid+1
            print(low)
            recur(k,a,low,high)
        else:
            high=mid-1
            print(high)
            recur(k,a,low,high)
  else:
      print("the element is not in the list")
  
    



n=int(input("enter how many no.s:"))
k=int(input("enter key to be searched:"))
a=[]
low=0
high=n-1
print("enter numbers:")
for i in range(0,n):
    a.append(int(input()))

recur(k,a,low,high)
