#basic wordle-like board object for infibnite game,
#tracks/ draws guess board object

class wordboard:
    numguesses= 0 #number of valid guesses made
    guessed = []#array off tuples with guesses and scores
    solution = "" #solution for game
    gameover = false #have we reached state where guess is equal to the ansdwer


    def __init__(self,answer):
        self.solution = answer
        self.numguesses = 0
        self.guessed = []
        self.gameover=false

    def scoreword(guess):
        # encode scoring of word into green/yellow/gray
        score = ""
        return score
    def enteredword (guess):
        #user has entered a valid word, so score it and tuple it with the guess then enter to list
        codedword = scoreword(guess)
        row = (guess, codedword)
        self.guessed.append(row) #add row to the board with it's appropriate color-coded score
        self.numguesses+= 1
    def guesscount():
        #return number of guesses user has made so far
        return self.numguesses
    def gameover ():
        #has user guessed correct answer yet?
        return self.gameover
    def drawboard():
        #create and return pygame surface object of full board of guesses, so game play can just append an empty row to bottom?
        
    
    
