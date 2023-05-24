
game_header = """ 
------------------------------------------------------------------------------------------------
|XX|--------------------s
|XX|                    s
|XX|                   sss 
|XX|                   sss
|XX|                  s   s 
|XX|                 s     s
|XX|                  s s s
|XX|
|XX|  WELCOME TO:
|XX|
|XX|  TTTTTTT  H     H  EEEEEEE    H     H     A     N     N   GGGGG   M     M     A     N     N
|XX|     T     H     H  E          H     H    A A    NN    N  G     G  MM   MM    A A    NN    N
|XX|     T     H     H  E          H     H   A   A   N N   N  G        M M M M   A   A   N N   N
|XX|     T     HHHHHHH  EEEEE      HHHHHHH  AAAAAAA  N  N  N  G  GGGG  M  M  M  AAAAAAA  N  N  N 
|XX|     T     H     H  E          H     H  A     A  N   N N  G  G  G  M     M  A     A  N   N N
|XX|     T     H     H  E          H     H  A     A  N    NN  G     G  M     M  A     A  N    NN
|XX|     T     H     H  EEEEEEE    H     H  A     A  N     N   GGGGG   M     M  A     A  N     N
|XX|   
------------------------------------------------------------------------------------------------   
"""
hangman_initial = """
|XX|--------------------s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                   sss
|XX|                   sss
|XX|                  s   s
|XX|                 s     s
|XX|                  s s s
|XX|                    
|XX|               
|XX|               
|XX|               
|XX|                  
|XX|                  
|XX|                  
|XX|                 
|XX|                
|XX|
|XX|
|XX|
---------------------------------------
"""
hangman_one_miss = """
|XX|--------------------s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                   ooo
|XX|                 o     o
|XX|                o  O O  o
|XX|                o  ---  o
|XX|                 o     o
|XX|                   sss
|XX|            
|XX|            
|XX|            
|XX|            
|XX|            
|XX|            
|XX|            
|XX|            
|XX|            
|XX|            
|XX|
|XX|
|XX|
---------------------------------------
"""
hangman_two_misses = """
|XX|--------------------s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                   ooo
|XX|                 o     o
|XX|                o  O O  o
|XX|                o  ---  o
|XX|                 o     o
|XX|                   sss
|XX|                   |z|
|XX|                   |z|
|XX|                   |z|
|XX|                   |z|
|XX|                   |z|
|XX|                   |z|
|XX|                   |z|
|XX|            
|XX|            
|XX|            
|XX|
|XX|
|XX|
---------------------------------------
"""
hangman_three_misses = """

|XX|--------------------s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                   ooo
|XX|                 o     o
|XX|                o  O O  o
|XX|                o  ---  o
|XX|                 o     o
|XX|                   sss
|XX|                   |z|
|XX|                  /|z|
|XX|                 //|z|
|XX|                // |z|
|XX|               //  |z|
|XX|              '''  |z|
|XX|                   |z|
|XX|               
|XX|               
|XX|               
|XX|
|XX|
|XX|
---------------------------------------
"""
hangman_four_misses ="""
|XX|--------------------s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                   ooo
|XX|                 o     o
|XX|                o  O O  o
|XX|                o  ---  o
|XX|                 o     o
|XX|                   sss
|XX|                   |z|
|XX|                  /|z|
|XX|                 //|z|
|XX|                // |z|
|XX|               //  |z|
|XX|              '''  |z|
|XX|                   |z|
|XX|                     \\\\
|XX|                      \\\\
|XX|                       \\\\
|XX|                       ''''
|XX|
|XX|
---------------------------------------
"""
hangman_five_misses = """
|XX|--------------------s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                   ooo
|XX|                 o     o
|XX|                o  O O  o
|XX|                o  ---  o
|XX|                 o     o
|XX|                   sss
|XX|                   |z|
|XX|                  /|z|\\
|XX|                 //|z|\\\\
|XX|                // |z| \\\\
|XX|               //  |z|  \\\\
|XX|              '''  |z|  '''
|XX|                   |z|
|XX|                     \\\\
|XX|                      \\\\
|XX|                       \\\\
|XX|                       ''''
|XX|
|XX|
---------------------------------------
"""
hangman_six_misses = """
|XX|--------------------s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                   ooo
|XX|                 o     o
|XX|                o  o o  o
|XX|                o  ---  o
|XX|                 o     o
|XX|                   sss
|XX|                   |z|
|XX|                  /|z|\\
|XX|                 //|z|\\\\
|XX|                // |z| \\\\
|XX|               //  |z|  \\\\
|XX|              '''  |z|  '''
|XX|                   |z|
|XX|                  // \\\\
|XX|                 //   \\\\
|XX|                //     \\\\
|XX|              ''''     ''''
|XX|
|XX|
---------------------------------------
"""
hangman_game_over = """
|XX|--------------------s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                    s
|XX|                   ooo
|XX|                 o     o
|XX|                o  x x  o
|XX|                o  ...  o
|XX|                 o     o
|XX|                   sss
|XX|                   |z|
|XX|                  /|z|\\
|XX|                 //|z|\\\\
|XX|                // |z| \\\\
|XX|               //  |z|  \\\\
|XX|              '''  |z|  '''
|XX|                   |z|
|XX|                  // \\\\
|XX|                 //   \\\\
|XX|                //     \\\\
|XX|              ''''     ''''
|XX|
|XX|
---------------------------------------
"""
import random

# Import word list from wordList.txt and store as word_list in the program:
word_list = []
with open("wordList.txt") as wordList_txt:
    for word in wordList_txt:
        word_list.append(word)

# Random word selection for the round:
random_word_index = random.randint(1,len(word_list))
random_word = word_list[random_word_index]

print(game_header)
print("\"THE HANGMAN\" is a single player terminal game.\n")
start_game = input("Would you like to start a new game? (y/n): ")