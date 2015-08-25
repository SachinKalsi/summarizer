# -*- coding: utf-8 -*-
import os
import unittest

from summarizer import summarize

class TestSummaries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        _dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
        test_files = ['autotech.txt', 'misty.txt', 'morouns.txt']

        cls.autotech = {}
        with open(os.path.join(_dir, 'autotech.txt'), 'r') as fp:
            lines = fp.readlines()
            cls.autotech['title'] = lines[0]
            cls.autotech['text'] = "\n".join(lines[1:])

    def test_autotech_summary(self):
        summary = summarize(self.autotech['title'], self.autotech['text'])
        for sentence in summary:
            self.assertEqual(sentence, sentence)

if __name__ == '__main__':
    unittest.run(verbosity=2)
