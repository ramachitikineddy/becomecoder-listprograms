def norepeated_value(n,data):
    data=list(set(data))
    data.sort()
    return data
n=int(input())
data=list(map(int,input().split()))
rev=norepeated_value(n,data)
print(*rev)
        
