import random
rock = '''
 _______
----'____)
    (_____)
    (_____)
    (_____)
----.(___)
'''
paper = '''  
 _______
---'    ____)
           ______)
          _______)
         _______)
---.__________)                          
         '''

scissor = '''      
 _______
---'   ____)____
          ______)
       __________)
      (_____)
---.__(___)                         
          '''
game_images = [rock, paper, scissor]
computer_choice = random.randint(0,2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print("Your choice: ")
print(game_images[user_choice])
print(f"Computer chose : {computer_choice}")
print(game_images[computer_choice])
if user_choice == 0 and computer_choice == 2:
    print("You have won.Hurray!")
elif computer_choice > user_choice:
    print("You lost!")
elif user_choice==2 and computer_choice==0:
    print("You lost!")
elif user_choice > computer_choice:
    print("You have won. Hurray!")
elif user_choice==computer_choice:
    print("Game tied.")
else:
    print("You have entered the wrong choice.")











