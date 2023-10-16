s = 0
n = input("n: ")
n= int(n)
for i in range(1, int((n/2)+1)):
    if n%i == 0:
        s += i

if s==n: print("perfect")
else: print ("not perfect")
