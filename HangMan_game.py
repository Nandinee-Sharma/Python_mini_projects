import random

stages = ['''
  +----+
  |    |
  0    |
 /|\   |
 / \   |
       |
 =======''',
 '''
  +----+
  |    |
  0    |
 /|\   |
 /     |
       |
 =======''',
''' 
  +----+
  |    |
  0    |
 /|\   |
       |
       |
 =======''',
 '''
  +----+
  |    |
  0    |
  |    |
       |
       |
  ======''',
 '''
  +----+
  |    |
  0    |
       |
       |
       |
  ======''',
 '''
  +----+
  |    |
       |
       |
       |
       |
  ======''']
word_list = ["Aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
lives = 5
while not game_over:
    print(f"---------------------{lives} lives left-------------------------")
    guess = input("Enter a letter: ").lower()
    display = ""
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)
    if guess not in chosen_word:
        lives -=1
        if lives==0:
            game_over = True
            print("------------------You lose------------------")
            print(f"------------It was '{chosen_word}'----------------")
            print("Hangman got hanged.")
    if "_" not in display:
        game_over = True
        print("-------------------You win-------------------")
    print(stages[lives])
