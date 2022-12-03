import random
runs,comp_runs,toss=0,0,0
print("Welcome to hand cricket!! You have to defend/chase the score inorder to win like real cricket.")
print("The condition for getting out is that the computer and the user have to produce the same number.")
print("-----------------------------------------------------------------------------------------------------")


def toss():
 print("User's number and the computer's number will be added. Choose within 1-6.")
 user_toss=int(input("Choose a number between 1-6. If it's even user wins the toss!!  "))
 if user_toss>6 :
    print("Choose between 1 and 6 only.")
    toss_again()
 print("User have chosen: ",user_toss)    
 comp_toss=random.choice([1,2,3,4,5,6])
 print("Computer have chosen: ",comp_toss)  
 toss=comp_toss+user_toss
 if toss==2 or toss==4 or toss==6 or toss==8 or toss==10 or toss==12:
    select=input("User have won the toss!! What would you choose to do? Bat/Ball: ").upper()
    if select=='BAT':
        print("User has chosen to bat first....")
        batting_first()
    elif select=='BALL':
        print("User has to bowl first....")
        bowling_first()
 else:
    comp1=random.choice([1,2])
    if comp1==1:
        print("Computer has chosen to bat first!! GAME STARTS!!")
        bowling_first()
    elif comp1==2:
        print("Computer has chosen to bowl first!! GAME STARTS!!")
        batting_first()
    else:
        print("There is a flaw in coin , User have been asked to bat first. GAME STARTS!!")
        batting_first()
        
def batting_first():
 print("User will have to bat now, choose a number between 1 and 6.")
 print("Choosing a number higher than 6 isn't allowed and user will be sent back!")
 print("If user choose a number the same as the computer user will be out!!")
 runs=0
 while True:
        comp_number = random.choice([1,2,3,4,5,6])
        user_number = int(input("User's number will be: "))
        runs+=user_number
        if comp_number == user_number or user_number > 6:
            print("Computer has chosen ",comp_number,"!!!")
            print("User is OUT! User have scored,", runs - user_number," runs.")
            runs = runs - user_number
            print("User will bowl now.....")
            bowling_second()
            break
        if runs > 50:
            print("A fine knock- you can see the batsmen is in form here.")
        elif runs > 100:
            print("This batsman is exceptional. A fab innings.")
        else:
            print("Computer has chosen: ", comp_number)
            print("So far you have scored ", runs," runs")
        
def bowling_first():
   print("To get the computer out chose the same number as the computer!!!")
   comp_runs=0
   while True:
        comp_number = random.choice([1,2,3,4,5,6])
        user_number = int(input("What is user's number? "))
        comp_runs+= comp_number
        print("Computer has chosen: ", comp_number)
        if comp_number == user_number:
            print("User has got the Computer out!!")
            #comp_runs = comp_runs - user_number
            batting_second()
        elif comp_runs < 0:
          comp_runs = 0
            
          print("Computer has scored ",comp_runs-user_number, " runs.")
          batting_second()
          break
        else:
            print("So far Computer has scored ", comp_runs," runs.")
 
def batting_second():
    print("User will have to bat now. To win user need..",(comp_runs), " runs.")
    print("Choose a number between 1 to 6.")
    print("If user choose a number same as the computer user will be out!!")
    runs=0
    while True:
        comp_number = random.choice([1,2,3,4,5,6])
        user_number = int(input("What is user's number? "))
        runs+=user_number
        if runs > comp_runs:
            print("Computer has chosen: ",comp_number,".")
            print("User has scored", runs)
            print("What an amazing win, user beat the computer.")
            end()
        if comp_number == user_number or user_number > 6:
            print("Computer has chosen",comp_number,"!!!")
            print("User is OUT! User have scored: ",runs - user_number)
            runs = runs - user_number
            if runs < comp_runs:
                print("Unlucky, the computer has beaten user by ",comp_runs - runs , "runs.")
                end()
                break
            if runs > 50:
                print("What a fabulous innings!")
            elif runs > 100:
                print("A marvellous innings!!")
        else:
            print("Computer has chosen ", comp_number,".")
            print("So far user have scored ",runs,"runs.")
        
def bowling_second():
    print("To get the computer out chose the same number as the computer!")
    comp_runs=0
    while True:
        comp_number = random.choice([1,2,3,4,5,6])
        user_number = int(input("What is user's number? "))
        comp_runs+=comp_number
        if comp_runs > runs:
            print("Computer is at ",comp_runs, '!!!')
            print("That was a close one... The Computer has beaten user!!")
            end()
            break
        elif comp_number == user_number and comp_runs < runs:
            print("The computer chose ",comp_number,"!!!")
            print("Well done, what a great win!! User have won by ", runs - comp_runs, "runs.")
            end()
            break
        else:
            print("Computer has chosen: ",comp_number)
            print("Computer has scored: ", comp_runs, "runs")  
        
def toss_again():        
  print("Let's toss!!")
  toss()
 
def end():
        answer = input(("Would you like a rematch? (Y/N): ")).upper()
        if answer == "Y":
            print("Ok!! Let's do the toss!!")
            toss()
        if answer == "N":
          print("Thanks for playing! You were an excellent cricketer!")
toss_again()               