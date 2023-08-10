import pprint

ls =[[i*10+j for j in range(1,11)]for i in range(10)] 
pprint.pprint(ls)

print()
#1
ls =[[i*10+j for j in range(1,11)][::-1]for i in range(10)][::-1] 
pprint.pprint(ls)

print()
#2
