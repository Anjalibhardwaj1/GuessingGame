#December 30 2020
#Guessing Game
#This program will pick a random number from 1 to 100, and
#it will ask the user to guess the number.
from random import randint

#Welcome Message and Rules
print("\n---------------------- Guessing Game ------------------------------")
print("Welcome!")
print("In this game I will think of a number, and you will try to guess it!\n")

#Start Game
ready = input("Are you ready to play? (Y/N)")

#If 'y' then start game otherwise, prompt and exit.
if ready.lower() == 'y':
        print("\nGenerating a random number...")

        #Randomly chose a number from 1 to 100
        random_num = randint(1, 100)

        #Initialize user Guess List
        guess_list = [0]

        #While True this code will loop and prompt the user for guesses
        while True:

            #Prompt user for their guess and convert to integer
            user_guess  = int(input('Enter Your Guess! \n'))

            #If the user's guess is out of bounds, ask the user again.
            if user_guess < 1 or user_guess > 100:
                print('Please Enter a Number Between 1 and 100. \n')
                continue

            #If the user's guess is correct then prompt user, tell them their amount of tries and break out of loop
            if user_guess == random_num:
                print('Correct! It took you {} tries!'.format(len(guess_list)))
                print("Play again next time!")
                exit()
                break

            #Add user's guesses to guess_list
            guess_list.append(user_guess)

            #If there exists 3 values in the list compare the current value to the previous value
            if guess_list[-2]:
                #if the current value is closer to the random number prompt "WAMER!"
                if abs(random_num-user_guess) < abs(random_num-guess_list[-2]):
                    print('WARMER!\n')

                #Otherwise, print "COLDER!"
                else:
                    print('COLDER!\n')

            #otherwise check if user's guess is within 10 digits of the random number
            else:
                if abs(random_num - user_guess) <= 10:
                    print("WARM!\n")
                else:
                    print("COLD!\n")

else:
    print("...Come back next time")
    exit()
