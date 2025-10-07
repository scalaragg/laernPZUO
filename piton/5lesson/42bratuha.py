dictionary = {
    'book': 'книга',
    'cucmber': 'огурец',
    'game': 'игра',
    'dota': 'аутизм',
    'apple': 'яблоко'
}

while True:
        word = input('слово для перевода(quit шоб стоп): ')

        if word =="quit":
            print('всё стоп')
            break

        if word in dictionary:
            print('перевод: ', dictionary[word])
        else:
            print('перевода нет')
            otvet = input('добавим? (да)')

            if otvet == 'да':
                perevod = input('как переводится?')
                dictionary[word] = perevod
                print('перевод добавлен')
