
list = [18,20,8,16,4,10,12,3]
x = sorted(list)
y = x[-2]
count = 0
while(y!=0):
    if(y%2==0):
        y=y/2
    else:
        y = y-1
    count +=1
print(count)