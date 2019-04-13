import random
from card_deck import CardDeck


def main():
    
    # initialize variable to kick process out of loop 
    loop = 0

    #initialize variable to count the total number of sets that were found
    set_count = 0

      # Define lists that contain card characteristics THESE LISTS WILL GET PASSED IN
    colors = ['R', 'G', 'P']  # Red, Green, Purple
    shapes = ['Ov', 'Di', 'Sg']  # Oval, Diamond, Squiggle
    fills = ['So', 'St', 'Nf']  # Solid, Stripes, Nofill
    counts = ['1', '2', '3']

    # instantiate a card deck
    deck = CardDeck(colors,shapes,fills,counts).build_deck()
    print(deck)

    print('There are '+ str(len(deck))+ ' cards in the deck')

    # select the first 12 cards to start
    cardsInPlay = drawCards(deck,12)
    print('Current Cards in Play: ')
    print(cardsInPlay)
    
    print('There are '+ str(len(deck)) + ' cards remaining in the deck')

    while loop != 2 or len(deck)>=3 :
        # build combos
        comboList = createCombos(cardsInPlay)
        # if a set was found, foundSet will be a string such as 3_St_G_Di,3_So_G_Ov,3_Nf_G_Ss
        foundSet = checkForSets(comboList)

        # If no sets were found among the cards in play
        if foundSet == 'NoSetFound':
            if len(deck) != 0: # if there are still card in the deck
                print('No Set Found')
                # select another three cards from the deck
                threeCards = drawCards(deck,3)
                print('Three new cards: ' + str(threeCards))
                # append cards to Cards in Play so there are now 15 cards in play
                cardsInPlay.append(threeCards[0])
                cardsInPlay.append(threeCards[1])
                cardsInPlay.append(threeCards[2])
            else: # if there are no cards remaining in the deck set flag to exit loop
                loop = 2

        # if a set WAS found:
        else:
            # use split to turn the 3 card string into a list
            setList = foundSet.split(',')
            print('SET found: ' + str(setList))
            set_count = set_count + 1
            print('Set count: ' + str(set_count))
            # remove the three cards from Cards In Play
            for card in setList:
                cardsInPlay.remove(card)

            print()

            if len(cardsInPlay) == 9:
                if len(deck)>=3:
                    threeCards = drawCards(deck,3)
                    cardsInPlay.append(threeCards[0])
                    cardsInPlay.append(threeCards[1])
                    cardsInPlay.append(threeCards[2])
                else:
                    loop += 1

        if loop !=2:
            print('Cards In Play: ' + str(cardsInPlay))
            #stop = input(print('There are '+ str(len(deck)) + ' cards remaining in the deck'))
            print('There are ' + str(len(deck)) + ' cards remaining in the deck')
            #print(deck)

    print('No SETs found in remaining Cards in Play')
    print('Total SETs found: ' + str(set_count))
    #print('Total number of cards remaining in deck: ' + str(len(deck)))

def drawCards(deck,x):
    #define empty list that will contain x cards
    selectedCards = []

    # set up a loop that repeats x times to pick x cards and test to make sure it's working correctly
    for i in range(0,x):
        assert len(deck) >= 1
        index = random.randint(0, len(deck) - 1)
        assert (0 <= index) and (index <= len(deck) - 1)

        num_cards_before = len(deck)
        expected_card = deck[index]
        drawn_card = deck.pop(index)
        num_cards_after = len(deck)

        assert num_cards_before == num_cards_after + 1
        assert drawn_card == expected_card
        assert drawn_card not in deck

        num_selected_cards_before = len(selectedCards)
        selectedCards.append(drawn_card)
        num_selected_cards_after = len(selectedCards)

        assert num_selected_cards_before == num_selected_cards_after - 1
        assert drawn_card in selectedCards

        # ANNA'S CODE
        # #generate a random number in the range of the indexes of the cards in the array
        # index = random.randint(0,len(deck)-1)
        # print(deck[index])
        # # remove the card from the deck - this will be removed from the list in main
        # deck.remove(deck[index])
        # print(deck) #take a peek and confirm card was removed
        # #append the card with the randomly generated index to the list of selected cards
        # selectedCards.append(deck[index])

    # THIS IS GARRETT'S VERSION
    # for i in range(0, x):
    #     index = random.randint(0, len(deck) - 1)
    #     drawn_card = deck.pop(index)
    #     selectedCards.append(drawn_card)

    return selectedCards

def checkForSets(currentCombos):
 
    # create trait arrays for each combination of cards within the 12 that are in play
    for combo in currentCombos:
            
        # initialize empty arrays to hold the individual traits of the cards in the combo
        symbolCounts = []
        fills = []
        colors = []
        shapes = []
       
        #turn combo string into a list
        splitCombo = combo.split(',')
        #print('Currently checking this combo: ' + str(splitCombo))
        
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

       
        # After all the traits for the cards in a combo are put into trait arrays, check each trait array
        # to see whether it be valid for a set.

        #check he number of symbols on the cards
        checkSymbolCounts = checkTrait('Counts: ',symbolCounts)
        #print('Symbol Count is: ' + str(checkSymbolCounts)) this is good for debugging
        if checkSymbolCounts is True:
            # check the fills on the cards
            checkFills = checkTrait('Fills: ', fills)
            #print('Fills is: ' + str(checkFills))

            if checkFills is True:
                # check the colors on the cards
                checkColors = checkTrait('Colors: ', colors)
                #print('Colors is: ' + str(checkColors))

                if checkColors is True:
                    # check the shapes on the cards
                    checkShapes = checkTrait('Shapes: ' ,shapes)
                    #print('Shapes is: ' + str(checkShapes))
                      
        #THESE ARE GOOD FOR DEBUGGING
        #combosChecked += 1
        #print('Combos checked: ' + str(combosChecked))
          
        # check if you have a set and return combo if so
        if checkSymbolCounts is True and checkFills is True and checkColors is True and checkShapes is True:
            return combo
        
    ## if no sets were found
    return 'NoSetFound'

    stop = print(input('pause'))


def checkTrait(trait, myTrait):
#Checks all the value for a trait.

    # print(trait + str(myTrait)) THIS IS USEFUL FOR DEBUGGING
    #initialize counters
    same = 0
    diff = 0

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
    #print('same:' + str(same))
    #print('diff:' + str(diff))

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

    # initialize empy list to hold three letter groups
    combos = []

    #Make copy of currentCards list
    for card in currentCards:
        currentCards_copy.append(card)
    
    x = 0
    #create combos
    while len(currentCards_copy) > 3:
        for y in range(1,len(currentCards_copy)):
            for z in range(y+1,len(currentCards_copy)):
                combo = currentCards_copy[x] + ',' + currentCards_copy[y] + ',' + currentCards_copy[z]
                #append to list of "cards" in play
                combos.append(combo)
           
        # Remove the first element, which will shift everything to left resulting in a new element with index 0
        currentCards_copy.remove(currentCards_copy[0]) 

    # create the last combo with the last three cards
    combo = currentCards_copy[0] + ',' + currentCards_copy[1] + ',' + currentCards_copy[2]

    # append last combo to list
    combos.append(combo)
    #print('there are ' + str(len(combos)) + ' possible combinations')
    return(combos)
        

# call main()
main()
    
    
