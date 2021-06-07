def issorted_data(n,data):
    s=data.copy()
    rs=data.copy()
    s.sort()
    rs.sort(reverse=True)
    if s==data or rs==data:
        return True
    return False
        
n=int(input())
data=list(map(int,input().split()))
print(issorted_data(n,data))
