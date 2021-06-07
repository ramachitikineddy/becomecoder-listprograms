def second_largestnum(n,data):
    k=0
    sl=0
    
    for i in data:
        if i>k:
            sl=k
            k=i
    return sl
n=int(input())
data=list(map(int,input().split()))
print(second_largestnum(n,data))
        
