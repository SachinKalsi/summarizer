# -*- coding: utf-8 -*-
import os
import unittest

from summarizer import summarize

_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")

def _read_expected_summary(fname, _dir=_dir):
    expected_summary = None
    with open(os.path.join(_dir, fname), 'r') as fp:
        expected_summary = fp.readlines()
    return expected_summary


class TestSummaries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_files = ['autotech.txt', 'misty.txt', 'morouns.txt']

        cls.autotech = {}
        with open(os.path.join(_dir, 'autotech.txt'), 'r') as fp:
            lines = fp.readlines()
            cls.autotech['title'] = lines[0]
            cls.autotech['text'] = "".join(lines[1:])

        cls.misty = {}
        with open(os.path.join(_dir, 'misty.txt'), 'r') as fp:
            lines = fp.readlines()
            cls.misty['title'] = lines[0]
            cls.misty['text'] = "".join(lines[1:])

        cls.morouns = {}
        with open(os.path.join(_dir, 'morouns.txt'), 'r') as fp:
            lines = fp.readlines()
            cls.morouns['title'] = lines[0]
            cls.morouns['text'] = "".join(lines[1:])

    def test_autotech_summary(self):
        expected_summary = _read_expected_summary('autotech_s.txt')
        actual_summary = summarize(self.autotech['title'], self.autotech['text'])

        for actual, expected in zip(actual_summary, expected_summary):
            self.assertEqual(actual.replace('\n', ''), expected.replace('\n', ''))

    def test_misty_summary(self):
        expected_summary = _read_expected_summary('misty_s.txt')
        actual_summary = summarize(self.misty['title'], self.misty['text'])

        for actual, expected in zip(actual_summary, expected_summary):
            self.assertEqual(actual.replace('\n', ''), expected.replace('\n', ''))

    def test_morouns_summary(self):
        expected_summary = _read_expected_summary('morouns_s.txt')
        actual_summary = summarize(self.morouns['title'], self.morouns['text'])

        for actual, expected in zip(actual_summary, expected_summary):
            self.assertEqual(actual.replace('\n', ''), expected.replace('\n', ''))

if __name__ == '__main__':
    unittest.run(verbosity=2)

