import random

x = [random.randint(1, 20) for i in range(50)]
r = dict()

for i in x:
    r[i] = r.get(i, 0) + 1  # get()方法可以返回指定键的值，如果该键不存在的话，返回默认值

for k, v in r.items():
    print(k, v)
