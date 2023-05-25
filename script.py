import random

# variables:
page_break = """
-----------------------------------------------------------------------------------------------------------------------
"""
game_header = """ 
Welcome to:

|XX|--------------------s
|XX|                    s
|XX|                   sss 
|XX|                   sss        
|XX|                  s   s 
|XX|                 s     s   
|XX|                  s s s    
|XX|
|XX|  TTTTTTT  H     H  EEEEEEE    H     H     A     N     N   GGGGG   M     M     A     N     N
|XX|     T     H     H  E          H     H    A A    NN    N  G     G  MM   MM    A A    NN    N
|XX|     T     H     H  E          H     H   A   A   N N   N  G        M M M M   A   A   N N   N
|XX|     T     HHHHHHH  EEEEE      HHHHHHH  AAAAAAA  N  N  N  G  GGGG  M  M  M  AAAAAAA  N  N  N 
|XX|     T     H     H  E          H     H  A     A  N   N N  G  G  G  M     M  A     A  N   N N
|XX|     T     H     H  E          H     H  A     A  N    NN  G     G  M     M  A     A  N    NN
|XX|     T     H     H  EEEEEEE    H     H  A     A  N     N   GGGGG   M     M  A     A  N     N
|XX|   

\"THE HANGMAN\" is a single player terminal game.
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
"""
hangman_seven_misses = """
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
"""
hangman_game_over = """

|XX|--------------------s        
|XX|                    s        
|XX|                   sss       
|XX|                   sss       
|XX|                  s   s      
|XX|                 s     s     
|XX|                  s s s       
|XX|          
|XX|   GGGGG      A     M     M  EEEEEEE    OOO    V     V  EEEEEEE  RRRRR      !!!  !!!  !!!                         
|XX|  G     G    A A    MM   MM  E        O     O  V     V  E        R     R    !!!  !!!  !!!                  
|XX|  G         A   A   M M M M  E        O     O  V     V  E        R     R    !!!  !!!  !!!                  
|XX|  G  GGGG  AAAAAAA  M  M  M  EEEEE    O     O  V     V  EEEEE    RRRRR      !!!  !!!  !!!                      
|XX|  G  G  G  A     A  M     M  E        O     O   V   V   E        R   R      !!!  !!!  !!!                  
|XX|  G     G  A     A  M     M  E        O     O    V V    E        R    R                        
|XX|   GGGGG   A     A  M     M  EEEEEEE    OOO       V     EEEEEEE  R     R    !!!  !!!  !!!                        
|XX|   

"""
hangman_you_win = """

|XX|--------------------s
|XX|                    s
|XX|                   sss 
|XX|                   sss        
|XX|                  s   s 
|XX|                 s     s   
|XX|                  s s s    
|XX|          
|XX|  Y     Y    OOO    U     U    W     W  IIIIIII  N     N    !!!  !!!  !!!
|XX|   Y   Y   O     O  U     U    W     W     I     NN    N    !!!  !!!  !!!
|XX|    Y Y    O     O  U     U    W     W     I     N N   N    !!!  !!!  !!!
|XX|     Y     0     O  U     U    W  W  W     I     N  N  N    !!!  !!!  !!!
|XX|     Y     O     O  U     U    W W W W     I     N   N N    !!!  !!!  !!!
|XX|     Y     O     O  U     U    WW   WW     I     N    NN  
|XX|     Y       OOO      UUU      W     W  IIIIIII  N     N    !!!  !!!  !!!
|XX|

"""
word_list = []
word_as_list = []
guesses_as_list = []
guesses_as_string = ""
misses_counter = 0
possible_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
past_guesses = []
guess_counter = 0
game_word = ""

# Import word list from wordList.txt and store as word_list in the program:
with open("wordList.txt") as wordList_txt:
    for word in wordList_txt:
        word_list.append(word.upper().rstrip())

# select_word function chooses a random word from the word list for the roun and creates initial guess as list:
def select_word():
    word_index = random.randint(1,len(word_list))
    word = word_list[word_index]
    word_list.remove(word)
    for letter in word:
        word_as_list.append(letter)
    for letter in word:
        guesses_as_list.append(" ")
    return word

# update player guess_list to be displayed as string during game:
def update_guess_as_string(word_as_list, guesses_as_list, guesses_as_string):
    for i in range(len(word_as_list)):
        if guesses_as_list[i] == word_as_list[i]:
            guesses_as_string += " {value}".format(value = guesses_as_list[i])
        else:
            guesses_as_string += " _"
    return guesses_as_string

# start_new_game function asks for user (Y/N) input and catches any exception asking for a valid answer.
def start_new_game():
    player_input = input("Would you like to start a new game? (Y/N): ")
    if player_input.upper() == "Y" or player_input.upper() == "N":
        if player_input.upper() == "Y":
            game_word = select_word()
            print(page_break)
            print("Great, let's play:\n")
            print("You can type \"EXIT\" at any time to quit the game.\n")
            print(hangman_initial)
            print("I've selected a word of {letter_count} letters for you to try and guess before being hanged: {string}".format(letter_count = len(game_word), string = update_guess_as_string(word_as_list, guesses_as_list, guesses_as_string)))
        else:
            print(page_break)
            print("\nI'm sad to see you leave! Come back at any time.\n")
            quit()    
    else:
        print(page_break)
        print("\nOops, it seems like you did not provide a valid answer, please try again:")
        start_new_game()

# print visual aid according to miss_counter:
def insert_visual_aid(misses_counter):
    if misses_counter == 0:
        print(hangman_initial)
    elif misses_counter == 1:
        print(hangman_one_miss)
    elif misses_counter == 2:
        print(hangman_two_misses)
    elif misses_counter == 3:
        print(hangman_three_misses)
    elif misses_counter == 4:
        print(hangman_four_misses)
    elif misses_counter == 5:
        print(hangman_five_misses)
    elif misses_counter == 6:
        print(hangman_six_misses)
    elif misses_counter == 7:
        print(hangman_seven_misses)
    else:
        print("This is an error message")

# gameplay function:
def play_game(word_as_list, guesses_as_list, guesses_as_string, misses_counter, possible_letters, past_guesses, guess_counter):
    while word_as_list != guesses_as_list and misses_counter <= 7:
        if guess_counter == 0:
            print(page_break)
            player_guess = input("What is your first guess: ")
        else:
            print(page_break)
            player_guess = input("What is your next guess: ")
        if player_guess.upper() == "EXIT":
            quit()
        else:
            if player_guess.upper() in possible_letters:
                if player_guess.upper() not in past_guesses:
                    if player_guess.upper() not in word_as_list:
                        misses_counter += 1
                        guess_counter += 1
                        if misses_counter == 8:
                            word = ""
                            for i in range(len(word_as_list)):
                                word += word_as_list[i]
                            print(page_break)
                            print("Sorry, but my word was {word} and {letter} is not part of it: {string}".format(word = word, letter = player_guess.upper(), string = update_guess_as_string(word_as_list, guesses_as_list, guesses_as_string)))
                            print(hangman_game_over)
                            break
                        else: 
                            past_guesses.append(player_guess.upper())
                            print(page_break)
                            print("Sorry, but {letter} is not in my word: {string}".format(letter = player_guess.upper(), string = update_guess_as_string(word_as_list, guesses_as_list, guesses_as_string)))
                            insert_visual_aid(misses_counter)
                            past_guesses_string = ""
                            for i in past_guesses:
                                past_guesses_string += i + " "
                            if guess_counter > 1:
                                print("You have made {number} guess so far: {letters}".format(number = guess_counter, letters = past_guesses_string))
                                print("Wrong guesses: {x}".format(x = misses_counter))
                                print("Correct guesses: {x}".format(x = (guess_counter-misses_counter)))
                            else:
                                print("You have made {number} guess so far: {letters}".format(number = guess_counter, letters = past_guesses_string))
                                print("Wrong guesses: {x}".format(x = misses_counter))
                                print("Correct guesses: {x}".format(x = (guess_counter-misses_counter)))
                    if player_guess.upper() in word_as_list:
                        guess_counter += 1
                        past_guesses.append(player_guess.upper())
                        for i in range(len(word_as_list)):
                            if word_as_list[i] == player_guess.upper():
                                guesses_as_list[i] = player_guess.upper()
                        if guesses_as_list == word_as_list:
                            word = ""
                            for i in range(len(word_as_list)):
                                word += word_as_list[i]
                            print(page_break)
                            print("Good job! My word was {word} and ir does contain the letter {letter}: {string}".format(word = word, letter = player_guess.upper(), string = update_guess_as_string(word_as_list, guesses_as_list, guesses_as_string)))
                            print(hangman_you_win)
                            break
                        else:
                            print(page_break) 
                            print("Good job! My word does contain the letter {letter}: {string}".format(letter = player_guess.upper(), string = update_guess_as_string(word_as_list, guesses_as_list, guesses_as_string)))
                            insert_visual_aid(misses_counter)
                            past_guesses_string = ""
                            for i in past_guesses:
                                past_guesses_string += i + " "
                            if guess_counter > 1:
                                print("You have made {number} guess so far: {letters}".format(number = guess_counter, letters = past_guesses_string))
                                print("Wrong guesses: {x}".format(x = misses_counter))
                                print("Correct guesses: {x}".format(x = (guess_counter-misses_counter)))
                            else:
                                print("You have made {number} guess so far: {letters}".format(number = guess_counter, letters = past_guesses_string))
                                print("Wrong guesses: {x}".format(x = misses_counter))
                                print("Correct guesses: {x}".format(x = (guess_counter-misses_counter)))
                elif player_guess.upper() in past_guesses:
                    print(page_break)
                    print("Oops, it seems like you already guessed {letter} before, please try again: ".format(letter = player_guess.upper()))
                    continue
            else:
                print(page_break)
                print("Oops, it seems like you did not enter a valid letter as your guess, please try again: ")
                continue

print(game_header)
start_new_game()
play_game(word_as_list, guesses_as_list, guesses_as_string, misses_counter, possible_letters, past_guesses, guess_counter)