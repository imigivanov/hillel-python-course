# 1)Дан массив из словарей 

data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]


# 1.1) отсортировать массив из словарей по значению ключа ‘age' 
def sort_by_age(array):
    return sorted(array, key=lambda key_to_sort_by: key_to_sort_by['age'])


print(sort_by_age(data))

"""
1.2) сгруппировать данные по значению ключа 'city' 
вывод должен быть такого вида :
result = {
   'Kiev': [
      {'name': 'Viktor', 'age': 30 },
      {'name': 'Andrey', 'age': 34}],

   'Dnepr': [ {'name': 'Maksim', 'age': 20 },
              {'name': 'Artem', 'age': 50}],
   'Lviv': [ {'name': 'Vladimir', 'age': 32 },
             {'name': 'Dmitriy', 'age': 21}]
}
"""


def group_by_city(array):
    result = {}
    for element in array:
        if element['city'] not in result:
            result[element['city']] = []
        result[element['city']].append(element)
    return result


group_by_city(data)
