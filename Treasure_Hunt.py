print('''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           |'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'|U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-|U|.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')
print("Welcome to the treasure island!")
print("Your mission is to find the treasure.")
choice1 = input('You\'r are at a crossroad,where do you want to go? Type "left" or "right:" ' ).lower()
if choice1=="left":
    choice2 = input('You are now at a lake, what do want to do? "Wait" or "Swim" :').lower()
    if choice2 == "wait":
        choice3 = input('Now choose from which door you want to go?: "Red", "Yellow" or "Blue": ').lower()
        if choice3=="yellow":
            print("Hurray! You've found the treasure.")
        else:
            print("Danger! Game over.")
    else:
        print("Crocodiles! Game over.")
else:
    print("You fell into a lake, Game over!")

