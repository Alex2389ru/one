a = int(input('Введите число'))
b = 100
c = 50

if a == 100:
    print('Число равное 100')
elif a > b:
    print('Число больше 100')
elif a < b and a > c:
    print('Число больше 50, но меньше 100')    
elif a < c:
    print('Число меньше 50') 
else:
    print('Число равное 50')          

