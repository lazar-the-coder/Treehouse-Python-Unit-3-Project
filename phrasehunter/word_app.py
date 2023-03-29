import game
import phrase
import json
import string


phrase_list = []

def load_json():
    with open("phrasehunter/phrase_list.json") as phrasefile:
        all_phrases = json.load(phrasefile)
        for full_phrase in all_phrases["checked phrases"]:
            phrase_list.append(full_phrase)

def save_to_json(phrase):
    with open("phrasehunter/phrase_list.json") as phrasefile:
        all_phrases = json.load(phrasefile)
    with open("phrasehunter/phrase_list.json", "w") as phrasefile:
        all_phrases["new phrases"].append(phrase)
        json.dump(all_phrases, phrasefile)

def limit_getter():
    limit = input("how many tries do you get?  ")
    entering_limit = True
    while entering_limit:
        try:
            limit = int(limit)
            if limit > 0:
                entering_limit = False
            else:
                limit = input("Please enter a whole number above 1  ")
        except ValueError:
            limit = input("Please enter a whole number above 1  ")
    print ("you have", limit, "tries")
    return limit

def play(game_play):
    load_json()
    limit = limit_getter()
    game_start = game_play.Game(limit, phrase_list)
    game_start.start()

def add_phrase():
    phrase = input("What is the phrase you want to add?   ")
    entering_phrase = True
    while entering_phrase:
        if set(list(phrase)).issubset(set(string.ascii_letters).union({' '})):
            save_to_json(phrase.lower())
            entering_phrase = False
        else:
            phrase = input("Please enter a phrase with letters and spaces only   ")

def start():
    running = True
    while running:
        choice = menu_choice()
        match choice:
            case 'g':
                play(game)
            case 'a':
                add_phrase()
            case 'q':
                running = False
                print('Alright')

def menu_choice():
    print('''
          \rG) Start a New game
          \rA) Add a Phrase
          \rQ) Quit
          ''')
    while True:
        choice = input('What do you want to do?   ')
        try:
            if choice.lower() in ['g', 'a', 'q']:
                return choice.lower()
            else:
                print('Sorry, didn\'t understand. Please enter a valid choice.')
        except ValueError:
            print('Sorry, didn\'t understand. Please enter a valid choice.')
            

if __name__ == "__main__":
    start()
