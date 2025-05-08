cook_book = {}
list_with_ingedients = []

with open('recipes.txt', 'r', encoding = 'utf-8') as file:

    for line in file:
        dict_ingred = {}

        if not line.strip().isdigit() and '|' not in line.strip() and line.strip() != '':       #Проверка на то, что строка является название блюда
            name_eat = line.strip()
            cook_book[name_eat] = list_with_ingedients

        elif line.strip().isdigit():        #Проверка на то что строка - цифра, ее вообще никак не задействуем
            pass

        elif '|' in line.strip():       #Проверка на то, что это строка с ингредиентами
            list_with_ingedients_add = line.strip().split(' | ')
            dict_ingred['ingredient_name'] = list_with_ingedients_add[0]
            dict_ingred['quantity'] = int(list_with_ingedients_add[1])
            dict_ingred['measure'] = list_with_ingedients_add[2]
            list_with_ingedients.append(dict_ingred)

        else:       #Единственный в нашем случае вариант - пустая строка, значит нужно сбросить список, т.к. начнется новое блюдо
            list_with_ingedients = []

print(cook_book)