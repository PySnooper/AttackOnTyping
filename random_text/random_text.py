from faker import Faker

class RandomText:
    """[Initialize Faker method]
    """    
    def __init__(self):
        self.fake = Faker()


    def get_words(self, word_count):
        """[Take in a word Count creates a series of random strings to be returned.]

        Args:
            word_count ([int]): [Number to indicate how many random words need to be generated for the user.]

        Returns:
            [str]: [Series of random strings based on the word_count input.]
        """        
        word_list = self.fake.words(nb=word_count, unique=True)
        words = ' '.join(word_list)
        return words


    def get_sentences(self, sentence_count, word_count, variable=False):

        """[Take in a sentence_count and word_count to create a series of random strings and sentences to be returned, with capital letters and punctuation.]

        Args:
            word_count ([int]): [Number to indicate how many random words need to be generated per sentence.]
            sentence_count ([int]): [Number to indicate how many sentences need to be generated for the user.]

        Returns:
            [str]: [Series of random strings as sentences based on the word_count and sentence_count inputs.]
        """        
        sentences = []
        for _ in range(sentence_count):
            sentences.append(self.fake.sentence(nb_words=word_count, variable_nb_words=variable))
        text = ' '.join(sentences)
        return text
