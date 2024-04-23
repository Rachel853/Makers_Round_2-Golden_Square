def make_snippet(string):
    if len(string.split(" ")) < 6:
        return string
    return " ".join(string.split(" ")[:5]) + "..."

def count_words(string):
    if len(string) > 0:
        return len(string.split(" "))
    return 0