import random


def main():
    gameOver = False
    while not gameOver:
        choices = ['rock', 'paper', 'scissors']
        print("Choose rock, paper, or scissors:")

        player = ""
        while player not in choices:
            player = input().strip().lower()
            if player not in choices:
                print("Please input either rock, paper, or scissors!")
        player = choices.index(player)
        cpu = random.randint(0, 2)
        print(f"Opponent chose {choices[cpu]}!")
        if player == cpu:
            print("Tie game!")
        elif player == 0:
            if cpu == 1:
                print("Opponent wins!")
            else:
                print("You win!")
        elif player == 1:
            if cpu == 2:
                print("Opponent wins!")
            else:
                print("You win!")
        elif player == 2:
            if cpu == 0:
                print("Opponent wins!")
            else:
                print("You win!")
        state = input("Would you like to play again? (y/n): ")
        if state != 'y':
            gameOver = True


main()
