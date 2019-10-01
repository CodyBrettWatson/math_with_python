def factors(num):
    '''returns a list of the factors of num'''
    factor_list=[]
    for i in range(1,num+1):
        if num % i == 0:
            factor_list.append(i)
    return factor_list

print(factors(150))
print(factors(138))


def greatest_common_factor(a,b): 
    if (b == 0): 
         return a 
    return greatest_common_factor(b, a%b) 

print(greatest_common_factor(150,138))