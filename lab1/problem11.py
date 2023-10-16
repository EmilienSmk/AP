#desc generate all prime nubmers having n difgits with the prop that all its prefixes are also prime
#input: n-the number of digits
#Output: prime numbers whose prefixes are also prime
n=int(input("n= "))

aux=n
d=1
v=True

while(aux!=0):
    d=d*10
    aux=aux-1

for i in range(2, d):
    v= True
    for j in range(2, i):
        if (i % j) == 0:
            v=False   
    if(v==True):
        x=i
        aux=0
        contor=0
        while(x!=0):
            x=int (x/10)
            contor =contor + 1

        aux=i
        vf=True

        while(aux!=0): 
            for k in range(2, aux):
                if (int (aux % k) == 0):
                    vf=False
                    
            aux=aux//10
            if aux==1:
                vf=False 

        if vf==True and n==contor:
            print(i)
            
