
#Вначале запускаем все файлы, для того чтобы произвести подсчет строк в каждом
with open('1.txt', encoding = 'utf-8') as f_1, open('2.txt', encoding = 'utf-8') as f_2, open('3.txt', encoding = 'utf-8') as f_3:
    i_1 = i_2 = i_3 = 0     #переменные в которых хранится кол-во строк в файлах

    for f in f_1:
        i_1 += 1
    

    for f in f_2:
        i_2 += 1
    

    for f in f_3:
        i_3 += 1

k = 3       #Счетчик для завершения цикла, т.к. файла 3, чтобы записать из каждого

with open('task_3.txt', 'w') as f:      #Это специальный блок кода, который просто очищает все из файла task_3, чтобы не записывать сотни строк одно и тоже 
    f.write('')
    

while k > 0:

    if i_1 == min(i_1, i_2, i_3):       #Ищем наименьшее кол-во строк

        with open('1.txt', encoding = 'utf-8') as read_file, open('task_3.txt', 'a', encoding = 'utf-8') as write_file:
            write_file.write('1.txt\n')     #Запись имени файла
            write_file.write(str(i_1) + '\n')       #Запись кол-ва строк
            write_file.write(read_file.read())      #Записываем в итоговый файл копию файла 1
            write_file.write('\n')      
            k -= 1      #Уменьшаем счетчик
            i_1 += max(i_1, i_2, i_3)       #Чтобы теперь i_1 точно не было минимальным, прибавляем к нему максимальное из двух оставшихся

    if i_2 == min(i_1, i_2, i_3):       #Все по аналогии с i_1

        with open('2.txt', encoding = 'utf-8') as read_file, open('task_3.txt', 'a', encoding = 'utf-8') as write_file:
            write_file.write('2.txt\n')
            write_file.write(str(i_2) + '\n')
            write_file.write(read_file.read())
            write_file.write('\n')
            k -= 1
            i_2 += max(i_1, i_2, i_3)

    if i_3 == min(i_1, i_2, i_3):       #Все по аналогии с i_1

        with open('3.txt', encoding = 'utf-8') as read_file, open('task_3.txt', 'a', encoding = 'utf-8') as write_file:
            write_file.write('3.txt\n')
            write_file.write(str(i_3) + '\n')
            write_file.write(read_file.read())
            write_file.write('\n')
            k -= 1
            i_3 += max(i_1, i_2, i_3)