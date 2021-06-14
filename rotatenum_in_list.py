def reverse(arr,l,h):
    while(l<h):
        arr[l],arr[h]=arr[h],arr[l]
        l+=1
        h-=1
def rotatelist(n,arr,r):
    r=r%n
    reverse(arr,0,r-1)
    reverse(arr,r,n-1)
    reverse(arr,0,n-1)
n=int(input())
arr=list(map(int,input().split()))
r=int(input())
rotatelist(n,arr,r)
print(*arr)
    
