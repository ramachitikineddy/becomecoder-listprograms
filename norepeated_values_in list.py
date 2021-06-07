def norepeated_value(n,data):
    d=[]
    for i in data:
        if i not in d:
            d.append(i)
    return d
n=int(input())
data=list(map(int,input().split()))
rev=norepeated_value(n,data)
print(*rev)
        
