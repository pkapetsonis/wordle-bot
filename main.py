from words import words,starting_words
from random import choice


def input_handler(word):
    letter_count = 0

    duplicates = False
    for letter in word:
        if word.count(letter) > 1:
            duplicates = True
    
    if duplicates:
        print("Warning double letters!")
    else:
        print()
    

    

    for l in word:



        data = input(f"{l}: ")

        if data == "0":
            for w in words[:]:
                if l in w:
                    words.remove(w)        

        elif data == "1":
            for w in words[:]:
                if l not in w :
                    words.remove(w)
                elif word[letter_count] != w[letter_count]:
                    words.remove(w)

        elif data == "2":
            for w in words[:]:
                if l not in w :
                    words.remove(w)
                elif word[letter_count] == w[letter_count]:
                    words.remove(w)
        
        letter_count += 1

print("""           WELCOME TO
█░█░█ █▀█ █▀█ █▀▄ █░░ █▀▀   █▀ █▀█ █░░ █░█ █▀▀ █▀█
▀▄▀▄▀ █▄█ █▀▄ █▄▀ █▄▄ ██▄   ▄█ █▄█ █▄▄ ▀▄▀ ██▄ █▀▄
                HOW TO USE:
            -Enter the word given from the bot to wordle.
            -The commands are:
                -"0" for everything wrong (grey color).
                -"1' fro everything right (green color).
                -"2" for right letter but wrong position (yellow color).
            -If there is warn for double letter and one of the two is right (green) and the other wrong (grey) send 1 for the right and nothing for the wrong.
      
      Made by: pkapetsonis\n""")

word = choice(starting_words)
words.remove(word)
print(f'The first word is: "{word}"', end=" ")
input_handler(word)

word = choice(words)
words.remove(word)
print(f'The second word is: "{word}"', end=" ")
input_handler(word)

word = choice(words)
words.remove(word)
print(f'The third word is: "{word}"', end=" ")
input_handler(word)

word = choice(words)
words.remove(word)
print(f'The fourth word is: "{word}"', end=" ")
input_handler(word)

word = choice(words)
words.remove(word)
print(f'The fifth word is: "{word}"', end=" ")
input_handler(word)

word = choice(words)
print(f'The final word is: "{word}"')



