def series(n):
    if n==1: #if we want to stop loop use base condition
        return n
    else:
        print(n)
        return series(n-1)
print(series(5))