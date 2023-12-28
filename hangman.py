import random
from ascii_pics import HANGMANPICS, GAME_END, title, bye

print(title)

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
            L.append(l.lower())
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
    liste_francais1 = open("liste_francais.txt", "r", encoding='latin-1')
    liste_francais = liste_francais1.readlines()
    for x in range(len(liste_francais)):
        if x != len(liste_francais):
            clean_francais.append(liste_francais[x][0:-1])
        else:
            clean_francais.append(liste_francais[x])

    clean_francais = [i for i in clean_francais if ' ' not in i and len(i)>= 5]
    
    word_to_find = random.choice(clean_francais)
    word_to_find = "abat-jour"
    # word_to_find = "baguette magique"
    word_to_find = "boute-en-train"
    liss_word_to_find = lissage_lettres(word_to_find)


    if level == '1':
        print("\nNiveau FACILE\n")
        count = 0
        final1 = []
        first_and_last_letter = []
        word_found_letters = []
        easy_level_setup = []
        input_play_again = 'o'

        first_and_last_letter.append(liss_word_to_find[0])
        first_and_last_letter.append(liss_word_to_find[-1])
        word_found_letters.append(liss_word_to_find[0])
        word_found_letters.append(liss_word_to_find[-1])

        for i in range(len(word_to_find)):
            if liss_word_to_find[i] in [" ", "'", "-"]:
                word_found_letters.append(liss_word_to_find[i])

        for i in range(len(word_to_find)):
            if liss_word_to_find[i] in first_and_last_letter or liss_word_to_find[i] in [" ", "'", "-"]:
                easy_level_setup.append(" " + word_to_find[i] + " ")
            else:
                easy_level_setup.append(" _ ")
        print(''.join(easy_level_setup))


        while True:
            input1 = input("Tapez une lettre: ")

            if (input1.isalpha() or input1 in [" ", "'", "-"]) and len(input1) == 1:
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

                        if input_play_again == 'n':
                            return ''

                        print('\n' + ''.join(final1) + '\n')

                        if " _ " not in final1:
                            print(GAME_END[0])
                            input_play_again = input("Une autre partie ? Entrez 'o' oui, 'n' non :  ")
                            if input_play_again == 'o':
                                return(hang())
                            else:
                                return bye
                        else:
                            input1 = input("Tapez une lettre: ")
                    else:
                        count += 1
                        if len(word_to_find) > 6:
                            if count > 8:
                                print(f'{HANGMANPICS[8]}\n{GAME_END[1]}\n\nLe mot cherché était: {word_to_find}\n\n')
                                input_play_again = input("Une autre partie ? Entrez 'o' oui, 'n' non :  ")
                                if input_play_again == 'o':
                                    return(hang())
                                else:
                                    return bye
                            else:
                                print(HANGMANPICS[count-1], end="\n")
                                if word_found_letters != first_and_last_letter:
                                    print('\n' + ''.join(final1) + '\n')
                                else:
                                    print('\n' + ''.join(easy_level_setup) + '\n')
                        else:
                            if count > 6:
                                print(f'{HANGMANPICS[8]}\n{GAME_END[1]}\n\nLe mot cherché était: {word_to_find}\n\n')
                                input_play_again = input("Une autre partie ? Entrez 'o' oui, 'n' non :  ")
                                if input_play_again == 'o':
                                    return(hang())
                                else:
                                    return bye
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
        input_play_again = 'o'

        init = []
        for i in range(len(word_to_find)):
            if liss_word_to_find[i] in [" ", "'", "-"]:
                word_found_letters.append(liss_word_to_find[i])

        for i in range(len(word_to_find)):
            if liss_word_to_find[i] in [" ", "'", "-"]:
                init.append(" " + word_to_find[i] + " ")
            else:
                init.append(" _ ")
        print(''.join(init))

        while True:
            input1 = input("Tapez une lettre: ")

            if (input1.isalpha() or input1 in [" ", "'", "-"]) and len(input1) == 1:
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
                        
                        if input_play_again == 'n':
                            return ''

                        print('\n' + ''.join(final1) + '\n')

                        if " _ " not in final1:
                            print(GAME_END[0])
                            input_play_again = input("Une autre partie ? Entrez 'o' oui, 'n' non :  ")
                            if input_play_again == 'o':
                                return(hang())
                            else:
                                return bye
                        else:
                            input1 = input("Tapez une lettre: ")
                    else:
                        count += 1
                        if len(word_to_find) > 6:
                            if count > 8:
                                print(f'{HANGMANPICS[8]}\n{GAME_END[1]}\n\nLe mot cherché était: {word_to_find}\n\n')
                                input_play_again = input("Une autre partie ? Entrez 'o' oui, 'n' non :  ")
                                if input_play_again == 'o':
                                    return(hang())
                                else:
                                    return bye
                            else:
                                print(HANGMANPICS[count-1], end="\n")
                                if word_found_letters:
                                    print('\n' + ''.join(final1) + '\n')
                                else:
                                    print('\n' + (" _ " * len(word_to_find)) + '\n')
                        else:
                            if count > 6:
                                print(f'{HANGMANPICS[8]}\n{GAME_END[1]}\n\nLe mot cherché était: {word_to_find}\n\n')
                                input_play_again = input("Une autre partie ? Entrez 'o' oui, 'n' non :  ")
                                if input_play_again == 'o':
                                    return(hang())
                                else:
                                    return bye
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
        input_play_again = 'o'
        HANGMANPICS_lvl3_1 = []
        HANGMANPICS_lvl3_2 = []
        PICS_index_to_keep_1 = [2, 3, 4, 6, 7, 8]
        PICS_index_to_keep_2 = [2, 3, 4, 6, 8]
        for i in PICS_index_to_keep_1:
            HANGMANPICS_lvl3_1.append(HANGMANPICS[i])
        for j in PICS_index_to_keep_2:
            HANGMANPICS_lvl3_2.append(HANGMANPICS[j])


        init = []
        for i in range(len(word_to_find)):
            if liss_word_to_find[i] in [" ", "'", "-"]:
                word_found_letters.append(liss_word_to_find[i])

        for i in range(len(word_to_find)):
            if liss_word_to_find[i] in [" ", "'", "-"]:
                init.append(" " + word_to_find[i] + " ")
            else:
                init.append(" _ ")
        print(''.join(init))

        while True:
            input1 = input("Tapez une lettre: ")

            if (input1.isalpha() or input1 in [" ", "'", "-"]) and len(input1) == 1:
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

                        if input_play_again == 'n':
                            return ''

                        print('\n' + ''.join(final1) + '\n')

                        if " _ " not in final1:
                            print(GAME_END[0])
                            input_play_again = input("Une autre partie ? Entrez 'o' oui, 'n' non :  ")
                            if input_play_again == 'o':
                                return(hang())
                            else:
                                return bye
                        else:
                            input1 = input("Tapez une lettre: ")
                    else:
                        count += 1
                        if len(word_to_find) > 8:
                            if count > 8:
                                print(f'{HANGMANPICS[8]}\n{GAME_END[1]}\n\nLe mot cherché était: {word_to_find}\n\n')
                                input_play_again = input("Une autre partie ? Entrez 'o' oui, 'n' non :  ")
                                if input_play_again == 'o':
                                    return(hang())
                                else:
                                    return bye
                            else:
                                print(HANGMANPICS[count-1], end="\n")
                                if word_found_letters:
                                    print('\n' + ''.join(final1) + '\n')
                                else:
                                    print('\n' + (" _ " * len(word_to_find)) + '\n')
                        elif len(word_to_find) <= 8 and len(word_to_find) > 5:
                            if count > 5:
                                print(f'{HANGMANPICS[8]}\n{GAME_END[1]}\n\nLe mot cherché était: {word_to_find}\n\n')
                                input_play_again = input("Une autre partie ? Entrez 'o' oui, 'n' non :  ")
                                if input_play_again == 'o':
                                    return(hang())
                                else:
                                    return bye
                            else:
                                print(HANGMANPICS_lvl3_1[count-1], end="\n")
                                if word_found_letters:
                                    print('\n' + ''.join(final1) + '\n')
                                else:
                                    print('\n' + (" _ " * len(word_to_find)) + '\n')
                        else:
                            if count > 4:
                                print(f'{HANGMANPICS[8]}\n{GAME_END[1]}\n\nLe mot cherché était: {word_to_find}\n\n')
                                input_play_again = input("Une autre partie ? Entrez 'o' oui, 'n' non :  ")
                                if input_play_again == 'o':
                                    return(hang())
                                else:
                                    return bye
                            else:
                                print(HANGMANPICS_lvl3_2[count-1], end="\n")
                                if word_found_letters:
                                    print('\n' + ''.join(final1) + '\n')
                                else:
                                    print('\n' + (" _ " * len(word_to_find)) + '\n')

                        input1 = input("Tapez une lettre: ")
        
            else:
                print("\n ! Vous devez entrer une lettre et une seule: ")
                continue


print(hang())
