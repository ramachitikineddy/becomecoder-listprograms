def search(n,data,s):
    c=0
    for i in range(n):
        if data[i]==s:
            c+=1
        if c==2:
            return i+1
    else:
        return False
n=int(input())
data=list(map(int,input().split()))
s=int(input())
print(search(n,data,s))
        
