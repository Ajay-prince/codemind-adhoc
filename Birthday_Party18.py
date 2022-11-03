n1=list(map(int,input().split()))

n2=[]
for i in n1:
    if i not in n2:
        n2.append(i)
for k in n2:
    print(3*k)