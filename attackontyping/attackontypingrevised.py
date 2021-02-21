import time
import random
import os
import pyfiglet
from colorama import Fore, Back, Style
from random_text.random_text import RandomText
from timer.timer import Timer
from ascii_art.ascii import welcome_message, lives, easy_ascii, med_ascii, hard_ascii, ext_ascii, game_over_ascii, dev_menu_art, rules_art, thanks
from about.about import logan, anthony, nick, nebiyu

clear = lambda: os.system('clear')


ext_mode = {"descr": "EXTREME MODE", "words": 4, "seconds": "25", "struct": "sentences", "sentences" : 3, "next": None}
hard_mode = {"descr": "HARD MODE", "words": 3, "seconds": "20", "struct": "sentences", "sentences" : 1, "next": ext_mode}
med_mode = {"descr": "MEDIUM MODE", "words": 3, "seconds": "10", "struct": "words", "next": hard_mode}
easy_mode = {"descr": "EASY MODE", "words": 1, "seconds": "15", "struct": "words", "next": med_mode}

class GameLogic:
    def __init__(self):
        self.lives = 3
        self.points = 0
        self.diff = easy_mode

    def reset_game(self):
        self.lives = 3
        self.points = 0
        self.diff = easy_mode

    def next_diff(self):
        self.diff = self.diff["next"]

    
    def get_text(self):
        text = RandomText()
        question = ''
        if self.diff['struct'] == 'words':
            question = text.get_words(self.diff["words"])
        if self.diff["struct"] == 'sentences':
            question = text.get_sentences(self.diff["sentences"], self.diff["words"], True)
        return question
        


    

