# desc: print all powers less than k of a given integer n
#input: n- integer whose powers we need to print
#input: k- n's powers need to be less than this
#output: aux- all powers of n less than k

n=int (input ("n= "))
k=int (input ("k= "))
aux= n;
v=bool=True

print (1) #any n to the power 0

if(n>1):
    while v==True:
        if(aux<k):
            print (aux)
            aux=aux*n
        else:
            v=False
        
