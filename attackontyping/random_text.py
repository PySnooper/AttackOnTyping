import string
from faker import Faker

class RandomText:
    def __init__(self):
        self.easy_word_count = 5
        self.medium_word_count = 10
        self.hard_word_count = 10
        self.extreme_word_count = 10
        self.hard_sent_count = 2
        self.extreme_sent_count = 5
        self.fake = Faker().unique
        pass

    def get_easy_text(self):
        text = self.fake.sentence(nb_words=self.easy_word_count,variable_nb_words=False)
        text = text.translate(str.maketrans('', '', string.punctuation)).lower()
        return text

    def get_medium_text(self):
        text = self.fake.sentence(nb_words=self.medium_word_count,variable_nb_words=False)
        text = text.translate(str.maketrans('', '', string.punctuation)).lower()
        return text

    def get_hard_text(self):
        sentences = []
        for _ in range(self.hard_sent_count):
            sentences.append(self.fake.sentence(nb_words=self.hard_word_count,variable_nb_words=False))
        text = ' '.join(sentences)
        return text

    def get_extreme_text(self):
        sentences = []
        for _ in range(self.extreme_sent_count):
            sentences.append(self.fake.sentence(nb_words=self.extreme_word_count,variable_nb_words=False))
        text = ' '.join(sentences)
        return text