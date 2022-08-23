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

def hang():
    
    clean_francais = []
    liste_francais1 = open("liste_francais.txt", "r")
    liste_francais = liste_francais1.readlines()
    for x in range(len(liste_francais)):
        if x != len(liste_francais):
            clean_francais.append(liste_francais[x][0:-1])
        else:
            clean_francais.append(liste_francais[x])
    
    word_to_find = random.choice(clean_francais)
    
    print(" _ " * len(word_to_find))

    count = 0
    L = []
    word_fl = []

    liss_word_to_find = lissage_lettres(word_to_find)

    while True:
        input1 = input("Tapez une lettre: ")

        if input1.isalpha() and len(input1) == 1 or input1 in [" ", "'", "-"]:
            while True:
                if input1 in liss_word_to_find:
                    word_fl = []

                    for x in range(len(liss_word_to_find)):
                        if liss_word_to_find[x] == input1:
                            L.append(liss_word_to_find[x])
                            
                    for i in range(len(word_to_find)):
                        if liss_word_to_find[i] in L:
                            word_fl.append(" " + word_to_find[i] + " ")
                        else:
                            word_fl.append(" _ ") 
                    print(''.join(word_fl))

                    if word_fl and " _ " not in word_fl:
                        return GAME_END[0]
                    else:
                        input1 = input("Tapez une lettre: ")
                else:
                    count += 1
                    if count > 8:
                        print(HANGMANPICS[8], end="\n")
                        return f'{GAME_END[1]}\n\nLe mot cherché était: {word_to_find}\n\n'
                    else:
                        print(HANGMANPICS[count-1], end="\n")
                    if word_fl:
                        print(''.join(word_fl))
                    else:
                        print(" _ " * len(word_to_find))
                    input1 = input("Tapez une lettre: ")
    
        else:
            print("Vous devez entrer une lettre et une seule: ")
            continue



print(hang())