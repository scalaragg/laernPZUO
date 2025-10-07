week = []
max = 0
for day in range(7):
    temp = int(input('скок потратил?'))
    if temp > max:
        max = temp

    week.append(temp)
total = 0
for day in week:
    total = total + day
print('потратил за неделю:', total)
print('средний расход за день: ', total//7)
print("Больше всего за один день потратил: ", max)