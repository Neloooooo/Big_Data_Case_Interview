import random

num = [random.randint(0, 100) for i in range(20)]
print(num)

j = num[::2]
o = num[1::2]
o.sort(reverse=True)

print(j)
print(o)
