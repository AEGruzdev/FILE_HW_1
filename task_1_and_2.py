from pprint import pprint

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

def get_shop_list_by_dishes(dishes, person_count):

    dict_with_ingresients = {}

    for elem in dishes:     #Запускаем перебор блюд из переданного в функцию списка

        for ingreds in cook_book[elem]:     #Перебор словарей с ингредиентами и количеством из cook_booka, ключом которых является как раз название блюда

            if ingreds['ingredient_name'] not in dict_with_ingresients:     # Условие, что в нашем словаре еще нет такого ключа (ингредиента)
                dict_with_ingresients[ingreds['ingredient_name']] = {'measure': ingreds['measure'], 'quantity': ingreds['quantity']*person_count}
  
            else:       #Если такой ингредиент уже есть, то мы только увеличиваем его количество 
                dict_with_ingresients[ingreds['ingredient_name']]['quantity'] += ingreds['ingredient_name']['quantity']

    return dict_with_ingresients



pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Фахитос'], 2))