n=int(input ("n= "))

oglindit=0
contor=0

while(n!=0):
    oglindit=oglindit*10+int(n%10)
    contor= contor + 1
    n= int (n/10)

print (oglindit)
print (contor)
