def total_marks(n,data):
    res=0
    for i in data:
        res+=i
    return res
n=int(input())
data=list(map(int,input().split()))
total=total_marks(n,data)
print(total)
