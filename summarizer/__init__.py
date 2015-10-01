# -*- coding: utf-8 -*-
from .parser import Parser
from .summarizer import Summarizer
from .sanitizer import sanitize

__version__ = '0.0.5'

def summarize(title, text, count=3, sanitize=False, summarizer=None):
    if sanitize:
        text = sanitize(text)

    if not summarizer:
        summarizer = Summarizer()

    result = summarizer.get_summary(text, title)
    result = summarizer.sort_sentences(result[:count])
    result = [res['sentence'] for res in result]

    return result

