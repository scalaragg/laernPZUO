book = {
    "title": "1984", 
    "author": "Джордж Оруэлл",
    "year": 1950,
    "ganre": "Антиутопия"
}
player = {
    "name": "oleg67",
    "damage": 20.3,
    "age": 42,
    "city": 17,
    "isAlive": True
}
simple = {
    1: "Один",
    2: "Два"
}
print(player['name']) 
print(player.get('class'))  # none(без ошибки)
print(player.get('age'))
print(player.get('class','не найден')) # пишет что справа

#перезаписать значение
player["damage"] = 22.5
#создатся новая пара ключ значение
player['class'] = 'koldun'
print(player)

# if in slovar player have key 'name' = выполнить
if 'name' in player:
    print('ключ name существует')
if 'HP' not in player:
    print('Ключ HP не найден')
#удаление
removed_value = player.pop('city')
#удалить последний элемент списка
last_item = player.popitem()
print('Удалили последнюю пару: ', last_item)
print(player.keys()) # вывести ключи
print(player.values()) # вывести значение ключей
print(player.items()) # вывести пары

# ПЕРЕБОР СЛОВАРЕЙ В ЦИКЛАХ бля поч капс
#перебор ключей словаря
for key in player.keys():
    print(key) # напечатает: name age damage ....

#перебор по значеням
for value in player.values():
    print(value) # напечатает: oleg67 42 22.5 ....

for key, value, in player.items():
    print(f'Ключ {key}, значнеие: {value}')


students = [
    {'name': 'Никтос','age': 0, 'grades': [5,4,3,4,2,3,5]},
    {'name': 'Ванек','age': 15, 'grades': [5,5,5,5,5,5,4]},
    {'name': 'Санек','age': 9, 'grades': [3,3,2,4,4,2,5]}
]

#получение возратса первого студента
print(students[0]['age'])
print(students[1]['name'])

#вывод всех имен стужентов
for student in students:
    print(student['name'])