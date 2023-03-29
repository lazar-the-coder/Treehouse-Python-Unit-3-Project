import random
import string

from phrase import Phrase


class Game:
    def __init__(self, limit, phrase_list):
        self.missed = 0
        self.limit = limit
        self.phrases = [Phrase(phrase) for phrase in phrase_list]
        self.active_phrase = None
        self.guesses = []

    def start(self):
        self.welcome()
        self.active_phrase = self.get_random_phrase()
        self.missed = 0
        self.guesses = []
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
        self.active_phrase.display(self.guesses)
        self.game_over(win)

    def welcome(self):
        print("----Welcome, player, to the game", 
              "\n---You must uncover a phrase by guessing one letter at a time",
              f"\n-You have {self.limit} tries\n\n")

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def get_guess(self):
        guess = input("make a guess\n  ").lower()
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
                print(f"You've answered wrong {self.missed} times out of {self.limit},\n You have {self.limit - self.missed} guesses left.\n")
        else:
            print('please enter a letter')

    def game_over(self, win):
        if win:
            print('Congradulations, you did it! Great job!')
        else:
            print('You\'ve failed, Game over. But don\'t give up!')
        while True:
            play_again = input("would you like to play again? y/n").lower()
            if play_again == "y":
                break
            else:
                print('Alright, good bye!')
                quit()
        self.start()



