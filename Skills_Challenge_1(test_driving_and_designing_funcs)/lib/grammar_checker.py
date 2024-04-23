def grammar_checker(text):
    if text == "" or None:
        raise Exception("No text provided")
    return text[0].isupper() and text[-1] in '.?!'
        