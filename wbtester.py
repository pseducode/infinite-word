#scrap file to play with/test wordboard class
import wordboard


def main():
    print ("hello!")
    test = wordboard.wordboard("audio")
    test.enteredword("audio")
    print("game is currently over?: "+str(test.isgameover()))

if __name__=="__main__":
    main()
