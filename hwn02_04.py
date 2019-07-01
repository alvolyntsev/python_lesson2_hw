import random
i=0
lst1=[]
lst2=[]
lst3=[]
for i in range(10):
    lst1.append(random.randint(-100,100))
    
print(lst1)
for i1 in range(len(lst1)):
    for itm in lst1:
         if itm!=lst1[i1]:
              lst3.append(itm)
lst2=lst2+lst3
print('lst2=', lst2)
print('lst3=', lst3)