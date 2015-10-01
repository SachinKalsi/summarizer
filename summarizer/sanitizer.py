# -*- coding: utf-8 -*-
""" News specific helpers to sanitize text. """

def sanitize(text):
    """ Preprocessing for common issues found in news articles. """
    text = remove_dateline(text)
    return text

def remove_dateline(text):
    """ This will remove the dateline from the beginning of the text. """
    dashes = [u"—", u"--"]
    truncate = text[:50]

    dateline = -1
    for dash in dashes:
        dateline = truncate.find(dash)
        if dateline >= 0:
            return text[dateline + len(dash):]

    return text
