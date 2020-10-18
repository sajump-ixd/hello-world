def welcome():
    print "                _                              "
    print "__      __ ___ | |  ___  ___   _ __ ___    ___ "
    print "\ \ /\ / // _ \| | / __|/ _ \ | '_ ` _ \  / _ \ "
    print " \ V  V /|  __/| || (__| (_) || | | | | ||  __/"
    print "  \_/\_/  \___||_| \___|\___/ |_| |_| |_| \___|"
    print "                                               "

def intro():
    print "Let's travel the world and learn some history!"
    raw_input ("press enter to start >")

import math

# how to levelUp to leave the game after 3 rounds
count = 0 
def levelUp():
    global count
    count += 1

# end sequence
def endGame():
    print " _    _                               _ "
    print "| |_ | |__    ___     ___  _ __    __| |"
    print "| __|| '_ \  / _ \   / _ \| '_ \  / _` |"
    print "| |_ | | | ||  __/  |  __/| | | || (_| |"
    print " \__||_| |_| \___|   \___||_| |_| \__,_|"
    print "                                        "
    print "Thank you for playing!"

#china entry puzzle
def chinaPuzzle():
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "So you want to visit China?"
    print "First, you need to guess the secret passcode!"
    num1 = raw_input ("First Number: ")
    num2 = raw_input ("Second Number: ")
    num3 = raw_input ("Third Number: ")   
    
    try:
        num1=int(num1) # turns raw_input's string into an int and throws ValueError if not
        num2=int(num2)
        num3=int(num3)
        passcode = (num2 * (num1 + num2 + num3))
        if (passcode % 2) == 0: 
            print "You guessed the secret passcode!"
            raw_input (">")
            china()
        else:
            print " "
            print "That's incorrect. Please try again."
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            chinaPuzzle() 
    except ValueError as ve: #this stops the code from breaking if they enter non-numbers
        print "Please only enter integers! Try again."
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        chinaPuzzle()

#china 
def china(): 
    if count > 2:
        endGame()
    else:
        print "__  __ _  _             "
        print "\ \/ /(_)( )__ _  _ __  "
        print " \  / | ||// _` || '_ \ "
        print " /  \ | | | (_| || | | |"
        print "/_/\_\|_|  \__,_||_| |_|"
        print "Welcome to China!" 
        print "We are going to visit Xi'an, capital of Shaanxi Province."
        print "It is home to the Terracotta Army of Emperor Qin Shi Huang,"
        print "the first Emperor of China. The sculptures were buried"
        print "with the emperor in 210-209 BCE. They were discovered"
        print "by local farmers in 1974."
        raw_input (">")                   
        levelUp()
        if count < 3:
            print "Where do you want to go next,"
            next = raw_input ("Italy or Peru?: ")
            if (next == "Italy") or (next == "italy"):
                italyPuzzle()
            elif (next == "Peru") or (next == "peru"):
                peruPuzzle()
            else:
                print "Try again!"
                wordSearch()
        else: 
            endGame()
        
#peru entry puzzle
def peruPuzzle():
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "So you want to visit Peru?"
    print "First, you need to finish the pattern!"
    print "0, 1, 1, 2, 3, 5, 8, 13, 21, 34"
    fibAnswer = raw_input ("What is the next number?: ")
    
    if fibAnswer == "55":
        print "That is correct!"
        raw_input (">")
        peru()
    else: 
        print "That is incorrect. Please try again."
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        peruPuzzle()

#peru
def peru():
    if count > 2:
        endGame()
    else:                     
        print " _ __    ___  _ __  _   _ "
        print "| '_ \  / _ \| '__|| | | |"
        print "| |_) ||  __/| |   | |_| |"
        print "| .__/  \___||_|    \__,_|"
        print "|_|                       "
        print "Welcome to Peru! We are going to visit Machu Picchu."
        print "Machu Picchu is an Inca citadel from the 15th century."
        print "It is in the Urubamba Province, above Scared Valley."
        print "In the Quechua language, machu means old and"
        print "pikchu means pyramid."
        raw_input (">")                   
        levelUp()
        if count < 3:
            print "Where do you want to go next,"
            next = raw_input ("China or Italy?: ")
            if (next == "China") or (next == "china"):
                chinaPuzzle()
            elif (next == "Italy") or (next == "italy"):
                italyPuzzle()
            else:
                print "Try again!"
                wordSearch()
        else: 
            endGame()
        
#rome italy entry puzzle
def italyPuzzle():
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "So you want to visit Italy?"
    pasta = raw_input ("First, you need to tell me your favorite pasta: ")
    sauce = raw_input ("And your favorite pasta sauce: ")
    topping = raw_input ("Plus your favorite pasta topping: ")
    print ("Yum! " + pasta + " with " + sauce + " topped with " + topping +"!")
    raw_input (">")
    italy()

#rome italy
def italy():
    if count > 2:
        endGame()
    else:                         
        print " _ __  ___   _ __ ___    ___ "
        print "| '__|/ _ \ | '_ ` _ \  / _ \ "
        print "| |  | (_) || | | | | ||  __/"
        print "|_|   \___/ |_| |_| |_| \___|"
        print "Welcome to Italy! We are going to visit Rome."
        print "The Colosseum, also known as the Flavian Amphitheatre,"
        print "was built in 70-80 AD. "
        print "At the time, largest amphitheatre ever built."
        print "It held an estimated 50,000 to 80,000 spectators."
        raw_input (">")                   
        levelUp()
        if count < 3:
            print "Where do you want to go next,"
            next = raw_input ("China or Peru?: ")
            if (next == "China") or (next == "china"):
                chinaPuzzle()
            elif (next == "Peru") or (next == "peru"):
                peruPuzzle()
            else:
                print "Try again!"
                wordSearch()
        else: 
            endGame()
        
#word search with China, Peru and Italy
def wordSearch():
    print '*~*~*~*~*~*~*~*~*~*~*~*~*'
    print 'Solve the word search to' 
    print 'find a country to visit!'
    print '                       '
    print 'G F C I K P S W X Z A Q'
    print 'Q L N H Y A I D M I S X'
    print 'D C P R I T A L Y H W O'
    print 'I F E V C N O H X W R F'
    print 'M F R N Y G A L U C F N'
    print 'P Q U T O N F D O Z C Y'
    print 'T N O J S W V S E O C H'
    print '                       '
    answer = raw_input ('Answer: ')

    if (answer == "china") or (answer == "China") or (answer == "CHINA"):
        chinaPuzzle()
    elif (answer == "peru") or (answer == "Peru") or (answer == "PERU"):
        peruPuzzle()
    elif (answer == "Italy") or (answer == "italy") or (answer == "ITALY"):
        italyPuzzle()
    else: 
        print "Try again!"
        wordSearch()

def main():
    welcome()
    intro()
    wordSearch()

main()
