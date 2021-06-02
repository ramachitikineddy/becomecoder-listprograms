import math as m
def isprime(num):
    if num==1:
        return 0
    sq=int(m.sqrt(num))
    for j in range(2,sq+1):
        if num%j==0:
            return 0
    return 1
def findprimes(n,data):
    prime=[]
    nonprime=[]
    for i in data:
        if isprime(i):
            prime.append(i)
        else:
            nonprime.append(i)
    return prime,nonprime

n=int(input())
data=list(map(int,input().split()))
primes,np=findprimes(n,data)
print(*primes)
print(*np)
