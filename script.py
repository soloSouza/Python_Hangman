import random

# Import word list from wordList.txt and store as word_list in the program:
word_list = []
with open("wordList.txt") as wordList_txt:
    for word in wordList_txt:
        word_list.append(word)

# Random word selection for the round:
random_word_index = random.randint(1,len(word_list)+1)
random_word = word_list[random_word_index]

# hangman initial
print(
"""

|--|--------------------s
|  |                    s
|  |                    s
|  |                    s
|  |                    s
|  |                    s
|  |                    s
|  |                   sss
|  |                   sss
|  |                  s   s
|  |                 s     s
|  |                  s s s
|  |                    
|  |               
|  |               
|  |               
|  |                  
|  |                  
|  |                  
|  |                 
|  |                
|  |
|  |
|  |
---------------------------------------
""")

# hangman first-miss:

print(
"""

|--|--------------------s
|  |                    s
|  |                    s
|  |                    s
|  |                    s
|  |                   ooo
|  |                 o     o
|  |                o  O O  o
|  |                o  ---  o
|  |                 o     o
|  |                   sss
|  |            
|  |            
|  |            
|  |            
|  |            
|  |            
|  |            
|  |            
|  |            
|  |            
|  |
|  |
|  |
---------------------------------------
""")

# hangman second-miss:

print(
"""

|--|--------------------s
|  |                    s
|  |                    s
|  |                    s
|  |                    s
|  |                   ooo
|  |                 o     o
|  |                o  O O  o
|  |                o  ---  o
|  |                 o     o
|  |                   sss
|  |                   | |
|  |                   | |
|  |                   | |
|  |                   | |
|  |                   | |
|  |                   | |
|  |                   | |
|  |            
|  |            
|  |            
|  |
|  |
|  |
---------------------------------------
""")

# hangman third-miss:
print(
"""

|--|--------------------s
|  |                    s
|  |                    s
|  |                    s
|  |                    s
|  |                   ooo
|  |                 o     o
|  |                o  O O  o
|  |                o  ---  o
|  |                 o     o
|  |                   sss
|  |                   | |
|  |                  /| |
|  |                 //| |
|  |                // | |
|  |               //  | |
|  |                   | |
|  |                   | |
|  |               
|  |               
|  |               
|  |
|  |
|  |
---------------------------------------
""")

# hangman fourth-miss:
print(
"""

|--|--------------------s
|  |                    s
|  |                    s
|  |                    s
|  |                    s
|  |                   ooo
|  |                 o     o
|  |                o  O O  o
|  |                o  ---  o
|  |                 o     o
|  |                   sss
|  |                   | |
|  |                  /| |
|  |                 //| |
|  |                // | |
|  |               //  | |
|  |                   | |
|  |                   | |
|  |                     \\\\
|  |                      \\\\
|  |                       \\\\
|  |
|  |
|  |
---------------------------------------
""")

# hangman fifth-miss:
print(
"""

|--|--------------------s
|  |                    s
|  |                    s
|  |                    s
|  |                    s
|  |                   ooo
|  |                 o     o
|  |                o  O O  o
|  |                o  ---  o
|  |                 o     o
|  |                   sss
|  |                   | |
|  |                  /| |\\
|  |                 //| |\\\\
|  |                // | | \\\\
|  |               //  | |  \\\\
|  |                   | |
|  |                   | |
|  |                     \\\\
|  |                      \\\\
|  |                       \\\\
|  |
|  |
|  |
---------------------------------------
""")

# hangman game-over:
print(
"""

|--|--------------------s
|  |                    s
|  |                    s
|  |                    s
|  |                    s
|  |                   ooo
|  |                 o     o
|  |                o  x x  o
|  |                o  ...  o
|  |                 o     o
|  |                   sss
|  |                   | |
|  |                  /| |\\
|  |                 //| |\\\\
|  |                // | | \\\\
|  |               //  | |  \\\\
|  |                   | |
|  |                   | |
|  |                  // \\\\
|  |                 //   \\\\
|  |                //     \\\\
|  |
|  |
|  |
---------------------------------------
""")