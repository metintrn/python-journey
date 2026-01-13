import random
rock="🪨"
paper="🗏"
scissors="✂️"
game_img=[rock,paper,scissors]

user_choice=int(input("what do you choice? type 0 for rock 1 for paper 2 for scissors\n"))
if user_choice>= 0 and user_choice<=2:
    print(game_img[user_choice])
computer_choice=random.randint(0,2)

print("computer chose: ")
print(game_img[computer_choice])
if computer_choice == 0 and user_choice==2:
            print("User wins!!")
elif user_choice >=3 or user_choice<0:
            print("You chose invalid number!!")
elif computer_choice==2 and user_choice==0:
            print("Commputer wins!!")
elif computer_choice>user_choice:
            print("Computer wins!")
elif user_choice >computer_choice:
            print("User wins!")
elif computer_choice==user_choice:
            print("It's a draw")
 #This is a simple Rock, Paper, Scissors game written in Python.
#The user selects an option, the computer makes a random choice, and the program compares both to determine the winner.

