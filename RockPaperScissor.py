# Rock Paper Scissor

import random
c = 0;
u = 0;

go = "y"
while(go is not "n"):
    swg = [ "rock","paper","scissor" ]
    ch = random.choice(swg)
    print(ch)
    print("Select your choice: R for Rock  P for Paper  S for Scissor")
    ans = input("\nEnter:").lower()

    if (ans == "r"):
        ck = "rock"
    elif (ans == "p"):
        ck = "paper"
    elif (ans == "s"):
        ck = "scissor"
    else:
        print("Invalid selection.. Please select R , P or S")
        continue

    print(ck)
    if (((ck == "rock") & (ch == "scissor")) | ((ck == "paper") & (ch == "rock")) | ((ck == "scissor") & (ch == "paper"))):
        print("You Won part of match")
        u += 1

    elif(((ch == "rock") & (ck == "scissor")) | ((ch == "paper") & (ck == "rock")) | ((ch == "scissor") & (ck == "paper"))):
        print("Computer Won part of match")
        c +=1

    elif((ch == "rock") & (ck == "rock") | (ch == "paper") & (ck == "paper") | (ch == "scissor") & (ck == "scissor")):
        print("Tie")

    k="y"
    while(k is not "n"):
        k = input("Do you want to continue? Y / N").lower()
        if (k == "y"):
            break
        elif(k == "n"):
            go = "n"
            break
        else:
            print("Invalid input, Please press Y or N")


print(f"\n Your Score = {u} \n Computer score = {c}")

if (u > c):
    print("You won the match")
elif(u == c):
    print("Match Tie")
else:
    print("Computer won the match, Next time better luck")

print("Thanks for playing game..!! Visit again")
