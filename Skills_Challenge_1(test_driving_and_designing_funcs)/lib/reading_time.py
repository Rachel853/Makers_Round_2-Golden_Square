import re

def estimate_reading_time(text):
    if text == "" or text == None:
        raise Exception("No text provided")
    words = text.split(' ')
    number_words = len(words)
    minutes_required = round(number_words/200)
    plural = ""
    if minutes_required != 1:
        plural += 's'
    return str(minutes_required) + " minute" + plural