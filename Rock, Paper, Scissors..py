import random
choices = ("камень", "ножницы", "бумага")
print("Камень бьёт ножницы, ножницы режут бумагу, бумага бьёт камень")
player = input("Выбирите: камень, ножницы, бумага" "-" )
while player!= "Выйти":
    player = player.lower()
    computer = random.choice(choices)
    print("Твой выбор " + player + ", Компьютер выбрал " + computer + ".")
    if player == computer:
        print ("Ничья")
    elif player == "камень":
        if computer == "ножницы":
            print("Вы победили!")
        else:
            print("Победил компьютор!")
    elif player == "бумага":
        if computer == "камень":
            print ("Вы победили!")
        else:
            print("Победил компьютер")
    elif player == "ножницы":
        if computer == "бумага":
            print("Вы победили!")
        else:
            print("Победил компьтер")
    else:
        print("По-моему, произошла ошибка...")
    print()
    player = input("Выбирите: Камень, ножницы, бумага" "-")