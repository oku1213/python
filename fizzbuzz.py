for n in range(1,21):
    if n % 15 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)
        
#文字列を配列に入れる
msg = 'hello'
ls = list(msg)
print(ls) #'h','e','l','l','o'

word = input('英単語>>')
ls = list(word)
if len(word) == len(set(ls)):
    print('同じアルファベットは含まれていない')
else:
    print('同じアルファベットが含まれている')
