import random

anothergame = "Y"
while anothergame == "Y":

    deck =       {1: {"card": "A",
                      "suit": "♥",
                      "value": 1},
                  2: {"card": "2",
                      "suit": "♥",
                      "value": 2},
                  3: {"card": "3",
                      "suit": "♥",
                      "value": 3},
                  4: {"card": "5",
                      "suit": "♥",
                      "value": 4},
                  5:  {"card": "5",
                       "suit": "♥",
                       "value": 5},
                  6: {"card": "6",
                      "suit": "♥",
                      "value": 6},
                  7: {"card": "7",
                      "suit": "♥",
                      "value": 7},
                  8: {"card": "8",
                      "suit": "♥",
                      "value": 8},
                  9: {"card": "9",
                      "suit": "♥",
                      "value": 9},
                  10: {"card": "10",
                       "suit": "♥",
                       "value": 10},
                  11: {"card": "J",
                       "suit": "♥",
                       "value": 10},
                  12: {"card": "Q",
                       "suit": "♥",
                       "value": 10},
                  13: {"card": "K",
                       "suit": "♥",
                       "value": 10},
                  14: {"card": "A",
                       "suit": "♦",
                       "value": 1},
                  15: {"card": "2",
                       "suit": "♦",
                       "value": 2},
                  16: {"card": "3",
                       "suit": "♦",
                       "value": 3},
                  17: {"card": "5",
                       "suit": "♦",
                       "value": 4},
                  18:  {"card": "5",
                        "suit": "♦",
                        "value": 5},
                  19: {"card": "6",
                       "suit": "♦",
                       "value": 6},
                  20: {"card": "7",
                       "suit": "♦",
                       "value": 7},
                  21: {"card": "8",
                       "suit": "♦",
                       "value": 8},
                  22: {"card": "9",
                       "suit": "♦",
                       "value": 9},
                  23: {"card": "10",
                       "suit": "♦",
                       "value": 10},
                  24: {"card": "J",
                       "suit": "♦",
                       "value": 10},
                  25: {"card": "Q",
                       "suit": "♦",
                       "value": 10},
                  26: {"card": "K",
                       "suit": "♦",
                       "value": 10},
                  27: {"card": "A",
                       "suit": "♠",
                       "value": 1},
                  28: {"card": "2",
                       "suit": "♠",
                       "value": 2},
                  29: {"card": "3",
                       "suit": "♠",
                       "value": 3},
                  30: {"card": "5",
                       "suit": "♠",
                       "value": 4},
                  31:  {"card": "5",
                        "suit": "♠",
                        "value": 5},
                  32: {"card": "6",
                       "suit": "♠",
                       "value": 6},
                  33: {"card": "7",
                       "suit": "♠",
                       "value": 7},
                  34: {"card": "8",
                       "suit": "♠",
                       "value": 8},
                  35: {"card": "9",
                       "suit": "♠",
                       "value": 9},
                  36: {"card": "10",
                       "suit": "♠",
                       "value": 10},
                  37: {"card": "J",
                       "suit": "♠",
                       "value": 10},
                  38: {"card": "Q",
                       "suit": "♠",
                       "value": 10},
                  39: {"card": "K",
                       "suit": "♠",
                       "value": 10},
                  40: {"card": "A",
                       "suit": "♣",
                       "value": 1},
                  41: {"card": "2",
                       "suit": "♣",
                       "value": 2},
                  42: {"card": "3",
                       "suit": "♣",
                       "value": 3},
                  43: {"card": "5",
                       "suit": "♣",
                       "value": 4},
                  44:  {"card": "5",
                        "suit": "♣",
                        "value": 5},
                  45: {"card": "6",
                       "suit": "♣",
                       "value": 6},
                  46: {"card": "7",
                       "suit": "♣",
                       "value": 7},
                  47: {"card": "8",
                       "suit": "♣",
                       "value": 8},
                  48: {"card": "9",
                       "suit": "♣",
                       "value": 9},
                  49: {"card": "10",
                       "suit": "♣",
                       "value": 10},
                  50: {"card": "J",
                       "suit": "♣",
                       "value": 10},
                  51: {"card": "Q",
                       "suit": "♣",
                       "value": 10},
                  52: {"card": "K",
                       "suit": "♣",
                       "value": 10}}

    for i in deck.values():
        text = str(i).replace('{','').replace('}','').replace("'card': '","").replace("', 'suit': '","").replace(", 'value':","")
        text = text.split("'")
        print(text[0], end=' ')
        
    print()
    card1key = ''
    card2key = ''
    card3key = ''
    card4key = ''
    card5key = ''
    card6key = ''
    card7key = ''
    card8key = ''
    card9key = ''
    card10key = ''
    card11key = ''
    card12key = ''
    totalround2 = ''
    totalround3 = ''
    totalround4 = ''
    totalround5 = ''
    totalround6 = ''
    totalround7 = ''

    player1 = input("Player 1 name: ")
    player2 = input("player 2 name: ")
    print("-"*40)
    print("WELCOME TO THE BLACKJACK TABLE")
    print("-"*40)
    
    rules = input("Do you know how to play? (Y/N) ").upper()
    if rules == "N":
        print("Player with higher score and <22 wins")
    else:
        print("Let's begin blackjack!")
        print("-"*40)
        
    firstseat = player1
    secondseat = player2

    
    #PLAYER1 TURN
    while 1:
        try:
            card1key = random.choice(deck)
            break
        except:
            pass
            
    for k,v in deck.items():
        if card1key == k:
            del deck[k]
    while 1:
        try:
            card2key = random.choice(deck)
            break
        except:
            pass
    for k,v in deck.items():
        if card2key == k:
            del deck[k]
    totalround2 = (card1key["value"]) + (card2key["value"])
    # DOUBLE ACE CHECK
    if totalround2 == 22:
        totalround2 = 12

    print("{}{} and a {}{}. \n"
          "You're at: {}".format(card1key["card"], card1key["suit"], card2key["card"], card2key["suit"], totalround2))
          
    player1_score = int(totalround2)

    print("-"*40)
    hitorstay = input("Hit or Stay? (H/S)").upper()

    if hitorstay == "H":
        while 1:
            try:
                card3key = random.choice(deck)
                break
            except:
                pass
        for k,v in deck.items():
            if card3key == k:
                del deck[k]
        totalround3 = (card1key["value"]) + (card2key["value"]) + (card3key["value"])


        print("{}{}, {}{}, and {}{}.\n"
              "Total: {}".format(card1key["card"], card1key["suit"], card2key["card"], card2key["suit"], card3key["card"], card3key["suit"], totalround3))

        if totalround3 < 21:
            hitorstay = input("Hit or Stay? (H/S)").upper()
            if hitorstay == "H":
                while 1:
                    try:
                        card4key = random.choice(deck)
                        break
                    except:
                        pass
                    
                    
                for k,v in deck.items():
                    if card4key == k:
                        del deck[k]
                totalround4 = (card1key["value"]) + (card2key["value"]) + (card3key["value"]) + (card4key["value"])
                print("{}{}, {}{}, and {}{}, and {}{}.\n"
                    "Total: {}".format(card1key["card"], card1key["suit"], card2key["card"], card2key["suit"], card3key["card"], card3key["suit"], card4key["card"], card4key["suit"], totalround4))


            else:
                print("-"*40)
        else:

            print("-"*40)
    else:
        
        print("-"*40)



    #PLAYER2 TURN
    print("################### - "+player2+" Turn -###################")
    while 1:
        try:
            card5key = random.choice(deck)
            break
        except:
            pass
    for k,v in deck.items():
        if card5key == k:
            del deck[k]
    while 1:
        try:
            card6key = random.choice(deck)
            break
        except:
            pass
    for k,v in deck.items():
        if card6key == k:
            del deck[k]


    totalround5 = (card5key["value"]) + (card6key["value"])
    #Double Ace Check
    if totalround5 == 22:
        totalround5 = 12

    print("{}{} and a {}{}. \n"
          "You're at: {}".format(card5key["card"], card5key["suit"], card6key["card"], card6key["suit"], totalround5))

    player2_score = int(totalround5)

    print("-"*40)
    hitorstay = input("Hit or Stay? (H/S)").upper()

    if hitorstay == "H":
        while 1:
            try:
                card7key = random.choice(deck)
                break
            except:
                pass
        for k,v in deck.items():
            if card7key == k:
                del deck[k]
        totalround6 = (card5key["value"]) + (card6key["value"]) + (card7key["value"])
        print("{}{}, {}{}, and {}{}.\n"
              "Total: {}".format(card5key["card"], card5key["suit"], card6key["card"], card6key["suit"], card7key["card"], card7key["suit"], totalround6))


        if totalround6 < 21:
            hitorstay = input("Hit or Stay? (H/S)").upper()

            if hitorstay == "H":
                while 1:
                
                    try:
                        card8key = random.choice(deck)
                        break
                    except:
                        pass
                
                for k,v in deck.items():
                    if card8key == k:
                        del deck[k]
                totalround7 = (card5key["value"]) + (card6key["value"]) + (card7key["value"]) + (card8key["value"])
                print("{}{}, {}{}, {}{}, and {}{}.\n"
                    "Total: {}".format(card5key["card"], card5key["suit"], card6key["card"], card6key["suit"], card7key["card"], card7key["suit"], card8key["card"], card8key["suit"], totalround7))










    #RESULTS OF ROUND
    print("-"*40)
    print("----------RESULTS----------")


    # results
    if totalround3 == "":
        totalround3 = 0
    if totalround4 == "":
        totalround4 = 0
        
    if totalround6 == "":
        totalround6 = 0
    if totalround7 == "":
        totalround7 = 0

    player1_final_score = totalround2
    player1_cards = "{}{}, {}{}".format(card1key["card"], card1key["suit"], card2key["card"], card2key["suit"])
    
    if totalround3 > 0:
        player1_final_score = totalround3
        player1_cards += ", {}{}".format(card3key["card"], card3key["suit"])
    if totalround4 > 0:
        player1_final_score = totalround4
        player1_cards += ", {}{}".format(card4key["card"], card4key["suit"])
    
    player2_final_score = totalround5
    player2_cards = "{}{}, {}{}".format(card5key["card"], card5key["suit"], card6key["card"], card6key["suit"])
    
    if totalround6 > 0:
        player2_final_score = totalround6
        player2_cards += ", {}{}".format(card7key["card"], card7key["suit"])
    if totalround7 > 0:
        player2_final_score = totalround7
        player2_cards += ", {}{}".format(card8key["card"], card8key["suit"])
        
    if (player1_final_score > 21 and player2_final_score > 21): #BUST
            print("Both are Busted!")
            
    elif (player1_final_score == 21 and player2_final_score == 21):
            print("We have a draw!")
            
    elif (player1_final_score == 21 and (player2_final_score < 21 or player2_final_score > 21)):
            print("We have a winner: "+player1)
            
    elif ((player1_final_score > 21 or player1_final_score < 21) and player2_final_score == 21):
            print("We have a winner: "+player2)
    
    elif (player1_final_score > 21 and player2_final_score < 21):
            print("We have a winner: "+player2)
            
    elif (player1_final_score < 21 and player2_final_score > 21):
            print("We have a winner: "+player1)
            
    elif (player1_final_score < 21 and player2_final_score < 21):
    
            if (player1_final_score > player2_final_score):
                    print("We have a winner: "+player1)
                    
            elif (player1_final_score == player2_final_score): 
                    print("We have a draw!")
            else:
                    print("We have a winner: "+player2)


    print(str(player1)+" score: "+str(player1_final_score))
    print(player1+"'s cards: "+player1_cards)
    #print(totalround2)
    #print(totalround3)
    #print(totalround4)
    print(str(player2)+" score: "+str(player2_final_score))
    print(player2+"'s cards: "+player2_cards)
    #print(totalround5)
    #print(totalround6)
    #print(totalround7)
    print("-"*40)
    anothergame = input("Want to try another round?(Y/N) ".format(firstseat, secondseat)).upper()
    if anothergame == "N":
        print("Thanks for playing! Come back for free martinis anytime!")
