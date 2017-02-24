__author__ = 'hamouy'


def match_ends(words):
    # +++your code here+++
    compt = 0
    for word in words:
        len_word = len(word)
        if len_word >= 2:
            if  word[0] == word[len_word-1]:
                compt += 1
    return compt


def front_x(words):

    # +++your code here+++
    return
