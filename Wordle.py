import colorama
from colorama import init, Fore, Style
from random import choice

init()

with open('words.txt', encoding='utf-8') as fille:
    words = fille.read().split('\n')
    answer_word = str()
    while len(answer_word) != 5:
        answer_word = choice(words).strip()

    print('\n')
    print("""Угадайте слово из 5 букв.У Вас есть 6 попыток.
Если буква встречается в загаданном слове один раз, то она подсветится желтым. 
Если буква встречается в загаданном слове больше одного раза, то она подсветится синим. 
Если буквы нет в слове, то она не будет подсвечена. Удачи!""")
    print('\n')
    while True:
        deb = int(input(f"Если хотите включить режим показа ответа, введите 1, в противном случае введите 2: \n"))
        if deb != 1 and deb != 2:
            print(f"\nВведите 1 или 2\n")
        elif deb == 1:
            print(f"\n{answer_word}\n")
            break
        elif deb == 2:
            break
    output = ''

    for i in range(1, 7):
        # Ввод слова от пользователя
        user_input = str()
        while True:
            user_input = input("Введите слово:")
            if len(user_input) != 5 or any(char.isdigit() for char in user_input) or any(not char.isalpha() for char in user_input):
                print("Введите слово из 5 букв, без цифр или символов!")
            else:
                break
        output = ''

        if user_input == answer_word:
            print('Победа! Вы угадали слово!')
            break

        for index, char in enumerate(user_input):
            if char == answer_word[index]: # Если буква есть в слове и на верном месте
                output += Fore.GREEN + char.upper() + Style.RESET_ALL
            elif answer_word.count(char) > 1:  # Если буква в слове встречается больше одного раза
                output += Fore.BLUE + char.upper() + Style.RESET_ALL
            elif char in answer_word: # Если буква есть в слове
                output += Fore.YELLOW + char.upper() + Style.RESET_ALL
            else: # Если буквы нет в слове
                output += Style.RESET_ALL + char.lower() + Style.RESET_ALL
        print(f"Оставшиеся попытки: {6-i}\n")
        print(output)
if user_input != answer_word:
    print(f'\nВы проиграли. Загаданное слово было: {Fore.RED + answer_word.upper()}')
