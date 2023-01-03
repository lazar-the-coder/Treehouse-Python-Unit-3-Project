import random

from phrase import Phrase

phrase_list = [
    'mad lad',
    'electronic hangman',
    'fink and his pinkertons',
    'lo and behond',
    'wheel of fortune'
    ]

phrases = [Phrase(phrase) for phrase in phrase_list]
for phrase in phrases:
    print(phrase.phrase) 
