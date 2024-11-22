a = int(input("vvedite den' rozdeniya "))
b = input("vvedite mesyac rozdeniya ")
if (b == "март" and (a > 0 and a < 32)) or (b == "апрель" and (a > 0 and a < 31)) or (b == "май" and (a > 0 and a < 32)):
    print("vi rodilis' vesnoi")
elif (b == "июнь" and (a > 0 and a < 31)) or (b == "июль" and (a > 0 and a < 32)) or (b == "август" and (a > 0 and a < 32)):
    print("vi rodilis' letom")
elif (b == "сентябрь" and (a > 0 and a < 31)) or (b == "октябрь" and (a > 0 and a < 32)) or (b == "ноябрь" and (a > 0 and a < 31)):
    print("vi rodilis' osen'u")
elif (b == "декабрь" and (a > 0 and a < 32)) or (b == "январь" and (a > 0 and a < 32)) or (b == "февраль" and (a > 0 and a < 30)):
    print("vi rodilis' zimoi")
else:
    print("вы не родились :(")
