def askToPlay():
    answer = input('Do you want to play a game? Yes or No : ')
    if answer.capitalize() == 'Yes':
        marker = input('Player 1 picks the marker: X or O : ')
        checkMarker(marker)
        play(marker)
    else:
        pass

def checkMarker(marker):
    if not (marker == 'X' or marker == 'O'):
        askToPlay()

def defineSecondMarker(marker):
    if marker == 'X':
        return 'O'
    else:
        return 'X'

def play(marker):
    gameOver = False
    turn = True
    ended = False
    array = ['1','2','3','4','5','6','7','8','9']
    print('Player 1 begins first.')
    while gameOver != True:
        displayArray(array)
        ended = isEnded(array)
        if ended:
            print('Nobody won!')
            break
        else:
            askForInput(array,turn,marker)
        turn = not turn
        gameOver = checkIfWon(array)
        if gameOver:
            if turn:
                print('Player 2 won!')
            else: 
                print('Player 1 won!')
            displayArray(array)
    askToPlay() 
def checkIfWon(array):
    for i in range(0,len(array)-2, 3):
        if (array[i] == array[i+1] == array[i+2]):
            return True
    for i in range(0,3):
        if (array[i] == array[i+3] == array[i+6]):
            return True

    if ((array[0] == array[4] == array[8] or array[2] == array[4] == array[6] )):
        return True
  
    return False

def isEnded(array):
    ended = True
    for i in range(0,len(array)):
        if array[i] == 'X' or array[i] == 'O':
            ended = True
        else:
            return False
    return ended

def displayArray(array):
        print('-------------------------')
        print(f'{array[6]}\t|{array[7]}\t|{array[8]}\t|\n \t| \t| \t|\n \t| \t| \t|')
        print('-------------------------')
        print(f'{array[3]}\t|{array[4]}\t|{array[5]}\t|\n \t| \t| \t|\n \t| \t| \t|')
        print('-------------------------')
        print(f'{array[0]}\t|{array[1]}\t|{array[2]}\t|\n \t| \t| \t|\n \t| \t| \t|')
        print('-------------------------')

def checkIfEmpty(string):
    return string != 'X' and string != 'O'

def askForInput(array,turn,marker):
    secondMarker = defineSecondMarker(marker)
    if turn:
        answer1 = input('Player1: Pick a number from 1-9. ')
        if (checkIfEmpty(array[int(answer1) - 1])):
            array[int(answer1) - 1] = marker
        else:
            askForInput(array,turn,marker)
    else: 
        answer2 = input('Player2: Pick a number form 1-9. ')
        if (checkIfEmpty(array[int(answer2) - 1])):
            array[int(answer2) - 1] = secondMarker
        else:
            askForInput(array,turn,marker)

askToPlay()