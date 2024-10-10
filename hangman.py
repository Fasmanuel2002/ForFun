import random as rd
import sys

contador = 10
all_words = ["France", "Spain", "USA", "Guatemala", "Rusia", "UnitedKingdom", "brazil", "Japan", "Nicaragua", "Peru", "Canada", "Germany", "Korea"]
correct = []
word = rd.choice(all_words).lower()

display_word = ["_" if letter.isalpha() else letter for letter in word]
print(" ".join(display_word))

while(contador != 0):
    user = input("\nEnter a letter: ").lower()
    if user in word:
        print("The user letter is correct")
        for letter in word:
            if letter == user:
                index = word.index(letter)
                correct.append(letter)
                print(correct)
                display_word[index] = letter
                print(" ".join(display_word))
                break
        
    if user not in word:
        print("The user letter is incorrect")
        contador -= 1
        print(f"How many chances you have {contador}")
        
    if len(correct) == len(word):
        print("Hooray you won")
        sys.exit("Finish program")
    if contador == 0:
        sys.exit(f"The word was {word}")