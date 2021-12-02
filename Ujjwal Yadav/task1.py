list = [18,20,8,16,4,10,12,3]
list.sort()
n= list[-2]
count = 0

while n!=0:
    if n%2==0:
        n/=2
        count+=1
    elif n%2!=0:
        n-=1    
        count+=1
print(count)