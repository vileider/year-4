def f(n:int):
    c= 0
    iter = 0
    while n >= 0:
        iter += 1
        n= n-2
        c = c+n-2
    return c
abc= 1
print(f(6700))
#print(f(abc) >= f(abc-2))