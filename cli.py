# -*- coding: utf-8 -*-
import sys
from summarizer import summarize, Parser

def sentences_from_tokens(tokens):
    sentence = []
    for tok in tokens:
        sentence.append(tok.tok)
        if tok.sentbreak:
            yield " ".join(sentence)
            sentence = []
    if sentence:
        yield " ".join(sentence)


if __name__ == '__main__':
    lines = sys.stdin.readlines()
    parser = Parser()
    tokens = parser.tokens("".join(lines))
    print(list(sentences_from_tokens(tokens)))

    #summary = summarize(lines[0], "".join(lines[1:]))
    #for sentence in summary:
    #    print(sentence.replace("\n", ""))
