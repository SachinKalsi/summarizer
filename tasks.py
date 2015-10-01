# -*- coding: utf-8 -*-

from invoke import task
import requests

@task
def article(id):
    r = requests.get('https://api.michigan.com/v1/article/' + id)
    r.raise_for_status()
    article = r.json()

    print(article['headline'])
    print(article['body'])
