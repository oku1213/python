import random
count = 0
while True:
    num = random.randint(1,9999)
    count += 1
    print(f'{count}:{num}')
    if num == 7777:
        break
print(f'{count}回目に7777がでました!')
