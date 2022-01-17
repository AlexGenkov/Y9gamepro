import os,time

playAgain="1"

def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again: ")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer)

def animation():
    os.system('clear')
    filenames= ["animation1.txt", "animation2.txt", "animation3.txt", "animation4.txt", "animation5.txt", "animation6.txt", "animation7.txt", "animation8.txt", "animation9.txt", "animation10.txt", "animation11.txt", "animation12.txt", "animation13.txt", "animation14.txt"]
    frames = []

    for name in filenames:
        with open(name,"r", encoding="utf8") as f:
            frames.append (f.readlines()) 

    for frame in frames:
        print("".join(frame))
        time.sleep(0.5)
        os.system('clear')

while playAgain=="1":
    print("                                                                                                                                   =========WELCOME TO QUIZ SYSTEM==========")
    print("-----------------------------------------")
    print("Type 1 to... PLAY QUIZ")
    print("Type 2 to... LEARN ABOUT THE PROJECT")
    choice = int(input('ENTER YOUR CHOICE: '))
    if choice ==2:
        print("                                                                                                                                   Hi, Im Alexander Genkov, a year 9 student at Upper Canada College. I have made this quiz game loosly on the story of Jabari Jumps. A increaible childrens book by Gaia Cornwall. Please enjoy the game.")

        print("                                                                                                                                   Oh no, the diving board at the pool house is broke! Jabri is sad but he has hope because you are here! You can fix the diving board by answering the following questions correctly there are 9 questions in total. You must get all 9 question correct to fix the diving board. If you don't... Dont worry, you have three aptempts on each question, in the vent that you do fail, continue going to train your knowledge. Good luck :) !")
    
    else:
        print("                                                                                                                                   Oh no, the diving board at the pool house is broke! Jabri is sad but he has hope because you are here! You can fix the diving board by answering the following questions correctly there are 9 questions in total. You must get all 9 question correct to fix the diving board. If you don't... Dont worry, you have three aptempts on each question, in the vent that you do fail, continue going to train your knowledge. Good luck :) !")


        
    score = 0
    print("                                                                                                                                   Answer the questions to the best of your ability:                                                                                                                                    ")

    guess1 = input("Jabri wants a soda from the vending mechine. Jabri has a toonie, five dollar bill, and a quater. If the Soda cost $2.25, can Jabari pay in exact change? Y for Yes| N for No: ")
    check_guess(guess1, "y")
    guess2 = input("Jabri Has two cookies and he wants to share them with his brother and father! What fraction of 1 cookie does each person get? Use the / as a fraction line:  ")
    check_guess(guess2, "2/3")
    guess3 = input("At the pool there is a lady painting, she is about to mix the colours Blue and yellow together. If she mixes red with that colour, what colour will she make?: ")
    check_guess(guess3, "brown")
    guess4 = input("Jabri sees a boy getting bullied at the pool house. Should he tell the bullies to stop Y for Yes| N for No: ")
    check_guess(guess4, "y")
    guess5 = input("Jabri and his two friends Mike and Dave want to see the baseball game over the fence. Jabri is tall enough to see over the fence if he stands on 1 box Dave needs two boxes to see over the fence but he uses three to get the best view. Mike needs one box but he has none because Dave took the last ones. Who needs to give Mike a box?: ")
    check_guess(guess5, "dave")
    guess6 = input("Later on Jabri and his friends are playing marbles. All the marbles are green! Dave says, this is a diverse colection of marbles of you Jabari! Is this statement true or False?: ")
    check_guess(guess6, "false")
    guess7 = input("Mike pulls of his set of marbles. They have many crazy patterns on then and they are all coloured differently! Would you consider this set of marbles to be diverse? Y for Yes| N for No: ")
    check_guess(guess7, "y")
    guess8 = input("While you are playing, a boy you do not know comes up to you and askes if he can play. Mike and Dave say no! Was this a nice action? Y for Yes| N for No: ")
    check_guess(guess8, "n")
    guess9 = input("Should Jabri include him in the game? Y for Yes| N for No:: ")
    check_guess(guess9, "y")
    print("Your Score is "+ str(score))

    if score==9:
        animation()
    else:
        print(" Oh No. You were unable to fix the diving board. Please Try again!")
    print("Do you want to play again?")

    playAgain = input("Please Type 1 for Yes or 2 for No: ")