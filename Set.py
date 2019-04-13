import random



def main():
    
    # initialize variable to kick process out of loop 
    loop = 0
    
    # call function that builds deck of cards
    cardDeck = buildCards()
    #print('There are '+ str(len(cardDeck)) + ' cards in the deck')

    # select the first 12 cards to start
    cardsInPlay = drawCards(cardDeck,12)
    print('Current Cards in Play: ')
    print(cardsInPlay)
    
    pause = input(print('There are '+ str(len(cardDeck)) + ' cards remaining in the deck'))
    

    while loop < 2:
        #***************THIS ISN'T RIGHT. COULD RESULT IN ENDLESS LOOP. NOT SURE HOW TO FIX****************
        while len(cardDeck)> 3:
      
            #build combos
            comboList = createCombos(cardsInPlay)

            #print(comboList)
            # if a set was found, foundSet will be a string such as 3_St_G_Di,3_So_G_Ov,3_Nf_G_Ss
            foundSet = checkForSets(comboList) 
            
            # If no sets were found among the current 12 cards
            #************This gets tricky. At the end you can be appending and selecting the same cards over and over.
            if foundSet == 'NoSetFound':
                print('No Set Found') 
                # append all 12 cards back to the deck
                print(cardsInPlay)
                for card in cardsInPlay:
                    cardDeck.append(card)
                    
                # select another 12 cards if the deck is still large enough
                if len(cardDeck)>= 12:
                    cardsInPlay = drawCards(cardDeck,12)
                    print('New Cards In Play:')
                    pause = input(print(cardsInPlay))
                else: 
                    loop = 2
                
            # if a set WAS found:
            else:
                
                # use split to turn the 3 card string into a list
                setList = foundSet.split(',')
                print('Cards in SET: ' + str(setList))
                # remove the three cards from Cards In Play
                for card in setList:
                    cardsInPlay.remove(card)
                #pause = input(print('length of cards in play: ' + str(len(cardsInPlay))))
                
                
                # select another three cards from the deck
                threeCards = drawCards(cardDeck,3)
                print('Three new cards: '+ str(threeCards))

                #append cards to Cards in Play
                cardsInPlay.append(threeCards[0])
                cardsInPlay.append(threeCards[1])
                cardsInPlay.append(threeCards[2])
                print('Cards In Play: ' + str(cardsInPlay))
        
            stop = input(print('There are '+ str(len(cardDeck)) + ' cards remaining in the deck'))

def drawCards(cards,x):   
    #define empty list that will contain 3 cards
    selectedCards = []
    
    # set up a loop that repeats 3 times to pick 3 cards
    for i in range(0,x):
        
        #generate a random number in the range of the indexes of the cards in the array
        index = random.randint(0,len(cards)-1)    

        #append the card with the randomly generated index to the list of selected cards
        selectedCards.append(cards[index])
   
        # remove the card from the deck - this will be removed from the list
        # back in main
        cards.remove(cards[index])
        
    return selectedCards
            
   
def checkForSets(currentCombos):
 
    #print('current combos' + str(currentCombos)) 
    #print()
    combosChecked = 0

    # create trait arrays for each combination of cards within the 12 that are in play
    for combo in currentCombos:
            
        # initialize empty arrays to hold the individual traits of the cards in the combo
        symbolCounts = []
        fills = []
        colors = []
        shapes = []
        traits = []
       
        #turn combo string into a list
        splitCombo = combo.split(',')
        print('Currently checking this combo: ' + str(splitCombo))
        
        #look at cards and put each trait into the appropriate trait list.
        for card in splitCombo:
            
            # split the trait string for each card into a list 
            trait = card.split('_')
            #print(trait)      

            # grab each trait and append to corresponding trait array
            symbolCount = trait[0]
            symbolCounts.append(symbolCount)
                              
            fill = trait[1]
            fills.append(fill)
           
            color = trait[2]
            colors.append(color)
           
            shape = trait[3]
            shapes.append(shape)

       
        # After all the traits for the cards in a combo are put into trait arrays,
        # check each trait array to see whether it would or wouldn't be good 
        # for making a set

        #check he number of symbols on the cards
        checkSymbolCounts = checkTrait('Counts: ',symbolCounts)
        print('Symbol Count is: ' + str(checkSymbolCounts))
        if checkSymbolCounts is True:
            # check the fills on the cards
            checkFills = checkTrait('Fills: ', fills)
            print('Fills is: ' + str(checkFills))

            if checkFills is True:
                # check the colors on the cards
                checkColors = checkTrait('Colors: ', colors)
                print('Colors is: ' + str(checkColors))

                if checkColors is True:
                    # check the shapes on the cards
                    checkShapes = checkTrait('Shapes: ' ,shapes)
                    print('Shapes is: ' + str(checkShapes))
                      
        combosChecked += 1
        print('Combos checked: ' + str(combosChecked))
          
        # check if you have a set and return combo if so
        if checkSymbolCounts is True and checkFills is True and checkColors is True and checkShapes is True:
            return combo
        
    ## if no sets were found
    return 'NoSetFound'

    stop = print(input('pause'))   
  
        
# Checks all the values for one trait.
def checkTrait(trait, myTrait):
        print(trait + str(myTrait))
        #initialize counters
        same = 0
        diff = 0
        index = 0
        print(myTrait)
       
        #compare all values of the given trait against each other
        for index in range(0,3):
            # if you are NOT looking at the last item on the list, compare it to the next item.
            if index !=2:
                # otherwise compare it to the next item in list
                if myTrait[index] == myTrait[index+1]:
                    same += 1         
                else:
                    diff +=1
            # if you are looking at that last item in the list, compare it to the first
            else:
                if myTrait[2]== myTrait[0]:
                    same +=1
                else:
                    diff +=1         

        # this is just for development
        print('same:' + str(same))
        print('diff:' + str(diff))

        # determine if this trait is good for a set
        if same == 3 or diff == 3:
            traitSet = True
        else:
            traitSet = False

        #return the boolean value
        return traitSet
                        

def createCombos(currentCards):
    # initialize and empty array that will contain a copy of currentCards.
    # this is necessary because otherwise whatever you do to currentCards will
    # affect the list back in main
    currentCards_copy = []
    
    #create all possible combinations of three cards
    index = 0
    
    # initialize empy list to hold three letter groups
    combos = []

    #Make copy of currentCards list
    for card in currentCards:
        currentCards_copy.append(card)
    
    x = 0
    #create combos
    #Think in can do with three for loops instead (for x, y, z)...later
    while len(currentCards_copy) > 3:
        for y in range(1,len(currentCards_copy)):          
            for z in range(y+1,len(currentCards_copy)):
                combo = currentCards_copy[x] + ',' + currentCards_copy[y] + ',' + currentCards_copy[z]              
                #append to list of "cards" in play
                combos.append(combo)
           
        # Remove the first element, which will shift everything to left and will have
        # a new element with index 0
        currentCards_copy.remove(currentCards_copy[0]) 

    # create the last combo with the last three cards
    combo = currentCards_copy[0] + ',' + currentCards_copy[1] + ',' + currentCards_copy[2]

    # append last combo to list
    combos.append(combo)
    #print('there are ' + str(len(combos)) + ' possible combinations')
    return(combos)
        
  
def buildCards():
    #Define sets that contain card characteristics
    colors = ['R','G','P'] #Red, Green, Purple
    shapes = ['Ov','Di','Sg'] #Oval, Diamond, Squiggle
    fills = ['So','St','Nf'] #Solid, Stripes, Nofill
    counts = ['1','2','3'] 

    #Define empty list to hold cards
    cardList = []
    # initialize card variable
    card = 'x_x_x_x'
    
    #initialize index for to be used in list
    index = 0

    #Build set of cards
    for c in colors:
        for s in shapes:
            for f in fills:
                for x in counts:
                    # build a card
                    card  = x + '_' + f + '_' + c +'_'+ s
                    cardList.append(card)
                    #print(cardList)
    print('There are ' + str(len(cardList)) + ' cards in the deck to start')
    return cardList


# call main()
main()
    
    
