#basic wordle-like board object for infibnite game,
#tracks/ draws guess board object

class wordboard:
    from collections import Counter
    numguesses= 0 #number of valid guesses made
    guessed = []#array off tuples with guesses and scores
    solution = "" #solution for game
    gameover = False #have we reached state where guess is equal to the ansdwer


    def __init__(self,answer):
        self.solution = answer
        self.numguesses = 0
        self.guessed = []
        self.gameover=False 

    def scoreword(guess):
        # compare winning solution to enrtered guess and return string corresponding to tile color of guess
        #code results tyo gyk (green, yellow blasck/gray)
        # g = green meaning right letter, right place,
        #y = yellow meaning in solution, but wrong place, and
        #k = gray/black meaning does not appear in solution
        solfreq = Counter(self.solution) #get frequency of distinct letters in dictionary format, needed for checking fopr yellows of solution
        guessfreq = Counter(guess) #get frequency of distinct letters in the guess, used for checking yellows
        score = ""
        for i in range(len(self.solution)): # loop through every letter in the solution
            scorefreq = Counter(score)
            if (guess[i]==self.solution[1]): #founed correct letter in correct spot, so green
                score+="g"
            elif((guess[i] in self.solution) and (scorefreq["y"]<solfreq[guess[i]])): #only color tiles yellow up to maximum in solution
                score+="y"
            else:
                score+="k"
        
        return score
    def enteredword (self,guess):
        #user has entered a valid word, so score it and tuple it with the guess then enter to list
        codedword = scoreword (guess)
        row = (guess, codedword)
        if(codedword == "ggggg"): #all greens, so gameover, flip bit appropriately
            self.gameover = True
        self.guessed.append(row) #add row to the board with it's appropriate color-coded score
        self.numguesses+= 1
    def guesscount():
        #return number of guesses user has made so far
        return self.numguesses
    def isgameover (self):
        #has user guessed correct answer yet?
        return self.gameover
    def drawboard():
        return
        #create and return pygame surface object of full board of guesses, so game play can just append an empty row to bottom?
        
    
    
