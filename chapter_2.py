#appending/adding items to a list
b=[]
b.append(4)
b.append(5)
b.append(True)
b.append("hello")
print(b)

# combining lists
c=[7,True]
d=[8,'Python']
print(c+d)
print(2*d)

# remove items from a list
b.remove(5)
print(b)

# using lists and for loops
a=[12,'apple',True,0.25]
for thing in a:
    print(thing)

for thing in a:
    print(thing, end='')

for thing in a:
    print(thing, end=',')

# Accessing individual items in a list
name_list=['Abe','Bob','Chloe','Daphne']
score_list=[55,63,72,54]
print(name_list[0],score_list[0])

n=2
print(name_list[n],score_list[n+1])

for i in range(4):
    print(name_list[i],score_list[i])

# accessing index value with enumerate()
for i, name in enumerate(name_list):
    print(name, "has index", i)

#access a range of list items
mylist=[1,2,3,4,5,6,7]

# finding the index of an item
c=[1,2,3,'hello']
print(c.index(1))
print(c.index(3))

# string indices
d = 'python'
print(len(d))
print(d[0])
print(d[:5])

# summations
running_sum=0
for i in range(10):
    running_sum+=3
print(running_sum)

def my_sum(num):
    running_sum=0
    for i in range(1,num+1):
        running_sum+=i
    return running_sum

def my_sum_2(num):
    running_sum=0
    for i in eange(num+1):
        running_sum += i**2 + 1
    return running_sum