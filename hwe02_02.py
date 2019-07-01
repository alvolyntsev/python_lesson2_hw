lst1= [7,7,4,66,99,75,'gjh','fgg',75]
lst2=['hgv','jjy',75,66,4,'jjg','fgg','des',79]
print (len(lst1), len(lst2))
print(f'lst1 {lst1}   lst2 {lst2}')
i1=0
i2=0
while i1<len(lst1):
#    print('i1=',i1)
    while i2<len(lst2):
#        print('i2=',i2)
        if lst1[i1] == lst2[i2]:
            print('del',lst1[i1])
            lst1.remove(lst1[i1])
            i1-=1
        i2+=1
    i1+=1
    i2=0
print(f'result {lst1}')