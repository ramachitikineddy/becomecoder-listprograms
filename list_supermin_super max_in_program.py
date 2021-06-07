def reverse(num):
    rev=0
    while num:
        r=num%10
        num=num//10
        rev=rev*10+r
    return rev
def findmin(n,data):
    s=min(data)
    p=max(data)
    #r=int(str(s)[::-1])
    r=reverse(s)
    t=reverse(p)
    for i in range(n):
        if data[i]==s:
            data[i]=r
        if data[i]==p:
            data[i]=t
    s=min(data)
    p=max(data)
    return s==r,p==t
n=int(input())
data=list(map(int,input().split()))
minval=findmin(n,data)
print(*minval)

"""

5
23 45 67 21 32
True True
"""
