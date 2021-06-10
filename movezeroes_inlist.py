
def movezeroes(n,data):
    for i in data:
        if i==0:
            data.remove(i)
            data.append(0)
    print(*data)
n=int(input())
data=list(map(int,input().split()))
print(movezeroes(n,data))
