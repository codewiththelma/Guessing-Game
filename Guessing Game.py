import random as r
def main():
    rNum = r.randint(1,100)
    print('Welcome to the Guessing Game')
    print('Guess a number between 1 and 100 both inclusive')
    attempts = 10
    counter = 1
    guesses =[0]
    while counter <=10:
        print (f'You have {attempts} Guesses')
        guess = (int)(input('Your guess: '))
        guesses.append(guess)
        
        if guess < 1  or guess > 100:
            print('OUT OF BOUNDS please try again')
        if guess == rNum :
            print(f'Weldone, that was correct and it took you {counter} guesses')
            break

        if guesses[-2]: 
            if (abs(rNum - guess) < abs(rNum - guesses[-2])):
                print('WARMER')
                counter+=1
                attempts -=1
            else:
                print('COLDER')
                counter+=1
                attempts -=1
            
        
        else:
            if (abs(rNum - guess) <= 10):
                print('WARM')
                counter+=1
                attempts -=1
            else:
                print('COLD')
                counter+=1
                attempts -=1

        if attempts == 0:
            print('Nice try, Better luck next time')
            print(f'The number was {rNum}')

main()


