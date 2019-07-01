import math
lst1=[88,6,77,96,-3,85,6,-5,9,64,1,99,4566,74,8,997]
lst2=[]
ind=0
for itm in lst1:
    if itm>0 and math.sqrt(itm)%1==0:
        lst2.append(int(math.sqrt(itm)))
print('lst2=', lst2)
