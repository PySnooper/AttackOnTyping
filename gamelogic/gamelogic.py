import random
from random_text.random_text import RandomText
from colorama import Fore, Back, Style
from ascii_art.ascii import easy_ascii, med_ascii, hard_ascii, ext_ascii


hard_warning = '********************************************\n' \
            + Fore.YELLOW \
            + 'You now have capital letters and punctuation\n' \
            + Style.RESET_ALL \
            + '********************************************\n'

ext_warning = '***********************************************************************\n' \
            + Fore.YELLOW \
            + 'You now have capital letters, punctuation, and random length sentences!\n' \
            + Style.RESET_ALL \
            + '***********************************************************************\n'



class GameLogic:
    ext_mode = {"descr": "EXTREME MODE", "words": 5, "seconds": 20, "struct": "sentences", "sentences" : 3, "next": None, "point_cap": 80, "warning": ext_warning, "ascii": ext_ascii, "points_per": 10}
    hard_mode = {"descr": "HARD MODE", "words": 5, "seconds": 10, "struct": "sentences", "sentences" : 1, "next": ext_mode, "point_cap": 60, "warning": hard_warning, "ascii": hard_ascii, "points_per": 10}
    med_mode = {"descr": "MEDIUM MODE", "words": 3, "seconds": 10, "struct": "words", "next": hard_mode, "point_cap": 40, "warning": None, "ascii": med_ascii, "points_per": 10}
    easy_mode = {"descr": "EASY MODE", "words": 1, "seconds": 10, "struct": "words", "next": med_mode, "point_cap": 20, "warning": None, "ascii": easy_ascii, "points_per": 10}

    def __init__(self):
        self.lives = 3
        self.points = 0
        self.diff = self.easy_mode

    def reset_game(self):
        self.lives = 3
        self.points = 0
        self.diff = self.easy_mode

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

    def set_diff(self, difficulty):
        self.reset_game()
        self.diff = difficulty