# -*- coding: utf-8 -*-
import os
import unittest

from summarizer import sanitizer

_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")

def _u(s):
    _str = s
    try:
        _str = _str.decode('utf-8', 'ignore')
    except AttributeError:
        pass
    return _str

class TestSanitizer(unittest.TestCase):
    def test_removing_dateline(self):
        for i in range(3):
            actual_text = None
            with open(os.path.join(_dir, 'dateline_' + str(i+1) + '.txt'), 'r') as fp:
                lines = fp.readlines()
                actual_text = sanitizer.remove_dateline(_u("".join(lines[1:])))

            expected_text = None
            with open(os.path.join(_dir, 'dateline_' + str(i+1) + '_expected.txt'), 'r') as fp:
                lines = fp.readlines()
                expected_text = _u(fp.readlines())

if __name__ == '__main__':
    unittest.run(verbosity=2)

