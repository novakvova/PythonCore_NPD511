# Користувач вводить номер тижня 1 - понеділок, 2 - вівторок і т.д.
# Програма виводить назву дня тижня відповідно до введеного номера.
# Користувач вказує номер тижня
day = input("Введіть номер дня тижня (1-7): ")
# Петеворюю str в int
day_number = int(day) # створив нову змінну day_number і перетворив str в int і внеї зписав
if day_number == 1:
    print("Понеділок")
elif day_number == 2:
    print("Вівторок")
elif day_number == 3:
    print("Середа")
elif day_number == 4:
    print("Четвер")
elif day_number == 5:
    print("П'ятниця")
elif day_number == 6:
    print("Субота")
elif day_number == 7:
    print("Неділя")
else:
    print("Некоректний номер дня тижня")