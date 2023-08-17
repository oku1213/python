def eat(breakfast,lunch,dinner='カレー',desserts=()):
    print(f'朝は{breakfast}をたべました')
    print(f'昼は{lunch}をたべました')
    print(f'夜は{dinner}をたべました')

    for d in desserts:
        print(f'おやつに{d}を食べました')

print('8月1日')
eat('トースト','パスタ','カレー',('アイス','チョコ','パフェ'))

def sumof(*args):
    total=0
    for i in args:
        total += i
    return total
print(sumof()) #0
print(sumof(3,5)) #8
print(sumof(3,5,7)) #15
