# -*- coding: utf-8 -*-
import os
import unittest

from summarizer import summarize

_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")

class TestSummaries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_files = ['autotech.txt', 'misty.txt', 'morouns.txt']

        cls.autotech = {}
        with open(os.path.join(_dir, 'autotech.txt'), 'r') as fp:
            lines = fp.readlines()
            cls.autotech['title'] = lines[0]
            cls.autotech['text'] = "\n".join(lines[1:])

    def test_autotech_summary(self):
        expected_summary = None
        with open(os.path.join(_dir, 'autotech_s.txt'), 'r') as fp:
            expected_summary = fp.readlines()
        actual_summary = summarize(self.autotech['title'], self.autotech['text'])

        for actual, expected in zip(actual_summary, expected_summary):
            self.assertEqual(actual.replace('\n', ''), expected.replace('\n', ''))

if __name__ == '__main__':
    unittest.run(verbosity=2)
