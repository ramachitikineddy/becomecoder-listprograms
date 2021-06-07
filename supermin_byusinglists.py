def rev(n):
    rev=0
    while n:
        r=n%10
        n=n//10
        rev=rev*10+r
    return rev
def reverse_of_digits(n,data):
    for i in range(len(data)):
        data[i]=revdigits(data[i])
    return data









def supermin(n,data):
    
    for i in range(len(data)):
        data[i]=rev.
