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
        return

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
        text = u"If you don't stop right now the F.B.I. will repremand you, bitch.  The U.S. doesn't earn respect, it takes it. Don't fuck with the N.S.A. or you'll feel our wrath.  My initials E.R.B. are swell."

        expected_sentences = [
            u"If you don't stop right now the F.B.I. will repremand you, bitch.",
            u"The U.S. doesn't earn respect, it takes it.",
            u"Don't fuck with the N.S.A. or you'll feel our wrath.",
            u"My initials E.R.B. are swell.",
        ]

        actual_sentences = self.parser.sentences(text)

        self.assertEqual(len(actual_sentences), len(expected_sentences))

        for actual, expected in zip(actual_sentences, expected_sentences):
            self.assertEqual(actual, expected)

    def test_multi_punct_words_sentence_enders(self):
        text = u"This is the F.B.I.  We work for the U.S.  It's funny because it's true."

        expected_sentences = [
            u"This is the F.B.I.",
            u"We work for the U.S.",
            u"It's funny because it's true.",
        ]

        actual_sentences = self.parser.sentences(text)

        self.assertEqual(len(actual_sentences), len(expected_sentences))

        for actual, expected in zip(actual_sentences, expected_sentences):
            self.assertEqual(actual, expected)

    def test_special_quote_period_sentence_enders(self):
        text = u"“I’m guilty.” Another man, Jasin Curtis, 19, also pleaded guilty and was sentenced in June to 27-40 years for robbery and murder.  'Do you get it?'  I don't think you do."

        expected_sentences = [
            u"“I’m guilty.”",
            u"Another man, Jasin Curtis, 19, also pleaded guilty and was sentenced in June to 27-40 years for robbery and murder.",
            u"'Do you get it?'",
            u"I don't think you do.",
        ]

        actual_sentences = self.parser.sentences(text)

        self.assertEqual(len(actual_sentences), len(expected_sentences))

        for actual, expected in zip(actual_sentences, expected_sentences):
            self.assertEqual(actual, expected)

    def test_gov_abbrev(self):
        text = u"Our Gov. is a piece of shit.  He can't do anything right."

        expected_sentences = [
            "Our Gov. is a piece of shit.",
            "He can't do anything right."
        ]

        actual_sentences = self.parser.sentences(text)

        self.assertEqual(len(actual_sentences), len(expected_sentences))

        for actual, expected in zip(actual_sentences, expected_sentences):
            self.assertEqual(actual, expected)

    def test_sgt_abbrev(self):
        text = u"I was a Sgt. in the flying spaghetti monster army.  It was alright."

        expected_sentences = [
            "I was a Sgt. in the flying spaghetti monster army.",
            "It was alright."
        ]

        actual_sentences = self.parser.sentences(text)

        self.assertEqual(len(actual_sentences), len(expected_sentences))

        for actual, expected in zip(actual_sentences, expected_sentences):
            self.assertEqual(actual, expected)

    def test_no_abbrev(self):
        text = u"I'm No. 1 bitches.  Suck an egg."

        expected_sentences = [
            "I'm No. 1 bitches.",
            "Suck an egg."
        ]

        actual_sentences = self.parser.sentences(text)

        self.assertEqual(len(actual_sentences), len(expected_sentences))

        for actual, expected in zip(actual_sentences, expected_sentences):
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.run(verbosity=2)


