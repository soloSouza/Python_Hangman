import random

# Import word list from wordList.txt and store as word_list in the program:
word_list = []
with open("wordList.txt") as wordList_txt:
    for word in wordList_txt:
        word_list.append(word)

# Random word selection for the round:
random_word_index = random.randint(1,len(word_list)+1)
random_word = word_list[random_word_index]
