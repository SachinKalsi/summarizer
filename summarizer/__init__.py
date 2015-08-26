# -*- coding: utf-8 -*-
from .summarizer import Summarizer

__version__ = '0.0.2'

def summarize(title, text, count=5, summarizer=Summarizer()):
    result = summarizer.get_summary(text, title)
    result = summarizer.sort_sentences(result[:count])
    result = [res['sentence'] for res in result]

    return result

