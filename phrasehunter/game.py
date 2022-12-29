import random
import string

from phrasehunter import phrase


phrase_list = [
    'gad lad',
    'cat in the hat',
    'bobby fink',
    'lo and behond',
    'John is a master'
    ]

class Game:
    def __init__(self):
        self.missed = 0
        self.limit = 5
        self.phrases = phrase_list
        self.active_phrase = None
        self.guesses = []

    def start(self):
        self.welcome()
        self.active_phrase = phrase.Phrase(self.get_random_phrase())
        playing_game = True
        while playing_game:
            self.active_phrase.display(self.guesses)
            self.get_guess()
            if self.active_phrase.check_complete(self.guesses):
                playing_game = False
                win = True
            if self.missed == self.limit:
                playing_game = False
                win = False
        self.game_over(win)

    def welcome(self):
        print('Welcome to the game')

    def get_random_phrase(self):
        return random.choice(phrase_list)

    def get_guess(self):
        guess = input('make a guess' ).lower()
        if len(guess) != 1:
            print("please enter 1 letter as a guess, no more, no less.")
        elif guess.lower() in string.ascii_lowercase:
            if guess in self.guesses:
                print("You already guessed that")
            elif self.active_phrase.check_letter(guess):
                print("Correct!")
                self.guesses.append(guess)
            else:
                print("Wrong!")
                self.missed += 1
                print(f"You've answered wrong {self.missed} out of {self.limit} times")
        else:
            print('not possible')

    def game_over(self, win):
        if win:
            print('Congradulations, you won!')
        else:
            print('You have failed!')
        while True:
            play_again = input("would you like to play again? y/n").lower()
            if play_again == "y":
                break
            else:
                print('Alright, good bye!')
                quit()
        self.start()



