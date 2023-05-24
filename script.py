import random

word_list = []
with open("wordList.txt") as wordList_txt:
    for word in wordList_txt:
        word_list.append(word)

