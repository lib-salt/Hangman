#
import random
from WordBank import word
import string


# Selects a word at random for the player to guess
def get_word(word):
    w = random.choice(word)
    return w


# Runs the hangman game
def hangman():
    w = get_word(word)
    letters = set(w)
    alphabet = set(string.ascii_lowercase)
    user_guesses = set()
    guesses = 12

    while len(letters) > 0 and guesses > 0:
        # user guesses
        print("Lives remaining:", guesses)
        print("Letters Guessed: ", " ".join(user_guesses))
        # Prints any guessed letters and dashes show remaining letters
        w_list = [letter if letter in user_guesses else "-" for letter in w]
        print("word: ", " ".join(w_list))

        # Asks user to input their guess
        player_input = input("Guess a letter:").lower()
        if player_input in alphabet - user_guesses:
            user_guesses.add(player_input)
            if player_input in letters:
                letters.remove(player_input)
            else:
                # If the guess is incorrect the player loses a life
                guesses = guesses - 1
                print("sorry the word does not contain that letter")

        elif player_input in user_guesses:
            print("You have already guessed this letter. Please choose again.")

        else:
            print("Incorrect guess. Please try again.")

    if guesses == 0:
        # Will print if the user runs out of lives
        print("Sorry you have run out of lives. The word was ", w)
    else:
        # Will print if the user correctly guesses the word
        print("Well done. You have correctly guessed the word,", w)


if __name__ == '__main__':
    hangman()
"""
 Reference:
 Code from github user kying18 was used. Code was not copied verbatim as some naming was changed and I produced my own 
 word bank.
 URL: https://github.com/kying18/hangman
"""