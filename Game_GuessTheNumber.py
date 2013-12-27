import random

def  greet():
    print 'Hello'
    playerName = raw_input('What is your Name: ')
    print 'Welcome ' +playerName + ' !!! Let us now play Guess the Number'
    return playerName


guess = 6

playerName = greet()

while True:
    number = random.randint(1,20)
    count =0
    while count < guess:
        count +=1
        enteredNo = input('Guess the number: ')
        if enteredNo < number:
            print 'Entered number is less than the correct number'
        elif enteredNo > number:
            print 'Entered number is greater than the correct number'
        elif enteredNo == number:
            print 'You have guessed correctly in ' + str(count) +' count'
            break
    if enteredNo != number:
        print 'you lose'

    choice = raw_input(playerName + ', do you want to play again Y/N : ')
    if(choice == 'N'):
        break


