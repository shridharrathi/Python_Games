import random, time

def displayMsg():
    print
    print 'You are in a land full of dragons. In front of you, '
    print 'you see two caves. In one cave, the dragon is friendly'
    print 'and he will share all the treasure with you. While in other'
    print 'cave dragon is greedy and hungry. He will eat you on sight'
    print

def chooseCaveNo():
    caveNo =''
    while caveNo != '1' and caveNo != '2':
        caveNo = raw_input('Enter the cave number: ')

    return caveNo
    
def checkCave(cave):
    print 'You are approaching cave: ' + cave
    time.sleep(2)

    friendlyCave = random.randint(1,2)
    if(str(friendlyCave) == cave):
        print ' you win'
    else:
        print 'you lose'

while True:
    displayMsg()
    cave = chooseCaveNo()
    checkCave(cave)
    choice = raw_input('do you want to play again Y/N : ')
    if(choice == 'N'):
        break
    

