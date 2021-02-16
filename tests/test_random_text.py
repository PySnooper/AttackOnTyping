import string
from attackontyping.random_text import RandomText


def test_easy_text():
    text = RandomText()
    actual = len(text.get_easy_text().split())
    expected = text.easy_word_count
    assert actual == expected


def test_medium_text():
    text = RandomText()
    actual = len(text.get_medium_text().split())
    expected = text.medium_word_count
    assert actual == expected


def test_hard_text():
    text = RandomText()
    actual_sentences = text.get_hard_text().split('.')
    actual_sentences.remove('')
    expected_sentence_length = text.hard_sent_count
    right_length = all(len(sent.split()) == text.hard_word_count for sent in actual_sentences)
    assert len(actual_sentences) == expected_sentence_length
    assert right_length


def test_extreme_text():
    text = RandomText()
    actual_sentences = text.get_extreme_text().split('.')
    actual_sentences.remove('')
    expected_sentence_length = text.extreme_sent_count
    right_length = all(len(sent.split()) == text.extreme_word_count for sent in actual_sentences)
    assert len(actual_sentences) == expected_sentence_length
    assert right_length