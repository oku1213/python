import random
"""
ls = [random.randint(0,100) for i in range(100)]
print(ls)
ls.sort(reverse=True)
print(ls)
print(ls[:10])
"""
#1行でやるなら
ls=sorted([random.randint(0,100) for i in range(100)],reverse=True)[:10]
print(ls)
