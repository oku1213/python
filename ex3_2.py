initial = 'k'
if initial == 'k':
    print('OK1')

point = 82
if 80 <= point < 256:
    print('OK2')

bmi = 24
if bmi < 20 or bmi > 25:
    print('OK3')

year = 2023
if year % 4 == 0:
    print('OK4')

day = 23
#if not (day ==28 and day == 30 and day == 31):
# if day not in[28,30,31]:
if not(day in[28,30,31]):
    print('OK5')
