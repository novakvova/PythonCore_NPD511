#print("Привіт!")


def writeFileAbonent():
    lastName = input("Вкажіть прізвище: ")
    firstName = input("Вкажіть ім'я: ")
    soName = input("Вкажіть побатькові: ")
    phone = input("Вкажіть телефон: ") 
    address = input("Вкажіть адресу: ")
    # a - вміст стиратися не буде, а файл буде дописуватися
    fileWriter = open("abonents.txt", 'a', encoding="utf-8")

    fileWriter.write(f"{lastName}\n")
    fileWriter.write(f"{firstName}\n")
    fileWriter.write(f"{soName}\n")
    fileWriter.write(f"{phone}\n")
    fileWriter.write(f"{address}\n")
    fileWriter.close()

def clearFileAbonents():
    # w - файл відкриє і очистить його вміст
    fileWriter = open("abonents.txt", 'w', encoding="utf-8")
    fileWriter.close()

def readFileAbonents():
    fileRead = open("abonents.txt", 'r', encoding="utf-8")
    lines = fileRead.read().splitlines()
    i = 0 #Лічильник рядків
    countAbonent = 1 # лічильник абоннетів
    countLines = len(lines) #кількість рядків
    while i < countLines:
        # if lines[i]=="\n":
        #     break # Виходимо із циклу
        print(f"-----------{countAbonent}----------")
        print(f"{lines[i]} {lines[i+1]} {lines[i+2]}")
        print(lines[i+3])
        print(lines[i+4])
        i=i+5 #переходжу на останій рядок
        countAbonent = countAbonent + 1

action = -1
while action!=0:
    print("0.Вихід")
    print("1.Додати клієнта")
    print("2.Показати усіх клієнтів")
    print("3.Очистити список клієнтів")
    print("->_", end="")
    action = int(input())
    match action:
        case 1:
            writeFileAbonent()
            print("--Додали нового абонента---")
        case 2:
            print("--Показуємо усіх абонентів--")
            readFileAbonents()
        case 3:
            clearFileAbonents()
            print("--Очищаємо список абонентів--")
    


