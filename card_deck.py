class CardDeck:
    def __init__(self, colors, shapes, fills, counts):

        # Define sets that contain card characteristics THESE LISTS WILL GET PASSED IN
        # colors = ['R', 'G', 'P']  # Red, Green, Purple
        # shapes = ['Ov', 'Di', 'Sg']  # Oval, Diamond, Squiggle
        # fills = ['So', 'St', 'Nf']  # Solid, Stripes, Nofill
        # counts = ['1', '2', '3']

        self.__colors = colors
        self.__shapes = shapes
        self.__fills = fills
        self.__counts = counts

    def build_deck(self):

        # Define empty list to hold cards
        cardlist = []

        # initialize card variable
        card = 'xxxx'

        # initialize index for to be used in list
        #index = 0

        # Build set of cards
        for c in self.__colors:
            for s in self.__shapes:
                for f in self.__fills:
                    for i in self.__counts:
                        # create card
                        card = i + '_' + f + '_' + c + '_' + s

                        #add card to cardlist
                        cardlist.append(card)

                        # print(cardList)
        #print('There are ' + str(len(cardlist)) + ' cards in the deck to start')
        return cardlist

