''' def isPrime(n):
    d=2
    if n<2:
        return False

    while(d<n):
        if n%d==0 :
            return False
        d=d+1
    return True

def highestPrime(n):
    for i in range (n-1,1,-1):
        if(isPrime(i)):
            return i        

n=int (input("n= "))
print(highestPrime(n))



def sumDigits(n):
    sum=0
    while(n!=0):
        sum=sum+ int(n%10)
        n=n//10
    return sum

n=int (input("n= "))
print(sumDigits(n))


def count_even(lst):
    k=0
    for i in range (len(lst)):
        if i%2==0:
            k=k+1
    return k

lst=int (input("lst= "))
for i in range :
    print(count_even(lst))


def read_lst(lst):
    lst=[]
    n=int(input("size of list "))
    for i in range (0,n):
        elem=int(input("Element "+ str(i+1)+" "))
        lst.append(elem)
    return lst
lst=[]
lst=read_lst(lst)
print("Number of even numvers in the list is: ", count_even(lst))

 '''
'''
def min_list(lst)
    if lst=[]
        return None
    min=lst[0]
    for elm in lst
        if elm<min
            min=elm
    return min

'''
are_friends(n1,n2) #returns true/false
get_divisors(n) #returns list of divisors

def are_friends(n1,n2)
    new_lst2=[]
    l2=get_divisors(n2)
    l1=get_divisors(n1)
    if sum_list(l1)==n2 and sum_list(l2)==n1;
        return True
    return False
                               
def get_divisors(n)
    new_lst=[]
    for i in range (n//2+1)
        if n%i==0
        new_lst.append(i)
    return new_lst


    






