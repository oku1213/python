import random

# 空っぽのリスト変数名dicesを作成する
# 何回振るかを聞きその結果を変数numに代入

num = int(input('何回振る?>>'))
dices = list()
for dice in range(num):
    n = random.randint(1,6)
    dices.append(n)
print(dices)
print(f'合計は{sum(dices)}でした')
