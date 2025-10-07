empty_list = [] # СПИСОК
fruits = ["apple","banana","wild cucumber"]
mixed_list = [1, "PUZO", True]
numbers = list([1,2,3,4,5,6,7])
print(fruits[2])
print(fruits[-1])
# добавление
print(fruits)
fruits.append("MANGO")
print(fruits)
fruits.insert(1, "tolst")
print(fruits)

fruits.remove("apple")
aboba = fruits.pop(-1)
print (aboba)
print(fruits)
numbers1 = [0,1,2,3,4,5,6,7,8,9]
print(numbers1[2:9]) # от 2 до 8
print(numbers1[:9]) # от начала и до 8
print(numbers1[2:]) # от 2 до конца списка
print(numbers1[::2]) # выводит каждое число которое стоит после ::
print(numbers1[::-1]) # вывод списка с конца
print(numbers1[7:2:-10])


for fruit in fruits: # для каждого рфукта в списке
    print("я люблю:", fruit)
list_leight = len(fruits)
print(list_leight)
for i in range(len(fruits)):
    print("Элемент под индексом: ", i, "-это", fruits[i])

prices = [100,200,250,50]
total = 0
for price in prices:
    total= total + price
print("summa vseh cen kirieshek: ", total)

for price in range(len(prices)): #другой способ
    total1= total1 + prices[price]
print("summa vseh cen kirieshek: ", total)