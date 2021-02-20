from faker import Faker

class RandomText:
    def __init__(self):
        self.fake = Faker()


    def get_words(self, word_count):
        word_list = self.fake.words(nb=word_count, unique=True)
        words = ' '.join(word_list)
        return words


    def get_sentences(self, sentence_count, word_count, variable=False):
        sentences = []
        for _ in range(sentence_count):
            sentences.append(self.fake.sentence(nb_words=word_count, variable_nb_words=variable))
        text = ' '.join(sentences)
        return text
