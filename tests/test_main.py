import unittest

from application import main


def test_sample_single_word():
    l = ('foo', 'bar', 'foobar')
    word = main.sample(l)
    assert word in l


def test_sample_multiple_words():
    l = ('foo', 'bar', 'foobar')
    words = main.sample(l, 2)
    assert len(words) == 2
    assert words[0] in l
    assert words[1] in l
    assert words[0] is not words[1]
