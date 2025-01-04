import random

def hangman():
    wrods = ("apple", "banana", "cat", "dog", "elephant", "penipple", "cyberattack")
    wrods = random.choice(wrods) 
    guessed_letter = []
    tries = 6

    print("Welcome to Hangman!")
    print("try to guess the word. You have 6 attempts")

    while tries>0:
        display_wrods = ''.join([letter if letter in guessed_words])
        print(display_wrods)

        if display_wrods == wrods:
            print("Congralulations! You guessed the corret wrods")
            break

        guess = input("guess a letter:-> ").lower()
        if guess not in wrods:
             

 