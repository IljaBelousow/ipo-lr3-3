day = int(input("Введите день: "))
month = input("Введите месяц: ").lower() 
day_month = {
    "январь": 31,
    "февраль": 28, 
    "март": 31,
    "апрель": 30,
    "май": 31,
    "июнь": 30,
    "июль": 31,
    "август": 31,
    "сентябрь": 30,
    "октябрь": 31,
    "ноябрь": 30,
    "декабрь": 31
}
if month in day_month and 1 <= day <= day_month[month]:
    if month in ["март", "апрель", "май"]:
        print("Вы весной")
    elif month in ["июнь", "июль", "август"]:
        print("Вы летом")
    elif month in ["сентябрь", "октябрь", "ноябрь"]:
        print("Вы осенью")
    elif month in ["декабрь", "январь", "февраль"]:
        print("Вы зимой")
else:
    print("Вы не родились :(")