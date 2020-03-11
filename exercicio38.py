print('-='* 20)
print('Forma um')
print('-='* 20)

for count in range(1, 51):
    if count % 2 == 0:
        print('{} é par'.format(count))
    else:
        print('{} não é par'.format(count))

print('-='* 20)
print('Forma dois')
print('-='* 20)

for count in range(0, 51, 2):
    print('{} é par'.format(count))
    