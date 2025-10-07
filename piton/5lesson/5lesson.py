L1 = 5
w1 = 3
S1 = L1 * w1
print(f'площадь команты 1 - {S1}')
# funkciya
def great():
    """ЭТО ФУНКЦИЯ ЙОУ"""
    print("this is my first def")
great()

#argument def
def puzo(name):
    """next def"""
    print(f"Hello {name} this is my first def")
puzo("Oleg")
puzo("hryak")

#def with any settings
def introduce(name,age,city):
    """about person"""
    print(f'Im {name} {age} i live in {city}')
introduce('Oleg',17,'city 17')
def calculate_area(L,W):
    area = L * W
    return area
room_area = calculate_area(5,3)
print(f'Ку йоу {room_area}')

def isAdult(age):
    if age >= 18:
        return True
    else:
        return False
if isAdult(2):
    print("достуа разрешен")
else:
    print("НИКАКОГО ЖОРНО С ПАУКАМИ")