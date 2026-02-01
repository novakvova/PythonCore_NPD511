# Робимо функцію, яка буде реалізовувати калькулятор
def myCalc():
    a = input("Вкажіть значення a: ->_")
    b = input("Вкажіть значення b: ->_") # тут текст - '34', "65"
    intA = int(a)
    intB = int(b) # тут ми маємо перетворення у тип ЧИСЛО 1, 34, 2.53
    print(f"{a}+{b}={intA+intB}") #f - форматований рядок у Python
    print(f"{a}-{b}={intA-intB}")
    print(f"{a}*{b}={intA*intB}")
    # if intB!=0: # != - оператор не дорівнює, тобто це коли 5!=0 - True
    #     print(f"{a}/{b}={intA/intB}")
    # else:
    #     print("Має спробу діленняна 0")
    if intB==0: # == це порівнння
        print("Має спробу діленняна 0")
    else:
        print(f"{a}/{b}={intA/intB}")

#викли функції
myCalc()