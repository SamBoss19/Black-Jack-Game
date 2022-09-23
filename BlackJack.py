import random


cards = '''
                                _____
         _____                _____ |6    |
        |2    | _____        |5    || & & |
        |  &  ||3    | _____ | & & || & & | _____
        |     || & & ||4    ||  &  || & & ||7    |
        |  &  ||     || & & || & & ||____9|| & & | _____
        |____Z||  &  ||     ||____S|       |& & &||8    | _____
               |____E|| & & |              | & & ||& & &||9    |
                      |____h|              |____L|| & & ||& & &|
                                  _____           |& & &||& & &|
                          _____  |K  WW|          |____8||& & &|
                  _____  |Q  ww| | o {)|                 |____6|
           _____ |J  ww| | o {(| |o o%%| _____
          |10 & || o {)| |o o%%| | |%%%||A _  |
          |& & &||o o% | | |%%%| |_%%%>|| ( ) |
          |& & &|| | % | |_%%%O|        |(_'_)|
          |& & &||__%%[|                |  |  |
          |___0I|                       |____V|
                                     _____
         _____                _____ |6    |
        |2    | _____        |5    || v v |
        |  v  ||3    | _____ | v v || v v | _____
        |     || v v ||4    ||  v  || v v ||7    |
        |  v  ||     || v v || v v ||____9|| v v | _____
        |____Z||  v  ||     ||____S|       |v v v||8    | _____
               |____E|| v v |              | v v ||v v v||9    |
                      |____h|              |____L|| v v ||v v v|
                                  _____           |v v v||v v v|
                          _____  |K  WW|          |____8||v v v|
                  _____  |Q  ww| |   {)|                 |____6|
           _____ |J  ww| |   {(| |(v)%%| _____
          |10 v ||   {)| |(v)%%| | v%%%||A_ _ |
          |v v v||(v)% | | v%%%| |_%%%>||( v )|
          |v v v|| v % | |_%%%O|        | \ / |
          |v v v||__%%[|                |  .  |
          |___0I|                       |____V|
                             
'''
# number = random.randint(0,20)
# number1 = random.randint(0,20)
# playerCard = [number,number1]
# print(f"Your card is: {playerCard}")
print(cards)
decide = True
while decide == True:
    
    def winner():
        playcalc= sum(playerCard)
        compcalc = sum(computerCard)
        print(f"Your cards: {playerCard}")
        print(f"Computer cards: {computerCard}")
        if playcalc > 21:
            print(f"You lose!!. Your total card is {playcalc} which is above 21 ")
        elif playcalc > compcalc:
            print(f"You win!!!")
        elif playcalc == compcalc:
            print("Draw")
        else:
            print("You lose!!!")
    def randdom():
        number = random.randint(0,15)
        return number
    playerCard = []
    computerCard = []
    def initial():
        playerCard.append(randdom())
        playerCard.append(randdom())
        computerCard.append(randdom())
        computerCard.append(randdom())
        #return playerCard , computerCard
    def blackjack():
        print(f"Your cards: {playerCard}")
        print(f"Computer cards: {computerCard[0]}")
        request = input("Type 'y' to get another card, or 'n' to  pass: ").lower()
        if request == 'y':
            playerCard.append(randdom())
            winner()
        else:
            winner()
        
    initial()
    blackjack()
    again= input("Do you want to play a game of BlackJack? Type 'y' for Yes or 'n' for No: ").lower()
    if again == 'y':
        playerCard = []
        computerCard = []
        initial()
        blackjack()
    else:
        print('Thank You for playing')
        decide = False

