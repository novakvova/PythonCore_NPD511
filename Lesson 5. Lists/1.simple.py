print("---Робота із списками в Python---")

myList = [12, 18, 33, 22]
print("Початковий список:", myList)

# можна зберігати різні типи даних
mixedList = [12, "Hello", 45.6, True]
print("Список з різними типами даних:", mixedList)

# Можна зветрати до елементів списку за індексом
# Індекси починаються з 0
print("Перший елемент списку myList:", myList[0])

myList[0] = "Сало"

print("Змінений список myList:", myList)

myList.append(29)
print("Список myList після додавання нового елемента 29:", myList)

cats = ["Мурка", "Барсик", "Васька"]
print("Список котів:", cats)

myList.extend(cats) # до myList додаємо у кінець всі елементи зі списку cats
print("myList після додавання списку котів:", myList)

del myList[0] # видаляємо перший елемент списку
print("myList після видалення першого елемента:", myList)

myList.append(['ss', 'ee']) # додаємо до myList новий елемент - список з двох змінних
print("myList після додавання нового елемента-списку:", myList)

print("Довжина myList:", len(myList))

myList.extend([100, 200, 300])
print("myList після додавання ще трьох елементів:", myList)



