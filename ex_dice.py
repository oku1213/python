import random

print('サイコロ振ったよ')
n1 = random.randint(1,6)
n2 = random.randint(1,6)
print(f'1回目:{n1}')
print(f'2回目:{n2}')
if n1 == n2:
    print('2回目は1回目と同じ目です')
elif n2 < n1:
    print(f'2回目は1回目より{n1-n2}小さいです')
else:
    print(f'2回目は1回目より{n2-n1}大きいです')
