import random
from words import words # from a python file  called words import list variable called words which contain list of several words 


def get_valid_word(words):
  word=random.choice(words)        #randomly choice a word from  words list
  while '-' in word or ' 'in word: # to remove dash and space of some words present in [words list] 
    word=random.choice(words)
  return word.lower()                      #return a random word from a list of word


def display(lives):
  if lives==0:

    print("               _________________   ")
    print("               |             |     ")
    print("               |             O     ")
    print("               |            /|\    ")
    print("               |             |     ")
    print("               |            / \    ")

  elif lives==1:
        
        
    print("               _________________   ")
    print("               |             |     ")
    print("               |             O     ")
    print("               |            /|\    ")
    print("               |             |     ")
    print("               |                   ")
  elif lives==2:
    print("               _________________   ")
    print("               |             |     ")
    print("               |             O     ")
    print("               |            /|\    ")
    print("               |                   ")
    print("               |                   ")
  elif lives==3:
    print("               _________________   ")
    print("               |             |     ")
    print("               |             O     ")
    print("               |                   ")
    print("               |                   ")
    print("               |                   ")
  elif lives==4:
    print("               _________________   ")
    print("               |             |     ")
    print("               |                   ")
    print("               |                   ")
    print("               |                   ")
    print("               |                   ")
  elif lives==5:
    print("               _________________   ")
    print("               |                   ")
    print("               |                   ")
    print("               |                   ")
    print("               |                   ")
    print("               |                   ")
  elif lives==6:
    print("                                   ")
    print("               |                   ")
    print("               |                   ")
    print("               |                   ")
    print("               |                   ")
    print("               |                   ")


def start_game():
  name=input("What's Your Name\n")
  print("\t  Hello ",name,"!!\n\t  Are you ready to play H A N G M A N")
  display(0)
  print("\n\tStart Guessing Some Random Words Now")
  hangman()



  

    

def hangman():
  word=get_valid_word(words) #get a random word from get_valid_word function assigned to word variable
  letter_word=list(word) #track the guessing  letter in the word by creating letter_word list
  used_letter=list()    #list created to append the user guessed letter
  
  display_list=[]   # list created to display the guessing letter

  for i in word:
    display_list.append("_") # initially creating a total letter blanks of a randomly selected word
  

  lives=6    
              # 6 lives for the game

  while len(letter_word)>0 and lives>0:
     #To get a clue at lives=1
    
  
    
   
    print("\n")
    print("Your Word is : "," ".join(display_list))                   # show the total letters of a word by joining the list of total letter blanks
    print("\n")
    print("You have ",lives," lives left and you have used these letters: ",','.join(used_letter))  # show the guessed letter by joining the used_letter list

    user_input=input("Guess a Letter\n ") 
    # user can enter uppercase or lowercase letter but we should 
    # convert the letter to lowercase ,because our words list is  having lowercase 

    if user_input.lower() not in used_letter: #1 st condition is for fresh entered letter
      used_letter.append(user_input.lower()) #add not presented letters i.e user input to used_letter
      cond=False
      for letter in letter_word:
        if user_input in letter_word: # if it is present in original letter_word list        
          letter_word.remove(user_input.lower())  # remove the that letter from thelist
          cond=True                                      
      if cond==True:
        print("You have guessed a right letter",user_input) #display message
        display(lives)
      else: 
        print("You have guessed a wrong letter")
        lives=lives-1
        display(lives)
      
      

      
    elif user_input in used_letter:                                       # if already entered letter is entered again
      print("You have already used this letter. Guess the another Letter")   
      display(lives) 

    else:                                 # else for any different characters
      print("That's an invalid letter ")
      display(lives)

# placing rightly guessed letter at it's index using same display_list
    display_list=[] 
    for letter in word:   
      if letter in used_letter:  #if letter of a word is found at used_letter 
        display_list.append(letter)
      else:
        display_list.append('_')  #else the letter index would be blank
  #This whole process is continued till lives=0 and letter_word list length >0 i.e removing is done for this list at the right guessing     


  # After failed Guessing i.e with zero lives     
  if lives==0:
    print("You Died,Sorry.The Word was-->",word)
    continue_play=int(input("Please Enter 1 to continue "))
    if continue_play==1: # To continue the game 
      hangman()
    else:
      quit()
      
  # Else You Have Guessed all the Correct letters  in the word 
  else:
    print("YAY! You WON.The Word was--> ",word,"!!")
    continue_play=int(input("Please Enter 1 to continue "))
    if continue_play==1: #To continue the game
      hangman()
    else:
      quit()
start_game()      

            