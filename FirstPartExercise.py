__author__ = 'hamouy'


def match_ends(words):
    compt = 0
    for word in words:
        len_word = len(word)
        if len_word >= 2:
            if  word[0] == word[len_word-1]:
                compt += 1
    return compt


def front_x(words):
    list1 = list(words)
    list2=[]
    for word in words:
        if word[0] == "x":
            list2.append(word)
            list1.remove(word)
            continue
    list1 = sorted(list1)
    list2 = sorted(list2)
    return list2 + list1
