name = str(input("ваше имя: "))
age = int(input("ваш возраст: "))
po5rub = int(input("кол-во монет по 5руб:  "))
po10rub = int(input("кол-во монет по 10руб:  "))

if(name == "Oleg"):
    print("тебе не продадут хот дог, ты Олег")
else:
    if(age < 18):
        print("тебе не продадут хот дог, ты мелкий")
    else:
        if(age % 2 == 1):
            print("у тебя возраст не красивый")
        else:
           money =  po5rub * 10 + po10rub * 10
           hotdogs = money // 20
           print("Вот твои", hotdogs,"хотдогов")

        