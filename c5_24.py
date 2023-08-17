def eat(breakfast,lunch='ラーメン',dinner='カレー'):
    print(f'朝は{breakfast}をたべました')
    print(f'昼は{lunch}をたべました')
    print(f'夜は{dinner}をたべました')

print('8月1日')
eat(breakfast='納豆ご飯',dinner='カレーうどん')
print('8月2日')
eat(dinner='カレーうどん',breakfast='納豆ご飯')
print('8月3日')
eat('納豆ご飯',dinner='カレーうどん')

