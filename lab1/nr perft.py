s = 0
n = input()
n= int(n)
for i in range(1, n/2):
    if n%i == 0:
        s += i
        print(s)

if s==n:
    print("perfect")
else: print ("not perfect")
