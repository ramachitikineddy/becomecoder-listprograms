import math as m
def isprime(num):
    sq=int(m.sqrt(num))
    for j in range(2,sq+1):
        if num%j==0:
            return 0
    return 1
def prime_count(n,data):
    pc=0
    for i in data:
        if isprime(i):
            pc+=1
    return pc
    
n=int(input())
data=list(map(int,input().split()))
pc=prime_count(n,data)
print(pc)
