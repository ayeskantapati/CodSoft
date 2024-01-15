import random

def play_game():
    print("game Menu\n1- Rock\n2- Paper\n3- Scissors")
    us=int(input("Enter your Choice :"))
    if us==1:
        u='rock'
    elif us==2:
        u='paper'
    elif us==3:
        u='scissors'
    else:
        print("Enter Valid Choice...")
        return
    cc= random.choice(["rock", "paper", "scissors"])
    print("Your Choice is ",u,"& Computer choce is ",cc)
    if u == cc:
        print("It's a tie!\nbecause both are chose same choice :",cc)
    elif us==1 and cc=='scissors' or us==2 and cc=='rock' or us==3 and cc=='paper':
        print("Congratulation You win...")
    else:
        print("Computer wins!")
while 1:
    play_game()
    x=input("Do you want to continue(y/n) :")
    if x!='y':
        break
print("Game Terminated...!\nThanks for playing...!")