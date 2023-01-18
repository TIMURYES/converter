a = int(input('summani sumda kirgizing: '))
b = input('dollar\n rubl\n funt sterling\n valyutani tanlang: ')
if b == 'dollar':
    print(f'sizning pulingiz {a / 13000}-dollar')
elif b == 'rubl':
    print(f'sizning pulingiz {a / 164,43}-rubl')
elif b == 'funt sterling':
    print(f'sizning pulingiz {a / 14000}-funt sterling')
else:
    print('bizda bu valyuta yuq')
