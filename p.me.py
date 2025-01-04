import random
# from random_word import RandomWords

Words = ("apples", "bananas", "balls", "phyclogys", "perrameters", "penipples", "games")



hangman_art = {0:("  ",
                  "  ",
                  "  "),
              1: (" o ",
                  "    ",
                  "   ",),
               2: (" o ",
                   " | ",
                   "   "),
                3: (" o ",
                    "/| ",
                    "   "),
                4: (" o ",
                    "/|\\",
                    "   "),
                5: (" o ",
                    "/|\\",
                    "/   "),
                6: (" o ",
                    "/|\\",
                    "/ \\")}

for line in hangman_art[6]:
 print(line)

# def display_man(wrong_guesses):
#     print("********************")
#     for line in hangman_art[wrong_guesses]:      
#         print(line)
#     print("********************")
    

# def display_hint(hint):
#   print(" _ ".join(hint))
   

# def display_answer(answer):
#   print(" _ ".join(answer))
   

# def main():
#     answer = random.choice(Words)
#     hint = ["_"] * len(answer)
#     wrong_guesss = 0
#     guessed_letters = set()
#     is_running = True

#     while is_running:
#         display_man(wrong_guesss)
#         display_hint(hint)
#         guess = input("enter a lettet:-  ").lower()

#         if len(guess) != 1 or not guess.isalpha():
#             print("Invalid input")
#             continue
#         if guess in guessed_letters:
#             print(f"{guess} is already guessed")
#             continue
            
#     guessed_letters.add(guess)

#     if guess in answer:
#         for i in range(len(answer)):
#             if answer[i] == guess:
#                 hint[i] = guess
#             else:
#                 woring_guesss += 1
            
#             if "_" not in hint:
#                 display_man(wrong_guesss)
#                 display_answer(answer)
#                 print("You win")
#                 is_running = False
#             elif wrong_guesss >= len(hangman_art) - 1:
#                 display_man( wrong_guesss)
#                 display_answer(answer)
#                 print("You lose!")
#                 is_running = False


# if __name__== "__main__":
        #  main()