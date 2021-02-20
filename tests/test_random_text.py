from random_text.random_text import RandomText


def test_get_words():
    text = RandomText()
    word_count = 5
    actual = len(text.get_words(word_count).split(' '))
    expected = word_count
    assert actual == word_count


def test_get_sentences():
    text = RandomText()
    sentence_count = 2
    word_count = 5
    sentence_list = text.get_sentences(sentence_count, word_count).split('. ')
    actual_sentence_count = len(sentence_list)
    words_per_sentence = [len(sentence.split()) for sentence in sentence_list]
    words_match_count = all(count == word_count for count in words_per_sentence)
    assert words_match_count
    assert actual_sentence_count == sentence_count

def test_get_variable_sentences():
    text = RandomText()
    sentence_count = 10
    word_count = 5
    sentence_list = text.get_sentences(sentence_count, word_count, True).split('. ')
    actual_sentence_count = len(sentence_list)
    words_per_sentence = [len(sentence.split()) for sentence in sentence_list]
    words_match_count = all(count == word_count for count in words_per_sentence)
    assert not words_match_count
    assert actual_sentence_count == sentence_count

