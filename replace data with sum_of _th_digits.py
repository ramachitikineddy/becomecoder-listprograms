# sum of the given each number of the data with no return value
def sum(n):
    s=0
    while n:
        r=n%10
        n=n//10
        s=s+r
    return s
def sumofdigits(n,data):
    for i in range(len(data)):
        data[i]=sum(data[i])
    return data

n=int(input())
data=list(map(int,input().split()))
sumofdigits(n,data)
print(*data)
