def sumDigits(n):
    if n==0 or n==1:
        return n
    else:   
        return n%10+sumDigits(n//10)
print(sumDigits(984))
         