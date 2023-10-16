'''desc: generate in ascending order the first n numbers from the set m.
if x belongs to M then 2x+1 and 3x+1 also belong to M
input: n- the number of numbers that we'll output
output: the list of the first n numbers that belong to M
'''

n=int(input("n= "))


M = [1]

i = 0

while i <= n:
    print ("i ",i)
    if M[i] in M:
        M.append(2*i+1)
        M.append(3*i+1)

M.sort()

for i in range (len(M)):
    print (M[i])
    
    

