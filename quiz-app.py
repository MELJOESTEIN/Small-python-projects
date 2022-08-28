def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 1:
        if guess.lower() == answer.lower():
            print('Correct answer, Great!')
            score = score + 3 - attempt 
            still_guessing = False
        else:
            if attempt < 1:
                guess = input('Sorry wrong answer. Try again. ')
            attempt = attempt + 1
    if attempt == 2:
        print('The correct answer is ' + answer)
       
score = 0

name = input('Please, what is name?  ')
print("Welcome", name, " to our Quiz App !" )

#print("Let's Go !...")
#print("=========================================================================")

#first question
guess = input('Python is programming language. True or False? ')
check_guess(guess, 'True')

#second question
guess = input('GitHub is a command line. True or False?')
check_guess(guess, 'False')

#third question
guess = input('"cd"is a Linux command. True or False?')
check_guess(guess, 'True')

#forth question
guess = input('Linux is a game True or False?')
check_guess(guess, 'False')


print('Your score is ' + str(score))

print("Thanks for using this program!")