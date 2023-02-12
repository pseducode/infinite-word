#basic python implementation of wordle, using actual wordle, word-list,
#except with infinite guesses, insteasd of just 6, for poractice.
#need to use pygame for display purposess

# for input reference, use file = testtext.py, using code from tab = https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/
import random
import os, sys
import fnmatch
import pygame
def scoreword(winning,guess): #compare winning word to guess and return string corresponding to matches
    #with gyk (green yellow black/gray)
    #green meaning right letter, right place, yellow meaning right letter,wong place, and k =black/gray, not appear in sdolution
    #first make a pass looking for green
    #next pass = check for yellows
    coded = ""#color representation of tile color, as compared to guess & winning word
    for i in range(len(winning)):
        if(guess[i]==winning[i]): # found correct letter, in correct spot, green
            coded+="g"
        elif(guess[i] in winning): # correct letter, wrong spot. so yellow
            coded+="y"
        else: #guess letter not in s olution, so grey/black
            coded+="k"
    return coded
def pickword():
    wordchoices = open("words","r")
    wordlist = wordchoices.readlines()
    numoptions =len(wordlist)
    return (wordlist[random.randint(0,numoptions-1)])
    
def main2(): #read main game loop for some reason
#some constants
    twidth=25 # width of a single tile
    theight=35 #height of a single tile
    theightoffset= 40 #padding to add between rows of y coord
    twidthoffset = 40 #padding to add between columns of x coords
    green = (0,255,0)
    gray = (200,200,200)
    yellow= (255,255,102)
    #first select a random word from official wordle wordlist
    winning = pickword()
    print("wiining solution will be: "+winning)
    #init pygame and start game lkoop
    pygame.init()
    size = (400,300)
    screen = pygame.display.set_mode(size)
    wordtry=""
    wordsguessed=[]
    while True:
        #deal with input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type ==pygame.KEYDOWN: #user typed a key, deal with it.
                if event.key == pygame.K_BACKSPACE:
                    wordtry = wordtry[:-1]
                elif ((event.Key==pygame.K_KP_ENTER) or (event.key=pygame.K_RETURN))
                    #pressed enter/return, validate word, add to wordlist
                
                
                
        #draw rows
        if wordtry =="": #haven't tried entering anything yet, draw empty row
            for i in range(5):
                xlocation = 20+(twidthoffset*i)
                pygame.draw.rect(screen,gray,pygame.Rect(xlocation,30,twidth,theight))
                pygame.display.flip()
            
            
        
        
    
    #use code from scrap.py to made wordle-clone tile-graphics (in user dir)
def main():
    
    
    print ("main game loop")
    #first load wordlist & pick one at random
    #load in graphics
    #prompt usaer to type in guess
    #compare guess to selected
    #display results of guess onscreen


if __name__=="__main__":
    main2()



