name = str(input("ваше имя: ")) 
if(name == "Oleg" and "oleg"):
    print("тебе не продадут хот дог, ты Олег")
else:
    age = int(input("ваш возраст: "))
    if(age < 18):
        print("тебе не продадут хот дог, ты мелкий")
    else:
        if(age % 2 == 1):
            print("у тебя возраст не кртуой")
        else:  
            po5rub = int(input("кол-во монет по 5руб:  "))
            po10rub = int(input("кол-во монет по 10руб:  "))

        money =  po5rub * 5 + po10rub * 10
        hotdogs = money // 20
        if(money <20):
            print("у тебя мало денег даже для одного хот дога")
        else:
            print("Вот твои", hotdogs,"хотдогов/a")
