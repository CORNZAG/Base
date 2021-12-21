print("Я хочу сыграть в одну игру, правила очень простые введи любые пять слов")
import random
f = 0
Hangman = random.randint(1, 5)
hidden_word = ""  # Рандомное выбранное слово из введенных (например, "питон")
coded_word = ""  # Зашифрованное рандомно выбранное слово (например, "_____")
for i in range(5):
    player = input()
    if i + 1 == Hangman:
        hidden_word = player
coded_word = coded_word.rjust(len(hidden_word), "_")
print(coded_word, "Попробуй отгадать слово по буквам")
while hidden_word != coded_word:
    user = input()
    for i in range(len(hidden_word)):
        if hidden_word[i] == user:
            coded_word = coded_word[:i] + user + coded_word[i + 1:]
        elif hidden_word[i] == user:
            print("Всего",f+1,"+1 Балл")
        elif hidden_word[i] != user:
            print("Всего",f-1, "-1 Балл")
    print(coded_word)