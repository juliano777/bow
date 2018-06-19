#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from string import punctuation as punct
from numpy import zeros as np_zeros

PUNCT = punct.split(' ')


class BagOfWords(object):

    def __init__(self):
        self.vocab = {*()}  # Lista de palavras (set vazio)

    def build_vocab(self, sentences):
        for sentence in sentences:
            for word in sentence.split(' '):
                self.vocab.add(word)

    def sent2array(self, sentence):
        words = {*()}
        for word in sentence.split(' '):
            if word not in PUNCT:
                words.add(word)

        return words

    def vector(self, sentence):
        v = np_zeros(len(self.vocab), dtype=int)

        for word in sentence.split(' '):
            for i, _word in enumerate(self.vocab):
                if _word == word:
                    # print(_word)
                    v[i] = 1
        return v


inputs = [
          'i like it',
          'i hate it',
          'that was good',
          'that was bad',
          'No guts, no glory!',
          'the truth is out there',
          'the book is on the table',
          ]

bow = BagOfWords()

bow.build_vocab(inputs)

inputs.append('the book is on the table')

for sentence in inputs:
    print('{} -> {}'.format(sentence, bow.vector(sentence)))

print(bow.vocab)
