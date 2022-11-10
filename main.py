import random

#The code for running the dice 
def game():
    rand = random.randint(1, 6)
    print("Your dice rool is " + str(rand))
    restart = input("do u want to get another dice rool?(y/n): ")
    if restart == 'y':
        game()
    else:
        print("Thanks for joining!")

def again():
    t = True
    count = 0
    while t :
        rand = random.randint(1, 6)
        print("Your dice rools are: ")
        print(rand)
        if count == 99:
            break
        else:
            count += 1
            continue
        
#Taking input from input for starting the game!
print("If you want 100 dice rools type '100': ")
start = input("Are you ready? (y/n/100): ")
if start == "y":
    print("")
    game()
elif start == '100':
    again()

else:
    print("Thanks for joining us")

    

