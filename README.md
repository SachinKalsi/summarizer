Summarizer [![Build Status](https://travis-ci.org/michigan-com/summarizer.svg)](https://travis-ci.org/michigan-com/summarizer)
==========

Summarizer is an automatic summarization algorithm.

Requirements
------------

* Python 2.7, 3.3, or 3.4
* NLTK

Install it
----------

```
pip install summarizer
```

Use it
------

```
from summarizer import summarize
summarize(title, text)
```

Documentation
-------------

Summarizer.summarize(title, text, count=5, summarizer=Summarizer())

* title: The title of the article
* text: The actual text of the article
* count: The number of summarized sentences to return
* summarizer: The class instance that will do all the work

Sanitizer module helps remove common oddities from the body of text.

Sanitizer.sanitize(text)

Contributing
------------

All contributions must be accompanied by some form of unit testing


