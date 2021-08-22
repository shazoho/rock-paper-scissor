import random
userchoice=input("Enter a choice (Rocks, Paper, and Scissors):")
choicelist=["Rocks", "Paper", "Scissors"]
computerchoice=random.choice(choicelist)
if userchoice==computerchoice:
    print("TIE!")
elif ((userchoice=="Rocks" and computerchoice=="Paper") or (userchoice=="Paper" and computerchoice=="Scissors") or (userchoice=="Scissors" and computerchoice=="Rocks")):
    print("Computer wins!")
elif((userchoice=="Rocks" and computerchoice=="Scissors") or(userchoice=="Paper" and computerchoice=="Rocks") or(userchoice=="Scissors" and computerchoice=="Paper")):
    print("You win!")
