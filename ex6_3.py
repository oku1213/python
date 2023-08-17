def welcome(u):
    print(f'ようこそ{u["name"]}さん')
    u['age']=u['age']+1
    print(f'あなたは来年{u["age"]}歳だから大吉です!')

username = input('名前を入力>>')
userage = int(input('年齢を入力>>'))
user = {'name':username, 'age':userage}
copied_user = user.copy()
welcome(copied_user)
print(f'{user["age"]}歳の{user["name"]}さん、またプレイしてくださいね')
