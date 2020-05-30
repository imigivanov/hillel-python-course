"""
Если таблица продуктов на складе. Данные представлены в виде list of dicts Найти самые дорогие товары.
Количество товаров, которые необходимо вывести будет передано в первом аргументе, данные по товарам будут переданы
вторым аргументом. 

bigger_price(2, [     {"name": "bread", "price": 100},     {"name": "wine", "price": 138},     {"name": "meat", "price": 15},     {"name": "water", "price": 1} ]) == [     {"name": "wine", "price": 138},     {"name": "bread", "price": 100} ] 

"""

pricing = [
            {"name": "bread", "price": 100},
            {"name": "wine", "price": 138},
            {"name": "meat", "price": 15},
            {"name": "water", "price": 1}]

def find_the_most_expensive(num, list_of_dicts):
    list_of_dicts = sorted(list_of_dicts, key=lambda key_to_sort_by: key_to_sort_by['price'], reverse = True)
    return list_of_dicts[:num]

print(find_the_most_expensive(2 ,pricing))