# -*- coding: utf-8 -*-
import os
import unittest
import requests

from summarizer import Parser, sanitize

_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")

class TestSentences(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = Parser()

    def test_approved_articles(self):
        r = requests.get('http://brevity.detroitnow.io/articles/valid-tokens/')
        r.raise_for_status()
        data = r.json()

        for article in data['articles']:
            r = requests.get('https://api.michigan.com/v1/article/' + str(article['article_id']))
            r.raise_for_status()
            art_jso = r.json()

            body = art_jso['body']
            body = sanitize(body)

            actual_sentences = self.parser.sentences(body)
            expected_sentences = article['sentences']

            self.assertEqual(len(actual_sentences), len(expected_sentences))

            for actual_s, expected_s in zip(actual_sentences, expected_sentences):
                self.assertEqual(actual_s, expected_s)

    def test_multi_punct_words_not_sentence_enders(self):
        text = """If you don't stop right now the F.B.I. will repremand you, bitch.  The U.S. doesn't earn respect, it takes it. Don't fuck with the N.S.A. or you'll feel our wrath.  My initials E.R.B. are swell."""

        expected_sentences = [
            "If you don't stop right now the F.B.I. will repremand you, bitch.",
            "The U.S. doesn't earn respect, it takes it.",
            "Don't fuck with the N.S.A. or you'll feel our wrath.",
            "My initials E.R.B. are swell.",
        ]

        actual_sentences = self.parser.sentences(text)

        self.assertEqual(len(actual_sentences), len(expected_sentences))

        for actual, expected in zip(actual_sentences, expected_sentences):
            self.assertEqual(actual, expected)

    def test_multi_punct_words_sentence_enders(self):
        text = """This is the F.B.I.  We work for the U.S.  It's funny because it's true."""

        expected_sentences = [
            "This is the F.B.I.",
            "We work for the U.S.",
            "It's funny because it's true.",
        ]

        actual_sentences = self.parser.sentences(text)

        self.assertEqual(len(actual_sentences), len(expected_sentences))

        for actual, expected in zip(actual_sentences, expected_sentences):
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.run(verbosity=2)


