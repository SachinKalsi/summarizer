# -*- coding: utf-8 -*-
import sys
from summarizer import summarize, Parser

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    summary = summarize(lines[0], "".join(lines[1:]))
    for sentence in summary:
        print(sentence.replace("\n", ""))
