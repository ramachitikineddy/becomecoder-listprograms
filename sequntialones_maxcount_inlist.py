def maxsort(n,data):
    count=0
    c=0
    for i in range(n-1):
        if data[i]==1:
            c+=1
        else:
            if count<c:
                count=c
            c=0
    return max(c,count)
n=int(input())
data=list(map(int,input().split()))
print(maxsort(n,data))
