#    PROJECT 1 = SNAKE WATER GUN GAME

import random
def snake_water_gun_game():
        print("welcome to snake water gun game")
        print("Press 'q' to exit")
        
        options=['snake','water','gun']
        rounds=0
        player_score=0
        computer_score=0

        while True:
                print("\n round", rounds+1)
                print(f"score:your{player_score}-computer{computer_score}")

                computer=random.choice(options)
                player=input("enter your choice(snake/water/gun)or 'exit' to quit:").lower()

                if player==exit:
                        break
                if player not in options:
                        print("invalid ,try again")
                        continue
                rounds+=1
                print(f"/n your choice{player}")
                print(f"computer choice{computer}")
                        #  determine the winner:
                
                if player==computer:
                        print("it is tie")
                elif (player=="snake" and computer=="water") or\
                    (player=="water" and computer=="gun")or\
                    (player=="gun" and computer=="snake"):
                        print("you win this round")
                        player_score+=1
                else:
                    print("computer win")
                    computer_score+=1
                print("/n final score")
                print(f"your score{player_score},computer score{computer_score}")
                if player_score >computer_score:
                       print("You Won the game")
                elif computer_score > player_score:
                       print("computer won the game")
                else:
                       print("game ended in a tie")
                print("thanks ! for playing")

a=snake_water_gun_game()
print(a)