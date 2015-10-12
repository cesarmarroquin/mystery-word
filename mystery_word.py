import re
import random
i = 0

word_list = ["bird", "calf", "river", "stream", "kneecap",  "cookbook",
             "language", "sneaker", "algorithm", "integration", "brain"]

def read_whole_file(input_file):
    """this function opens the file"""
    with open(input_file) as file:
        file = file.read()
        file = file.lower().split()
    return file


def easy_words(word):
    print("easy_words!")
    all_easy_words = list(filter((lambda x: len(x) >= 4 and len(x) <= 6 ), word))

    return all_easy_words


def medium_words(word):
    print("medium_words!")
    all_medium_words = list(filter((lambda x: len(x) >= 6 and len(x) <= 8 ), word))

    return all_medium_words


def hard_words(word):
    print("hard_words!")
    all_hard_words = list(filter((lambda x: len(x) >= 8 ), word))

    return all_hard_words


def random_word(list_of_words2):
    print("random_word!")
    random_word = random.choice(list_of_words2)

    return random_word
    pass


def display_word(list_of_words, guess):
    word_len = len(list_of_words)
    hangman = "_ "*word_len
    hangman = hangman.split()

    print(list_of_words)

    global i

    #for x in range(0, word_len):
    if guess[0] == list_of_words[i]:
        hangman[i] = guess[0]
    i += 1

    print(hangman)




def is_word_complete():
    pass
"""
def refactored(mode):
    mode_function = eval(mode + "_words")
    mode_function()
    mode_selected = False
    return mode_selected
"""






if __name__ == '__main__':

    mode_selected = True
    while mode_selected == True:
        user_input = input('please type in "easy", "medium", or "hard" to select your game difficulty: ')
        if user_input == "easy":
           # mode_selected = refactored(user_input)
            all_words = easy_words(word_list)
            random_words = random_word(all_words)
            display_words = display_word(random_words)
            mode_selected = False
        elif user_input == "medium":
            #mode_selected = refactored(user_input)
            all_words = medium_words(word_list)
            random_words = random_word(all_words)
            tries = 8


            for x in range(0,8):

                print("you have ", tries," trys left")
                new_guess = (input("what is your guess: ")).split()

                display_words = display_word(random_words, new_guess)
                tries -= 1
            mode_selected = False
        elif user_input == "hard":
            #mode_selected = refactored(user_input)
            all_words = hard_words(word_list)
            random_words = random_word(all_words)
            display_word(random_words)
            mode_selected = False
        else:
            print("you did not type in easy, medium, or hard")













