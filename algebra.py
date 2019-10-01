def algebra(a,b,c,d):
    '''Solves equations of the form ax+b=cx+d in terms of x.
    Remember if there is not a coefficient value on one 
    side then that means the coefficent is 0'''
    return (d-b)/(a-c)
    '''This works because:
    ax+b=cx+d -> ax-cx=d-b -> x(a-c)=d-b -> x=(d-b)/(a-c)'''

print(algebra(1,2,3,4))
print(algebra(12,24,35,42))
print(algebra(2,5,0,13))