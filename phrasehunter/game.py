import random
import string

from phrasehunter import phrase


phrase_list_1 = [
    'gad lad',
    'cat in the hat',
    'bobby fink',
    'lo and behond',
    'John is a master'
    ]

phrase_list = [
    'gad lad'
    ]

class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = phrase_list
        self.active_phrase = None
        self.guesses = []

    def start(self):
        self.welcome()
        self.active_phrase = phrase.Phrase(self.get_random_phrase())
        playing_game = True
        self.active_phrase.display(self.guesses)
        while playing_game:
            self.get_guess()
            self.active_phrase.display(self.guesses)
            if self.active_phrase.check_complete(self.guesses):
                playing_game = False
        self.game_over()

    def welcome(self):
        print('Welcome to the game')

    def get_random_phrase(self):
        return random.choice(phrase_list)

    def get_guess(self):
        guess = input('make a guess' )
        if guess in self.guesses:
            print("You already guessed that")
        elif guess in string.ascii_uppercase or guess in string.ascii_lowercase:
            if self.active_phrase.check_letter(guess):
                print("Correct!")
                self.guesses.append(guess)
            else:
                print("Try Again!")
        else:
            print('not possible')

    def game_over(self):
        print('Congradulations, you won!')


