import random
import hangman_words
import hangman_art

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     
''')

## GENERATE A RANDOM WORD ##
# Pick a word/string at random from the list above
rword_str = random.choice(hangman_words.word_list)

## GENERATE AS MANY BLANK-DASHES AS LETTERS IN THE WORD
# Convert the word/string to a list
space_join = ' '.join(rword_str)
rword_list = space_join.split()
#print(rword_list) #UNCOMMENT THIS FOR TESTING PURPOSE
# Replace the list indexes with dashes, then convert back to a string format
for i in range(len(rword_list)):
    rword_list[i] = ' __ '
    #print(rword_list)
#print(rword_list)  #rword_list has been updated with dashes as values
str_rword_list = ''.join(rword_list) #back to string
print(f"Guess the letters: {str_rword_list}\n") 

##Numbers of 6 tries when word ain't in the letters
life_lines = 0

end_of_game = False
while end_of_game == False:
    ##ASK THE USER TO GUESS A LETTER
    guessed_letter = input("Guess a letter: ")
    guessed_letter.lower()

    if guessed_letter in str_rword_list:
        print(f"You've already guessed {guessed_letter}")
    #CHECK IF THE GUESSED LETTER IS IN THE WORD
    for i in range(len(rword_str)):
        letter = rword_str[i]

        if letter == guessed_letter:
            rword_list[i] = letter
            #print(rword_list)
        #print(rword_list)
    # Change rword_list back to string
    str_rword_list = ''.join(rword_list) #back to string
    print(str_rword_list)

    #CHECK IF ALL THE BLANK-DASHES ARE FILLED OR NOT
    if '__' not in str_rword_list:
        end_of_game = True #Stops the while loop
        print("\nYOU WIN!!!")

    #WHEN GUESSED LETTER IS NOT PRESENT
    if guessed_letter not in rword_str:
        print(f"\nYou guessed '{guessed_letter}', which is not in the word. Therefore, you lose a life.")
        life_lines += 1
        if life_lines == 6:
            end_of_game = True #Stops the while loop
            print(f"\nYOU'VE BEEN HUNG! YOU LOSE!\nCorrect Answer: {rword_str}")
        #else statement is not necessary, it will loop automatically

    print(hangman_art.stages[life_lines])