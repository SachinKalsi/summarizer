# -*- coding: utf-8 -*-
import sys
from summarizer import summarize

lines = sys.stdin.readlines()
summary = summarize(lines[0], "\n".join(lines[1:]))
for sentence in summary:
    print(sentence.replace("\n", ""))
