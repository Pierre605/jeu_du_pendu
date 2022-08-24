import random
from ascii_pics import HANGMANPICS, GAME_END

def lissage_lettres(word):
    L = []
    for l in word:
        if l == "ç":
            L.append("c")
        elif l == "é" or l == "è":
            L.append("e")
        elif l == "î" or l == "ï":
            L.append("i")
        elif l == "â":
            L.append("a")
        else:
            L.append(l)
    return ('').join(L)

def level_option():
    while True:
        level_input = input("\nChoisissez votre niveau de difficulté:\n\nFacile: Tapez 1\nMedium: Tapez 2\nDifficile: Tapez 3\n\n")
        if len(level_input) == 1 and level_input in ['1', '2', '3']:
            return level_input
        else:
            print("\n ! Tapez 1, 2 ou 3")
            continue


def hang():
    
    level = level_option()
    clean_francais = []
    liste_francais1 = open("liste_francais.txt", "r")
    liste_francais = liste_francais1.readlines()
    for x in range(len(liste_francais)):
        if x != len(liste_francais):
            clean_francais.append(liste_francais[x][0:-1])
        else:
            clean_francais.append(liste_francais[x])
    
    word_to_find = random.choice(clean_francais)
    liss_word_to_find = lissage_lettres(word_to_find)

    
    
    if level == '1':
        print("\nNiveau FACILE\n")
        count = 0
        final1 = []
        first_and_last_letter = []
        word_found_letters = []
        easy_level_setup = []

        first_and_last_letter.append(liss_word_to_find[0])
        first_and_last_letter.append(liss_word_to_find[-1])
        word_found_letters.append(liss_word_to_find[0])
        word_found_letters.append(liss_word_to_find[-1])
        for i in range(len(word_to_find)):
            if liss_word_to_find[i] in first_and_last_letter:
                easy_level_setup.append(" " + word_to_find[i] + " ")
            else:
                easy_level_setup.append(" _ ")
        print(''.join(easy_level_setup))


        while True:
            input1 = input("Tapez une lettre: ")

            if input1.isalpha() and len(input1) == 1 or input1 in [" ", "'", "-"]:
                while True:
                    if input1 in liss_word_to_find:
                        final1 = []

                        for x in range(len(liss_word_to_find)):
                            if liss_word_to_find[x] == input1:
                                word_found_letters.append(liss_word_to_find[x])
                                
                        for i in range(len(liss_word_to_find)):
                            if liss_word_to_find[i] in word_found_letters:
                                final1.append(" " + word_to_find[i] + " ")
                            else:
                                final1.append(" _ ") 
                        print('\n' + ''.join(final1) + '\n')

                        if " _ " not in final1:
                            return GAME_END[0]
                        else:
                            input1 = input("Tapez une lettre: ")
                    else:
                        count += 1
                        if len(word_to_find) > 6:
                            if count > 8:
                                return f'{GAME_END[1]}\n\nLe mot cherché était: {word_to_find}\n\n'
                            else:
                                print(HANGMANPICS[count-1], end="\n")
                                print('\n' + ''.join(final1) + '\n')
                        else:
                            if count > 6:
                                return f'{GAME_END[1]}\n\nLe mot cherché était: {word_to_find}\n\n'
                            else:
                                print(HANGMANPICS[count+1], end="\n")
                                if word_found_letters != first_and_last_letter:
                                    print('\n' + ''.join(final1) + '\n')
                                else:
                                    print('\n' + ''.join(easy_level_setup) + '\n')

                        input1 = input("Tapez une lettre: ")
        
            else:
                print("\n ! Vous devez entrer une lettre et une seule: ")
                continue


    elif level == '2':
        print("\nNiveau MEDIUM\n")
        count = 0
        final1 = []
        word_found_letters = []

        print(' _ ' * len(word_to_find))

        while True:
            input1 = input("Tapez une lettre: ")

            if input1.isalpha() and len(input1) == 1 or input1 in [" ", "'", "-"]:
                while True:
                    if input1 in liss_word_to_find:
                        final1 = []

                        for x in range(len(liss_word_to_find)):
                            if liss_word_to_find[x] == input1:
                                word_found_letters.append(liss_word_to_find[x])
                                
                        for i in range(len(liss_word_to_find)):
                            if liss_word_to_find[i] in word_found_letters:
                                final1.append(" " + word_to_find[i] + " ")
                            else:
                                final1.append(" _ ") 
                        print('\n' + ''.join(final1) + '\n')

                        if " _ " not in final1:
                            return GAME_END[0]
                        else:
                            input1 = input("Tapez une lettre: ")
                    else:
                        count += 1
                        if len(word_to_find) > 6:
                            if count > 8:
                                return f'{GAME_END[1]}\n\nLe mot cherché était: {word_to_find}\n\n'
                            else:
                                print(HANGMANPICS[count-1], end="\n")
                                if word_found_letters:
                                    print('\n' + ''.join(final1) + '\n')
                                else:
                                    print('\n' + (" _ " * len(word_to_find)) + '\n')
                        else:
                            if count > 6:
                                return f'{GAME_END[1]}\n\nLe mot cherché était: {word_to_find}\n\n'
                            else:
                                print(HANGMANPICS[count+1], end="\n")
                                if word_found_letters:
                                    print('\n' + ''.join(final1) + '\n')
                                else:
                                    print('\n' + (" _ " * len(word_to_find)) + '\n')
                        

                        input1 = input("Tapez une lettre: ")
        
            else:
                print("\n !Vous devez entrer une lettre et une seule: ")
                continue

    elif level == '3':
        print("\nNiveau DIFFICILE\n")
        count = 0
        final1 = []
        word_found_letters = []
        HANGMANPICS_lvl3 = HANGMANPICS
        HANGMANPICS_lvl3.pop(0)

        print(' _ ' * len(word_to_find))

        while True:
            input1 = input("Tapez une lettre: ")

            if input1.isalpha() and len(input1) == 1 or input1 in [" ", "'", "-"]:
                while True:
                    if input1 in liss_word_to_find:
                        final1 = []

                        for x in range(len(liss_word_to_find)):
                            if liss_word_to_find[x] == input1:
                                word_found_letters.append(liss_word_to_find[x])
                                
                        for i in range(len(liss_word_to_find)):
                            if liss_word_to_find[i] in word_found_letters:
                                final1.append(" " + word_to_find[i] + " ")
                            else:
                                final1.append(" _ ") 
                        print('\n' + ''.join(final1) + '\n')

                        if " _ " not in final1:
                            return GAME_END[0]
                        else:
                            input1 = input("Tapez une lettre: ")
                    else:
                        count += 1
                        if len(word_to_find) > 8:
                            if count > 8:
                                return f'{GAME_END[1]}\n\nLe mot cherché était: {word_to_find}\n\n'
                            else:
                                print(HANGMANPICS[count-1], end="\n")
                                if word_found_letters:
                                    print('\n' + ''.join(final1) + '\n')
                                else:
                                    print('\n' + (" _ " * len(word_to_find)) + '\n')
                        elif len(word_to_find) <= 8 and len(word_to_find) > 5:
                            if count > 5:
                                return f'{GAME_END[1]}\n\nLe mot cherché était: {word_to_find}\n\n'
                            else:
                                print(HANGMANPICS[count+2], end="\n")
                                if word_found_letters:
                                    print('\n' + ''.join(final1) + '\n')
                                else:
                                    print('\n' + (" _ " * len(word_to_find)) + '\n')
                        else:
                            if count > 4:
                                return f'{GAME_END[1]}\n\nLe mot cherché était: {word_to_find}\n\n'
                            else:
                                print(HANGMANPICS_lvl3[count+2], end="\n")
                                if word_found_letters:
                                    print('\n' + ''.join(final1) + '\n')
                                else:
                                    print('\n' + (" _ " * len(word_to_find)) + '\n')
                        

                        input1 = input("Tapez une lettre: ")
        
            else:
                print("\n ! Vous devez entrer une lettre et une seule: ")
                continue



print(hang())