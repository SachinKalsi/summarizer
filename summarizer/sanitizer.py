# -*- coding: utf-8 -*-
""" News specific helpers to sanitize text. """

def remove_dateline(text):
    """ This will remove the dateline from the beginning of the text. """
    dashes = ["—", "--"]
    truncate = text[:50]

    dateline = -1
    for dash in dashes:
        dateline = truncate.find(dash)
        if dateline >= 0:
            return text[dateline + len(dash):]

    return text
