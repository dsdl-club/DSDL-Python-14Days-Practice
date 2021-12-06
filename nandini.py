l=[18,20,8,16,4,10,12,3]
l.sort()
sec_lar=l[-2]
k=0
while sec_lar>0:
    if sec_lar%2==0:
        sec_lar=sec_lar/2
        k=k+1
    else:
        sec_lar=sec_lar-1
        k=k+1
print("Minimum number of steps to reduce number are ",k)