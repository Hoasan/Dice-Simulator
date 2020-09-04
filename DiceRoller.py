import random

def main():
    p1 = 0
    p2 = 0
    p1score = 0
    p2score = 0
    try:
     rolls = input("How many rounds would you like? ")

     for i in range(int(rolls)):
        print("Round " + str(i + 1))
        p1 = dice_roll()
        p2 = dice_roll()
        print("Player 1 Roll: " + str(p1))
        print("Player 2 Roll: " + str(p2))
        
        if p1 == p2:
            print("Draw")
        elif p1 > p2:
            p1score += 1
            print("Player 1 Wins!")
        else:
            p2score += 1
            print("Player 2 Wins!") 
     if p1score == p2score:
       print("It's a draw!")
     elif p1score > p2score:
       print("Player 1 has won the game! Rounds won: " + str(p1score))
     else:
      print("Player 2 has won the game! Rounds won: " + str(p2score))
    except:
      print("This isn't a number!")

def dice_roll():
    diceRoll = random.randint(1, 6)
    return diceRoll
    
main()