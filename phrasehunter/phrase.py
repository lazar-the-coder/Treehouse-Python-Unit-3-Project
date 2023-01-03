class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def check_letter(self, letter):
        if letter in self.phrase:
            return True
        else:
            return False
        

    def check_complete(self, guesses):
        if set(list(self.phrase)) - set(guesses) == {' '}:
            return True
        else:
            return False

    def display(self, guesses):
        display_word = []
        for letter in list(self.phrase):
            if letter == ' ':
                display_word.append(' ')
            elif letter in guesses:
                display_word.append(letter)
            else:
                display_word.append('_')
        print(" ".join(display_word))
