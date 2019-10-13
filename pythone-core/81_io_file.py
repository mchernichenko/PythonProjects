"""
1) Запись в файл
   fileobj = open(filename, mode), где  mode:
   r - чтение
   x - запись, если новый, то будет создан
   x - запись только в новый файл
   a - добавить в конец
   вторая буква в mode: t, b - текстовый файл или бинарный

2) Чтение из файла: read, readline, readlines

3) автоматическое закрытие файлов c помощью менеджера контекста
   with выражение as переменная:

4) смещение указателя в открытом файле:
    tell() - текущеее смещение
    seek(offset, origin) - смещение указателя в байтах относительно origin

"""

# == 1. Запись в файл: write, print

poema = 'There was a young lady named Bright,\n' \
        'Whose speed was far faster than light;\n' \
        'She started one day\n' \
        'In a relative way,\n' \
        'And returned on the previous night.'

fout = open('test_file_name', 'wt')  # открыть текстовый файл на запись
fout.write(poema)  # запись в файл
print(poema, file=fout, sep='', end='')  # альтернативный способ записи в файл, разница в том, что по умолчанию print добавляет \n в конеце файла и использует пробле как разделитель
fout.close()

# если данный файла нельзя перезаписывать
try:
    fout = open('test_file_name', 'xt')
    fout.write('stomp stomp stomp')
except FileExistsError:
    print(' "file_name" already exists!. That was a close one.')

# == 2. Чтение из файла: read, readline, readlines

fin = open('test_file_name', 'rt' )
poema = fin.read()  # чтение файла ПОЛНОСТЬЮ, но если файл большой, то может не хватить памяти!
print('Размер файла (Байт): ', len(poema))
fin.close()
#---------------------------------------
poem = ''
fin = open('test_file_name', 'rt' )
chunk = 100
while True:
    fragment = fin.read(chunk)  # чтение по 100 байт
    if not fragment:
        break
    poem += fragment

print('Размер файла (Байт): ', len(poem))
fin.close()
#---------------------------------------
poem = ''
fin = open('test_file_name', 'rt' )
while True:
    line = fin.readline()  # построчное чтение
    if not line:
        break
    poem += line

print('Размер файла (Байт): ', len(poem))
fin.close()
#---------------------------------------
poem = ''
fin = open('test_file_name', 'rt' )
for line in fin: # построчное чтение через итератор
    poem += line

print('Размер файла (Байт): ', len(poem))
fin.close()
#---------------------------------------
fin = open('test_file_name', 'rt' )
lines = fin.readlines()
fin.close()
for line in lines:
    print(line, end='')  #  т.к. в исходном файле переносы уже есть

# == 3. автоматическое закрытие файлов c помощью менеджера контекста
with open('test_file_name', 'wt') as fout: # менеджер контекста для очистки обектов
    fout.write(poema) # как только блок кода под менедженом завершится, автоматически вызовется fout.close

# == 4. смещение указателя в открытом файле:
bdata = bytes(range(0, 256))  # bytes принимает список чисел от 0 до 255 и возвращает байты, получающиеся применением функции chr
print(bdata)  # взять байт, перевести его в 10-ю систему и напечатать код символа с этим кодом

with open('test_bfile', 'wb') as fout:
    fout.write(bdata)

fin = open('test_bfile', 'rb')
fin.seek(65)  # смещаем указатель на 65 байт с начала
fin.seek(3, 1)  # смещаем указатель на 3 байт с текущей позиции
fin.seek(-70, 2)  # смещаем указатель на 70 байт с конца
print('Вывод данных с текущей позиции указателя: ', fin.read())