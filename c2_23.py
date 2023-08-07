scores ={'network':60,'database':80,'security':60}
members = ['松田','浅木','工藤']
print(scores)
print(members)
tp1 = tuple(members) #リストmembersを材料にタプルに生成
print(tp1)
ls1 = list(scores) #scoresのキーを集めたリストを生成
print(ls1)
st1 = set(scores.values()) #scoresのvalueを材料としてsetを生成
print(st1)

n1 = int('8')

codes = ['#ff0000','#00ff00','#0000ff']
colors = ['red','green','blue']
dict1 = dict(zip(codes,colors))
print(dict1)


