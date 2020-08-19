#Guess number game!
n=18
no_of_guess=1
print("no of guesess is limited you have only 5 chance.")
while(no_of_guess<=5):
    guess=int(input("enter correct number:"))
    if guess > 18:
        print("you enterd much more please enter lesser number.\n")
    elif guess <18:
        print("you entered a smallest no please choose greater no.\n")
    else:
        print("Congratulations ! you guessed correct number\n")
        print(no_of_guess,"no of guess he took to finish.")
        break
    print(5-no_of_guess,"guesses are left")
    no_of_guess=no_of_guess+1
    if(no_of_guess>5):
        print("Sorry you lost to guess correct number.")
