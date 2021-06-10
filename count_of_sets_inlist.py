def maxsort(n,data):
    count=1
    c=1
    for i in range(n-1):
        if data[i]<data[i+1]:
            pass
        else:
            count+=1
    return count
n=int(input())
data=list(map(int,input().split()))
print(maxsort(n,data))
