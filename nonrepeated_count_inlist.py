def norepeated_count(n,data):
    d=[]
    c=0
    for i in data:
        if i not in d:
            d.append(i)
    print(*d)
    for i in range(len(d)):
        if d[i]==data[i]:
            c+=1
    return c
n=int(input())
data=list(map(int,input().split()))
print(norepeated_count(n,data))
        
