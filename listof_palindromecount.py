def palindrome(n):
    t=n
    rev=0
    while n:
        r=n%10
        n=n//10
        rev=rev*10+r
    return rev==t
def palindrome_count(n,data):
    pc=0
    for i in range(len(data)):
        if palindrome(data[i]):
            pc+=1
    return pc
n=int(input())
data=list(map(int,input().split()))
print(palindrome_count(n,data))

