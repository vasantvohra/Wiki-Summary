import wikipedia as w  # try https://en.wikipedia.org/wiki/Portal:Current_events
from flask import Flask, request, render_template

def search(phrase):
    try:
        ss=w.summary(phrase, sentences=5, chars=1, auto_suggest=True, redirect=True)
        return(ss)
    except:
        ss="Sorry! not in Wiki"
        return(ss)

