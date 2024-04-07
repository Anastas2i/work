import random
num=[]
for i in range(1,10):
    num.append(random.randint(1,10))
else:
     num[num.index(i)]=i**2
print(num)