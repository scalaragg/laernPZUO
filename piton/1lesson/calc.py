num1 = int(input("vvedite chislo: "))
num2 = int(input("vtoroe chislo: "))

char = str(input("chto delaem? + - * / %"))

if(num2 == 0 and char =="/"):
    print("na nol delit nezya")
else:
    if(char == "+"):
        print(num1+num2)

    elif(char == "-"):
        print(num1-num2)

    elif(char == "*"):
        print(num1*num2)

    elif(char == "/"):
        print(num1/num2)

    elif(char == "%"):
        print(num1%num2)
    else:
        print("ti pereputal rialno")

rus = 76 # 60
mat = 41 # 40
inf = 80 # 100
if(rus >=60 and mat >= 40 or inf == 100 ):
    print("sdal")
else:
    print("loh")