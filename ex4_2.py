"""
count = 1
print('カレーを召し上がれ')
ans = 'y'
while ans == 'y':
    print(f'{count}皿のカレーを食べました')
    ans = input('おかわりはいかがですか？(y/n)>>')
    if ans == 'y':
        count +=1
    else:
        print('ごちそうさまでした')
"""

count = 0
print('カレーを召し上がれ')
while True:
    count += 1
    print(f'{count}皿のカレーを食べました')
    ans = input('おかわりはいかがですか？(y/n)>>')
    if ans == 'n':
        break
print('ごちそうさまでした')

