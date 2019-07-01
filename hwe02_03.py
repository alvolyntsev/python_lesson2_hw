lst1=[88,6,77,96,3,85,6,5,9,64,1,99,4566,74,8,997]
lst2=[]
ind=0
for itm in lst1:
    if itm%2==0:
        lst2.append(itm/4)
    else:
        lst2.append(itm*2)
print('lst2=', lst2)