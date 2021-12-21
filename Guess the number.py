# import random
# NumberToGuess=random.randint(1,100)
# userGuess=-1
# while userGuess!=NumberToGuess:
#     userGuess=int(input("Угадай число от 1 до 100"))
#     if userGuess > NumberToGuess:
#         print("Число должно быть меньше!")
#     elif userGuess < NumberToGuess:
#         print("Число должно быть больше!")
#     else:
#         print("Вы угадали, это число = " + str(NumberToGuess))
#         break
#
guesses_made = 0

import random
number = random.randint(0, 20)

print("Загадано число от 0 до 20, отгадайте какое? (Есть 4 попытки)")
while guesses_made < 4:
    guess = int(input())
    guesses_made += 1

    if guess < number:
        print("(нужно больше)")

    if guess > number:
        print("(нужно меньше)")
    if guess == number:
        break

if guess == number:
    print("Ты угадал мое число!")
else:
    print ("Не угадал! Я загадал число {0}".format(number))
# guesses_made = 0
# import random
# number = random.randint(0, 15)
# print("Загадано число от 0 до 15, отгадайте какое?")
# while guesses_made < 3:
#         guess = int(input())
#         guesses_made += 1
#         if guess == number:
#             break
#         if abs(number - guess) < 3:
#             print("Тепло ", end="")
#         else:
#             print("Холодно ", end="")
#         if guess < number:
#             print("(нужно больше)")
#         if guess > number:
#             print("(нужно меньше)")
#     if guess == number:
#         print("Ты угадал мое число!")
#     else:
#         print("Не угадал! Я загадал число {0}".format(number))