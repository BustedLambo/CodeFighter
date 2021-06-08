import random
import time

from os import system, name
def clear():
  if name == "nt":
    _=system('cls')
  else:
    _=system("clear")

clear()



print("=> ")
print("\a"*1)
time.sleep(1.5)
clear()

print("=> C")
print("\a"*1)
time.sleep(0.05)
clear()

print("=> Co")
print("\a"*1)
time.sleep(0.05)
clear()

print("=> Code")
print("\a"*1)
time.sleep(0.05)
clear()

print("=> CodeFi")
print("\a"*1)
time.sleep(0.05)
clear()

print("=> CodeFig")
print("\a"*1)
time.sleep(0.05)
clear()

print("=> CodeFigh")
print("\a"*1)
time.sleep(0.05)
clear()

print("=> CodeFight")
print("\a"*1)
time.sleep(0.05)
clear()

print("=> CodeFighte")
print("\a"*1)
time.sleep(0.05)
clear()

print("=> CodeFighter")
print("\a"*1)
time.sleep(1.25)
clear()


print("=> CodeFighter!")
print("\a"*3)
time.sleep(1.25)
clear()

print("=> CodeFighter!!")
print("\a"*3)
time.sleep(4.5)
clear()
time.sleep(1.5)

print("=> Made by A.J.D using Repl.it (Like Streetfighter But it's in a console and written in python and not pixel arcade machine :)")
print("\a"*3)


time.sleep(3.5)
clear()
time.sleep(1.25)
print("\a"*3)
clear()
game=input("START: ")

clear()

keepplaying=True



gameinprogress = 0

score1=0
score2=0

score12=0
score22=0

hs=0
hs1=0

go=1
while go == 1:

  time.sleep(1.95)
  clear()
  print("<~~~~~~~~~~~~~~>")
  print("   GAME MENU:")
  print("<~~~~~~~~~~~~~~>")


  print("\n(1) 1 Player Mode ")
  print("(2) 2 Player Mode (Local Co-Op)")

  print("(3) Quit Game")

  choice=input("\n=> ")

  

  num=['1','2','3','4']

  
        
      

      













  if choice == "3":
    time.sleep(0.5)
    clear()
    print("Are you sure you want to leave the game? None of your progress will be saved.")
    print("\n(1) YES")
    print("(2) NO")
    leave1=['1']
    leave=input("\n=> ")
    if leave in leave1:
      clear()
      time.sleep(2)
      break
    if leave not in leave1:
      clear()
      time.sleep(2)
      continue



  if choice == "2":
    go=1
    while go == 1:

      player1health = 100
      if player1health > 100:
        player1health = 100

      player2health = 100
      if player2health > 100:
        player2health = 100

      clear()
      time.sleep(0.5)
      print("<~~~~~~~~~~~~~~~~>")
      print("  2 PLAYER MODE:")
      print("<~~~~~~~~~~~~~~~~>")
      print("\nCurrent Score: ")
      print("\n=> Player 1: "+str(score12))
      print("=> Player 2: "+str(score22))

      name1= "Player 1"
      name2= "Player 2"

      response=input("\n(1) START\n(2) END SESSION\n\n=> ")

      if response == "1":
        gameinprogress += 1
        time.sleep(2.5)
        clear()
        time.sleep(1.5)
        print("First, determine who will be Player 1 and who will be Player 2 before playing.")
        time.sleep(3)
        clear()
        time.sleep(1.5)
      if response == "2":
        clear()
        time.sleep(1.5)
        clear()
        break

      while gameinprogress == 1:

        

        play = 1
        if play == 1:
          clear()
          time.sleep(0.5)

          print("<~~~~~~~~~~~~~~~~~~~~~~~>")
          print("  PLAYER 1 ATTACK MENU:")
          print("<~~~~~~~~~~~~~~~~~~~~~~~>")

          print("\nHP:")

          if (player1health >= 1) and (player1health <= 10):
            print("=")
          if (player1health >= 11) and (player1health <= 20):
            print("==")
          if (player1health >= 21) and (player1health <= 30):
            print("===")
          if (player1health >= 31) and (player1health <= 40):
            print("====")
          if (player1health >= 41) and (player1health <= 50):
            print("=====")
          if (player1health >= 51) and (player1health <= 60):
            print("======")
          if (player1health >= 61) and (player1health <= 70):
            print("=======")
          if (player1health >= 71) and (player1health <= 80):
            print("========")
          if (player1health >= 81) and (player1health <= 90):
            print("=========")
          if (player1health >= 91) and (player1health <= 100):
            print("==========")

          print(str(player1health)+"/100")

          print("\nENEMY HP:")

          if (player2health >= 1) and (player2health <= 10):
            print("=")
          if (player2health >= 11) and (player2health <= 20):
            print("==")
          if (player2health >= 21) and (player2health <= 30):
            print("===")
          if (player2health >= 31) and (player2health <= 40):
            print("====")
          if (player2health >= 41) and (player2health <= 50):
            print("=====")
          if (player2health >= 51) and (player2health <= 60):
            print("======")
          if (player2health >= 61) and (player2health <= 70):
            print("=======")
          if (player2health >= 71) and (player2health <= 80):
            print("========")
          if (player2health >= 81) and (player2health <= 90):
            print("=========")
          if (player2health >= 91) and (player2health <= 100):
            print("==========")

          print(str(player2health)+"/100")

          print("\n(1) Blaze Strike -Deals moderate damage. (7-11)")
          print("(2) Spitting Fire -Deals high or low damage, depending on chance. (4-15)")
          print("(3) Inner Focus -Heals a moderate amount of HP. (6-10)")

          print("\n(4) Quit Game")
        

          moves=['1','2','3','4']

          attack = input("\n=> ")

          name1 = "Player 1"
          name2 = "Player 2"

          notin = 0

          if attack == "4":
            time.sleep(0.75)
            clear()
            print("Are you sure you want to leave the game?\n\n(1) YES\n(2) NO")
            leave=input("\n=> ")
            if leave == "1":
              gameinprogress -=1
              notin = 1
              time.sleep(0.75)
              clear()
              print("It's a draw! Nobody wins!")
              time.sleep(3.5)
              clear()
            
            if leave == "2":
              notin = 1
              time.sleep(0)
              continue

          if attack == "1":
            time.sleep(0.75)
            clear()
          if attack == "2":
            time.sleep(0.75)
            clear()
          if attack == "3":
            time.sleep(0.75)
            clear()

          if attack not in moves:

            notin = 1
            time.sleep(0.75)
            clear()
            print("That was not a valid move. Please select the digits 1, 2, 3, or 4 next time while performing an attack.")
            time.sleep(3.5)
          
            clear()

          if notin == 1:
            time.sleep(0)

          if notin == 0:
            go=1
            if go == 1:
              clear()
              time.sleep(0.5)

              print("<~~~~~~~~~~~~~~~~~~~~~~~>")
              print("  PLAYER 2 ATTACK MENU:")
              print("<~~~~~~~~~~~~~~~~~~~~~~~>")

              print("\nHP: ")

              if (player2health >= 1) and (player2health <= 10):
                print("=")
              if (player2health >= 11) and (player2health <= 20):
                print("==")
              if (player2health >= 21) and (player2health <= 30):
                print("===")
              if (player2health >= 31) and (player2health <= 40):
                print("====")
              if (player2health >= 41) and (player2health <= 50):
                print("=====")
              if (player2health >= 51) and (player2health <= 60):
                print("======")
              if (player2health >= 61) and (player2health <= 70):
                print("=======")
              if (player2health >= 71) and (player2health <= 80):
                print("========")
              if (player2health >= 81) and (player2health <= 90):
                print("=========")
              if (player2health >= 91) and (player2health <= 100):
                print("==========")

              print(str(player2health)+"/100")

              print("\nENEMY HP:")

              if (player1health >= 1) and (player1health <= 10):
                print("=")
              if (player1health >= 11) and (player1health <= 20):
                print("==")
              if (player1health >= 21) and (player1health <= 30):
                print("===")
              if (player1health >= 31) and (player1health <= 40):
                print("====")
              if (player1health >= 41) and (player1health <= 50):
                print("=====")
              if (player1health >= 51) and (player1health <= 60):
                print("======")
              if (player1health >= 61) and (player1health <= 70):
                print("=======")
              if (player1health >= 71) and (player1health <= 80):
                print("========")
              if (player1health >= 81) and (player1health <= 90):
                print("=========")
              if (player1health >= 91) and (player1health <= 100):
                print("==========")

              print(str(player1health)+"/100")

              print("\n(1) Blaze Strike -Deals moderate damage. (7-11)")
              print("(2) Spitting Fire -Deals high or low damage, depending on chance. (4-15)")
              print("(3) Inner Focus -Heals a moderate amount of HP. (6-10)")

              print("\n(4) Quit Game")

              moves=['1','2','3','4']

              attack1 = input("\n=> ")

              name1= "Player 1"
              name2= "Player 2"

              notin1 = 0

              if attack1 == "4":
                time.sleep(0.75)
                clear()
                print("Are you sure you want to leave the game?\n\n(1) YES\n(2) NO")
                leave1=input("\n=> ")
                if leave1 == "1":
                  gameinprogress -=1
                  notin = 1
                  time.sleep(0.75)
                  clear()
                  print("It's a draw! Nobody wins!")
                  time.sleep(3.5)
                  clear()
            
                if leave1 == "2":
                  notin1 = 1
                  time.sleep(0)
                  continue

              if attack1 not in moves:

                notin1 = 1
                time.sleep(0.75)
                clear()
                print("That was not a valid move. Please select the digits 1, 2, 3, or 4 next time while performing an attack.")
                time.sleep(3.5)
          
                clear()

              if attack1 == "1":
                time.sleep(0.75)
                clear()
              if attack1 == "2":
                time.sleep(0.75)
                clear()
              if attack1 == "3":
                time.sleep(0.75)
                clear()

              if notin1 == 1:
                time.sleep(0)

              if notin == 0:
                go2 = 1
                if go2 == 1:
                  if (attack == "1") and (attack1 == "1"):
                    damage=random.randint(7, 11)
                    player2health-=damage
                    time.sleep(0.75)
                    clear()
                    print(str(name2)+" takes -"+str(damage)+" from "+str(name1)+"'s Blaze Strike! "+str(name2)+" now has "+str(player2health)+" HP remaining.")
                    time.sleep(3.5)
                    clear()
                    if (player2health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name1)+", has defeated "+str(name2)+"! Way to go!")
                      time.sleep(3)
                      score12+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    if (player1health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name2)+", has defeated "+str(name1)+"! Way to go!")
                      time.sleep(3)
                      score22+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    damage1=random.randint(7, 11)
                    player1health-=damage
                    time.sleep(0.75)
                    clear()
                    print(str(name1)+" takes -"+str(damage)+" from "+str(name2)+"'s Blaze Strike! "+str(name1)+" now has "+str(player1health)+" HP remaining.")
                    time.sleep(3.5)
                    clear()
                    if (player2health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name1)+", has defeated "+str(name2)+"! Way to go!")
                      time.sleep(3)
                      score12+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    if (player1health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name2)+", has defeated "+str(name1)+"! Way to go!")
                      time.sleep(3)
                      score22+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue
                  if (attack == "1") and (attack1 == "2"):
                    damage=random.randint(7, 11)
                    player2health-=damage
                    time.sleep(0.75)
                    clear()
                    print(str(name2)+" takes -"+str(damage)+" from "+str(name1)+"'s Blaze Strike! "+str(name2)+" now has "+str(player2health)+" HP remaining.")
                    time.sleep(3.5)
                    clear()
                    if (player2health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name1)+", has defeated "+str(name2)+"! Way to go!")
                      time.sleep(3)
                      score12+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    if (player1health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name2)+", has defeated "+str(name1)+"! Way to go!")
                      time.sleep(3)
                      score22+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    damage1=random.randint(7, 11)
                    player1health-=damage
                    time.sleep(0.75)
                    clear()
                    print(str(name1)+" takes -"+str(damage)+" from "+str(name2)+"'s Spitting Fire! "+str(name1)+" now has "+str(player1health)+" HP remaining.")
                    time.sleep(3.5)
                    clear()
                    if (player2health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name1)+", has defeated "+str(name2)+"! Way to go!")
                      time.sleep(3)
                      score12+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    if (player1health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name2)+", has defeated "+str(name1)+"! Way to go!")
                      time.sleep(3)
                      score22+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue
                  if (attack == "1") and (attack1 == "3"):
                    damage=random.randint(7, 11)
                    player2health-=damage
                    time.sleep(0.75)
                    clear()
                    print(str(name2)+" takes -"+str(damage)+" from "+str(name1)+"'s Blaze Strike! "+str(name2)+" now has "+str(player2health)+" HP remaining.")
                    time.sleep(3.5)
                    clear()
                    if (player2health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name1)+", has defeated "+str(name2)+"! Way to go!")
                      time.sleep(3)
                      score12+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    if (player1health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name2)+", has defeated "+str(name1)+"! Way to go!")
                      time.sleep(3)
                      score22+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    heal1=random.randint(6, 10)
                    player2health+=heal1
                    if player2health >= 101:
                      player2health = 100
                      time.sleep(0.75)
                      clear()
                      print("You healed yourself even though you already had 100 HP. Your HP has stayed consistent.")
                      time.sleep(3.5)
                      clear()
                      time.sleep(0.75)
                      clear()
                      
                    print(str(name2)+" used Inner Focus! It healed +"+str(heal1)+" HP. "+str(name2)+" now has "+str(player2health)+" HP.")
                    time.sleep(3.5)
                    clear()
                    if (player2health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name1)+", has defeated "+str(name2)+"! Way to go!")
                      time.sleep(3)
                      score12+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    if (player1health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name2)+", has defeated "+str(name1)+"! Way to go!")
                      time.sleep(3)
                      score22+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue







                  if (attack == "2") and (attack1 == "2"):
                    damage=random.randint(7, 11)
                    player2health-=damage
                    time.sleep(0.75)
                    clear()
                    print(str(name2)+" takes -"+str(damage)+" from "+str(name1)+"'s Spitting Fire! "+str(name2)+" now has "+str(player2health)+" HP remaining.")
                    time.sleep(3.5)
                    clear()
                    if (player2health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name1)+", has defeated "+str(name2)+"! Way to go!")
                      time.sleep(3)
                      score12+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    if (player1health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name2)+", has defeated "+str(name1)+"! Way to go!")
                      time.sleep(3)
                      score22+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue


                    damage1=random.randint(7, 11)
                    player1health-=damage
                    time.sleep(0.75)
                    clear()
                    print(str(name1)+" takes -"+str(damage)+" from "+str(name2)+"'s Spitting Fire! "+str(name1)+" now has "+str(player1health)+" HP remaining.")
                    time.sleep(3.5)
                    clear()
                    if (player2health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name1)+", has defeated "+str(name2)+"! Way to go!")
                      time.sleep(3)
                      score12+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    if (player1health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name2)+", has defeated "+str(name1)+"! Way to go!")
                      time.sleep(3)
                      score22+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue
                  if (attack == "2") and (attack1 == "3"):
                    damage=random.randint(7, 11)
                    player2health-=damage
                    time.sleep(0.75)
                    clear()
                    print(str(name2)+" takes -"+str(damage)+" from "+str(name1)+"'s Spitting Fire! "+str(name2)+" now has "+str(player2health)+" HP remaining.")
                    time.sleep(3.5)
                    clear()
                    if (player2health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name1)+", has defeated "+str(name2)+"! Way to go!")
                      time.sleep(3)
                      score12+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    if (player1health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name2)+", has defeated "+str(name1)+"! Way to go!")
                      time.sleep(3)
                      score22+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    heal1=random.randint(6, 10)
                    player2health+=heal1
                    if player2health >= 101:
                      player2health = 100
                      time.sleep(0.75)
                      clear()
                      print("You healed yourself even though you already had 100 HP. Your HP has stayed consistent.")
                      time.sleep(3.5)
                      clear()
                      time.sleep(0.75)
                      clear()
                    print(str(name2)+" used Inner Focus! It healed +"+str(heal1)+" HP. "+str(name2)+" now has "+str(player2health)+" HP.")
                    time.sleep(3.5)
                    clear()
                    if (player2health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name1)+", has defeated "+str(name2)+"! Way to go!")
                      time.sleep(3)
                      score12+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    if (player1health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name2)+", has defeated "+str(name1)+"! Way to go!")
                      time.sleep(3)
                      score22+=1
                      gameinprogress -= 1

                      time.sleep(0)
                      continue
                  if (attack == "2") and (attack1 == "1"):
                    damage=random.randint(7, 11)
                    player2health-=damage
                    time.sleep(0.75)
                    clear()
                    print(str(name2)+" takes -"+str(damage)+" from "+str(name1)+"'s Spitting Fire! "+str(name2)+" now has "+str(player2health)+" HP remaining.")
                    time.sleep(3.5)
                    clear()
                    if (player2health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name1)+", has defeated "+str(name2)+"! Way to go!")
                      time.sleep(3)
                      score12+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    if (player1health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name2)+", has defeated "+str(name1)+"! Way to go!")
                      time.sleep(3)
                      score22+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    damage1=random.randint(7, 11)
                    player1health-=damage
                    time.sleep(0.75)
                    clear()
                    print(str(name1)+" takes -"+str(damage)+" from "+str(name2)+"'s Spitting Fire! "+str(name1)+" now has "+str(player1health)+" HP remaining.")
                    time.sleep(3.5)
                    clear()
                    if (player2health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name1)+", has defeated "+str(name2)+"! Way to go!")
                      time.sleep(3)
                      score12+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    if (player1health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name2)+", has defeated "+str(name1)+"! Way to go!")
                      time.sleep(3)
                      score22+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    





                  if (attack == "3") and (attack1 == "3"):
                    heal=random.randint(6, 10)
                    player1health+=heal
                    if player1health >= 101:
                      yourhealth = 100
                      time.sleep(0.75)
                      clear()
                      print("You healed yourself even though you already had 100 HP. Your HP has stayed consistent.")
                      time.sleep(3.5)
                      clear()
                      time.sleep(0.75)
                      clear()
                    print(str(name1)+" used Inner Focus! It healed +"+str(heal)+" HP. "+str(name1)+" now has "+str(player1health)+" HP.")
                    time.sleep(3.5)
                    clear()
                    if (player2health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name1)+", has defeated "+str(name2)+"! Way to go!")
                      time.sleep(3)
                      score12+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    if (player1health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name2)+", has defeated "+str(name1)+"! Way to go!")
                      time.sleep(3)
                      score22+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    heal1=random.randint(6, 10)
                    player2health+=heal1
                    if player2health >= 101:
                      player2health = 100
                      time.sleep(0.75)
                      clear()
                      print("You healed yourself even though you already had 100 HP. Your HP has stayed consistent.")
                      time.sleep(3.5)
                      clear()
                      time.sleep(0.75)
                      clear()
                    print(str(name2)+" used Inner Focus! It healed +"+str(heal1)+" HP. "+str(name2)+" now has "+str(player2health)+" HP.")
                    time.sleep(3.5)
                    clear()
                    if (player2health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name1)+", has defeated "+str(name2)+"! Way to go!")
                      time.sleep(3)
                      score12+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    if (player1health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name2)+", has defeated "+str(name1)+"! Way to go!")
                      time.sleep(3)
                      score22+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue
                  if (attack == "3") and (attack1 == "1"):
                    heal=random.randint(6, 10)
                    player1health+=heal
                    if player1health >= 101:
                      yourhealth = 100
                      time.sleep(0.75)
                      clear()
                      print("You healed yourself even though you already had 100 HP. Your HP has stayed consistent.")
                      time.sleep(3.5)
                      clear()
                      time.sleep(0.75)
                      clear()
                    print(str(name1)+" used Inner Focus! It healed +"+str(heal)+" HP. "+str(name1)+" now has "+str(player1health)+" HP.")
                    time.sleep(3.5)
                    clear()
                    if (player2health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name1)+", has defeated "+str(name2)+"! Way to go!")
                      time.sleep(3)
                      score12+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    if (player1health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name2)+", has defeated "+str(name1)+"! Way to go!")
                      time.sleep(3)
                      score22+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    damage1=random.randint(7, 11)
                    player1health-=damage
                    time.sleep(0.75)
                    clear()
                    print(str(name1)+" takes -"+str(damage)+" from "+str(name2)+"'s Spitting Fire! "+str(name1)+" now has "+str(player1health)+" HP remaining.")
                    time.sleep(3.5)
                    clear()
                    if (player2health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name1)+", has defeated "+str(name2)+"! Way to go!")
                      time.sleep(3)
                      score12+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    if (player1health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name2)+", has defeated "+str(name1)+"! Way to go!")
                      time.sleep(3)
                      score22+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue
                  if (attack == "3") and (attack1 == "2"):
                    heal=random.randint(6, 10)
                    player1health+=heal
                    if player1health >= 101:
                      yourhealth = 100
                      time.sleep(0.75)
                      clear()
                      print("You healed yourself even though you already had 100 HP. Your HP has stayed consistent.")
                      time.sleep(3.5)
                      clear()
                      time.sleep(0.75)
                      clear()
                    print(str(name1)+" used Inner Focus! It healed +"+str(heal)+" HP. "+str(name1)+" now has "+str(player1health)+" HP.")
                    time.sleep(3.5)
                    clear()
                    if (player2health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name1)+", has defeated "+str(name2)+"! Way to go!")
                      time.sleep(3)
                      score12+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    if (player1health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name2)+", has defeated "+str(name1)+"! Way to go!")
                      time.sleep(3)
                      score22+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    damage1=random.randint(7, 11)
                    player1health-=damage
                    time.sleep(0.75)
                    clear()
                    print(str(name1)+" takes -"+str(damage)+" from "+str(name2)+"'s Spitting Fire! "+str(name1)+" now has "+str(player1health)+" HP remaining.")
                    time.sleep(3.5)
                    clear()
                    if (player2health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name1)+", has! defeated "+str(name2)+"! Way to go!")
                      time.sleep(3)
                      score12+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue

                    if (player1health <= 0):
                      time.sleep(0.75)
                      clear()
                      print("You, "+str(name2)+", has defeated "+str(name1)+"! Way to go!")
                      time.sleep(3)
                      score22+=1
                      gameinprogress -= 1
                      time.sleep(0)
                      continue
      

        





            
              

















  if choice == "1":
    go = 1
    while go == 1:

  

      yourhealth=100
      if yourhealth > 100:
        yourhealth = 100
      robothealth=100
      if robothealth > 100:
        robothealth = 100



  
  
      clear()
      time.sleep(0.5)
      print("<~~~~~~~~~~~~~~~~>")
      print("  1 PLAYER MODE:")
      print("<~~~~~~~~~~~~~~~~>")
      print("\nCurrent Score: ")
      print("\n=> You: "+str(score1))
      print("=> Enemy (Computer): "+str(score2))
      
      
      


      
      name == "Player 1"

      



      response=input("\n(1) START\n(2) END SESSION\n\n=> ")
      

      if response == "1":
        gameinprogress +=1
      if response == "2":
        clear()
        time.sleep(1.5)
        clear()
        break
    


      while gameinprogress == 1:

    
        time.sleep(2.5)
        clear()
        time.sleep(1.5)

        print("<~~~~~~~~~~~~~~>")
        print("  ATTACK MENU: ")
        print("<~~~~~~~~~~~~~~>")

        print("\nHP:")

        if (yourhealth >= 1) and (yourhealth <= 10):
          print("=")
        if (yourhealth >= 11) and (yourhealth <= 20):
          print("==")
        if (yourhealth >= 21) and (yourhealth <= 30):
          print("===")
        if (yourhealth >= 31) and (yourhealth <= 40):
          print("====")
        if (yourhealth >= 41) and (yourhealth <= 50):
          print("=====")
        if (yourhealth >= 51) and (yourhealth <= 60):
          print("======")
        if (yourhealth >= 61) and (yourhealth <= 70):
          print("=======")
        if (yourhealth >= 71) and (yourhealth <= 80):
          print("========")
        if (yourhealth >= 81) and (yourhealth <= 90):
          print("=========")
        if (yourhealth >= 91) and (yourhealth <= 100):
          print("==========")

        print(str(yourhealth)+"/100")

        print("\nENEMY HP:")

        if (robothealth >= 1) and (robothealth <= 10):
          print("=")
        if (robothealth >= 11) and (robothealth <= 20):
          print("==")
        if (robothealth >= 21) and (robothealth <= 30):
          print("===")
        if (robothealth >= 31) and (robothealth <= 40):
          print("====")
        if (robothealth >= 41) and (robothealth <= 50):
          print("=====")
        if (robothealth >= 51) and (robothealth <= 60):
          print("======")
        if (robothealth >= 61) and (robothealth <= 70):
          print("=======")
        if (robothealth >= 71) and (robothealth <= 80):
          print("========")
        if (robothealth >= 81) and (robothealth <= 90):
          print("=========")
        if (robothealth >= 91) and (robothealth <= 100):
          print("==========")



        print(str(robothealth)+"/100")
   

        print("\n(1) Blaze Strike -Deals moderate damage. (7-11)")
        print("(2) Spitting Fire -Deals high or low damage, depending on chance. (4-15)")
        print("(3) Inner Focus -Heals a moderate amount of HP. (6-10)")

        print("\n(4) Quit Game")
        

        moves=['1','2','3','4']

        attack = input("\n=> ")

        name = "Player 1"

        notin = 0

        if attack == "4":
          time.sleep(0.75)
          clear()
          print("Are you sure you want to leave the game?\n\n(1) YES\n(2) NO")
          leave=input("\n=> ")
          if leave == "1":
            gameinprogress -=1
            notin = 1
            time.sleep(0.75)
            clear()
            print("It's a draw! Nobody wins!")
            time.sleep(3.5)
            clear()
            
          if leave == "2":
            notin = 1
            time.sleep(0)
            continue

        if attack == "1":
          
          damage=random.randint(7, 11)
          robothealth-=damage
          time.sleep(0.75)
          clear()
          print("The computer takes -"+str(damage)+" from "+str(name)+"'s Blaze Strike! The computer now has "+str(robothealth)+" HP remaining.")
          time.sleep(3.5)
          clear()
      

        if attack == "2":
          
          damage=random.randint(4, 15)
          robothealth-=damage
          time.sleep(0.75)
          clear()
          print("The computer takes -"+str(damage)+" from "+str(name)+"'s Spitting Fire! The computer now has "+str(robothealth)+" HP remaining.")
          time.sleep(3.5)
          clear()

        if attack == "3":
          
          heal=random.randint(6, 10)
          yourhealth+=heal
          if yourhealth >= 101:
            yourhealth = 100
            time.sleep(0.75)
            clear()
            print("You healed yourself even though you already had 100 HP. Your HP has stayed consistent.")
            time.sleep(3.5)
            clear()
          time.sleep(0.75)
          clear()
          print(str(name)+" used Inner Focus! It healed +"+str(heal)+" HP. "+str(name)+" now has "+str(yourhealth)+" HP.")
      
          time.sleep(3.5)
          clear()

          

        if attack not in moves:

          notin = 1
          time.sleep(0.75)
          clear()
          print("That was not a valid move. Please select the digits 1, 2, 3, or 4 next time while performing an attack.")
          time.sleep(3.5)
          
          clear()

        if notin == 1:
          time.sleep(0)
          
        if notin == 0:
          go1=1
          if go1 == 1:
            
            if robothealth >= 91 and robothealth <= 100:
              choice=random.randint(1, 10)
              if choice == 1:
                heal=random.randint(6, 10)
                robothealth+=heal
                if robothealth > 100:
                  robothealth = 100
                time.sleep(0.75)
                print("The Computer used Inner Focus! It healed +"+str(heal)+" HP. The computer now has "+str(robothealth)+" HP.")
          
                time.sleep(3.5)
                clear()

              if choice >= 2 and choice <= 6:
                damage=random.randint(7, 11)
                yourhealth-=damage
                time.sleep(0.75)
                print(str(name)+" takes -"+str(damage)+" from the Computer's Blaze Strike! "+str(name)+" now has "+str(yourhealth)+" HP remaining.")
                time.sleep(3.5)
                clear()
        
              if choice >= 7 and choice <= 10:
                damage=random.randint(4, 15)
                yourhealth-=damage
                time.sleep(0.75)
                print(str(name)+" takes -"+str(damage)+" from the Computer's Spitting Fire! "+str(name)+" now has "+str(yourhealth)+" HP remaining.")
                time.sleep(3.5)
                clear()
            if robothealth >= 81 and robothealth <= 90:
              choice=random.randint(1, 10)
              if choice >= 9 and choice <= 10:
                heal=random.randint(6, 10)
                robothealth+=heal
                if robothealth > 100:
                  robothealth = 100
                time.sleep(0.75)
                print("The Computer used Inner Focus! It healed +"+str(heal)+" HP. The computer now has "+str(robothealth)+" HP.")
          
                time.sleep(3.5)
                clear()

              if choice >= 3 and choice <= 8:
                damage=random.randint(7, 11)
                yourhealth-=damage
                time.sleep(0.75)
                print(str(name)+" takes -"+str(damage)+" from the Computer's Blaze Strike! "+str(name)+" now has "+str(yourhealth)+" HP remaining.")
                time.sleep(3.5)
                clear()
        
              if choice >= 1 and choice <= 2:
                damage=random.randint(4, 15)
                yourhealth-=damage
                time.sleep(0.75)
                print(str(name)+" takes -"+str(damage)+" from the Computer's Spitting Fire! "+str(name)+" now has "+str(yourhealth)+" HP remaining.")
                time.sleep(3.5)
                clear()
            if robothealth >= 71 and robothealth <= 80:
              choice=random.randint(1, 10)
              if choice >= 9 and choice <= 10:
                heal=random.randint(6, 10)
                robothealth+=heal
                if robothealth > 100:
                  robothealth = 100
                time.sleep(0.75)
                print("The Computer used Inner Focus! It healed +"+str(heal)+" HP. The computer now has "+str(robothealth)+" HP.")
          
                time.sleep(3.5)
                clear()

              if choice >= 4 and choice <= 8:
                damage=random.randint(7, 11)
                yourhealth-=damage
                time.sleep(0.75)
                print(str(name)+" takes -"+str(damage)+" from the Computer's Blaze Strike! "+str(name)+" now has "+str(yourhealth)+" HP remaining.")
                time.sleep(3.5)
                clear()
        
              if choice >= 1 and choice <= 3:
                damage=random.randint(4, 15)
                yourhealth-=damage
                time.sleep(0.75)
                print(str(name)+" takes -"+str(damage)+" from the Computer's Spitting Fire! "+str(name)+" now has "+str(yourhealth)+" HP remaining.")
                time.sleep(3.5)
                clear()
            if robothealth >= 61 and robothealth <= 70:
              choice=random.randint(1, 20)
              if choice >= 17 and choice <= 20:
                heal=random.randint(6, 10)
                robothealth+=heal
                if robothealth > 100:
                  robothealth = 100
                time.sleep(0.75)
                print("The Computer used Inner Focus! It healed +"+str(heal)+" HP. The computer now has "+str(robothealth)+" HP.")
          
                time.sleep(3.5)
                clear()

              if choice >= 5 and choice <= 16:
                damage=random.randint(7, 11)
                yourhealth-=damage
                time.sleep(0.75)
                print(str(name)+" takes -"+str(damage)+" from the Computer's Blaze Strike! "+str(name)+" now has "+str(yourhealth)+" HP remaining.")
                time.sleep(3.5)
                clear()
        
              if choice >= 1 and choice <= 4:
                damage=random.randint(4, 15)
                yourhealth-=damage
                time.sleep(0.75)
                print(str(name)+" takes -"+str(damage)+" from the Computer's Spitting Fire! "+str(name)+" now has "+str(yourhealth)+" HP remaining.")
                time.sleep(3.5)
                clear()
            if robothealth >= 51 and robothealth <= 60:
              choice=random.randint(1, 20)
              if choice >= 15 and choice <= 20:
                heal=random.randint(6, 10)
                robothealth+=heal
                if robothealth > 100:
                  robothealth = 100
                time.sleep(0.75)
                print("The Computer used Inner Focus! It healed +"+str(heal)+" HP. The computer now has "+str(robothealth)+" HP.")
          
                time.sleep(3.5)
                clear()

              if choice >= 3 and choice <= 14:
                damage=random.randint(7, 11)
                yourhealth-=damage
                time.sleep(0.75)
                print(str(name)+" takes -"+str(damage)+" from the Computer's Blaze Strike! "+str(name)+" now has "+str(yourhealth)+" HP remaining.")
                time.sleep(3.5)
                clear()
        
              if choice >= 1 and choice <= 2:
                damage=random.randint(4, 15)
                yourhealth-=damage
                time.sleep(0.75)
                print(str(name)+" takes -"+str(damage)+" from the Computer's Spitting Fire! "+str(name)+" now has "+str(yourhealth)+" HP remaining.")
                time.sleep(3.5)
                clear()
            if robothealth >= 41 and robothealth <= 50:
              choice=random.randint(1, 20)
              if choice >= 18 and choice <= 20:
                heal=random.randint(6, 10)
                robothealth+=heal
                if robothealth > 100:
                  robothealth = 100
                time.sleep(0.75)
                print("The Computer used Inner Focus! It healed +"+str(heal)+" HP. The computer now has "+str(robothealth)+" HP.")
          
                time.sleep(3.5)
                clear()

              if choice >= 7 and choice <= 17:
                damage=random.randint(7, 11)
                yourhealth-=damage
                time.sleep(0.75)
                print(str(name)+" takes -"+str(damage)+" from the Computer's Blaze Strike! "+str(name)+" now has "+str(yourhealth)+" HP remaining.")
                time.sleep(3.5)
                clear()
        
              if choice >= 1 and choice <= 6:
                damage=random.randint(4, 15)
                yourhealth-=damage
                time.sleep(0.75)
                print(str(name)+" takes -"+str(damage)+" from the Computer's Spitting Fire! "+str(name)+" now has "+str(yourhealth)+" HP remaining.")
                time.sleep(3.5)
                clear()
            if robothealth >= 31 and robothealth <= 40:
              choice=random.randint(1, 30)
              if choice >= 15 and choice <= 30:
                heal=random.randint(6, 10)
                robothealth+=heal
                if robothealth > 100:
                  robothealth = 100
                time.sleep(0.75)
                print("The Computer used Inner Focus! It healed +"+str(heal)+" HP. The computer now has "+str(robothealth)+" HP.")
          
                time.sleep(3.5)
                clear()

              if choice >= 10 and choice <= 14:
                damage=random.randint(7, 11)
                yourhealth-=damage
                time.sleep(0.75)
                print(str(name)+" takes -"+str(damage)+" from the Computer's Blaze Strike! "+str(name)+" now has "+str(yourhealth)+" HP remaining.")
                time.sleep(3.5)
                clear()
        
              if choice >= 1 and choice <= 9:
                damage=random.randint(4, 15)
                yourhealth-=damage
                time.sleep(0.75)
                print(str(name)+" takes -"+str(damage)+" from the Computer's Spitting Fire! "+str(name)+" now has "+str(yourhealth)+" HP remaining.")
                time.sleep(3.5)
                clear()
            if robothealth >= 21 and robothealth <= 30:
              choice=random.randint(1, 30)
              if choice >= 13 and choice <= 30:
                heal=random.randint(6, 10)
                robothealth+=heal
                if robothealth > 100:
                  robothealth = 100
                time.sleep(0.75)
                print("The Computer used Inner Focus! It healed +"+str(heal)+" HP. The computer now has "+str(robothealth)+" HP.")
          
                time.sleep(3.5)
                clear()

              if choice >= 6 and choice <= 12:
                damage=random.randint(7, 11)
                yourhealth-=damage
                time.sleep(0.75)
                print(str(name)+" takes -"+str(damage)+" from the Computer's Blaze Strike! "+str(name)+" now has "+str(yourhealth)+" HP remaining.")
                time.sleep(3.5)
                clear()
        
              if choice >= 1 and choice <= 5:
                damage=random.randint(4, 15)
                yourhealth-=damage
                time.sleep(0.75)
                print(str(name)+" takes -"+str(damage)+" from the Computer's Spitting Fire! "+str(name)+" now has "+str(yourhealth)+" HP remaining.")
                time.sleep(3.5)
                clear()
            if robothealth >= 11 and robothealth <= 20:
              choice=random.randint(1, 40)
              if choice >= 30 and choice <= 40:
                heal=random.randint(6, 10)
                robothealth+=heal
                if robothealth > 100:
                  robothealth = 100
                time.sleep(0.75)
                print("The Computer used Inner Focus! It healed +"+str(heal)+" HP. The computer now has "+str(robothealth)+" HP.")
          
                time.sleep(3.5)
                clear()

              if choice >= 15 and choice <= 29:
                damage=random.randint(7, 11)
                yourhealth-=damage
                time.sleep(0.75)
                print(str(name)+" takes -"+str(damage)+" from the Computer's Blaze Strike! "+str(name)+" now has "+str(yourhealth)+" HP remaining.")
                time.sleep(3.5)
                clear()
        
              if choice >= 1 and choice <= 14:
                damage=random.randint(4, 15)
                yourhealth-=damage
                time.sleep(0.75)
                print(str(name)+" takes -"+str(damage)+" from the Computer's Spitting Fire! "+str(name)+" now has "+str(yourhealth)+" HP remaining.")
                time.sleep(3.5)
                clear()
            if robothealth >= 1 and robothealth <= 10:
              choice=random.randint(1, 50)
              if choice >= 37 and choice <= 50:
                heal=random.randint(6, 10)
                robothealth+=heal
                if robothealth > 100:
                  robothealth = 100
                time.sleep(0.75)
                print("The Computer used Inner Focus! It healed +"+str(heal)+" HP. The computer now has "+str(robothealth)+" HP.")
          
                time.sleep(3.5)
                clear()

              if choice >= 14 and choice <= 36:
                damage=random.randint(7, 11)
                yourhealth-=damage
                time.sleep(0.75)
                print(str(name)+" takes -"+str(damage)+" from the Computer's Blaze Strike! "+str(name)+" now has "+str(yourhealth)+" HP remaining.")
                time.sleep(3.5)
                clear()
        
              if choice >= 1 and choice <= 13:
                damage=random.randint(4, 15)
                yourhealth-=damage
                time.sleep(0.75)
                print(str(name)+" takes -"+str(damage)+" from the Computer's Spitting Fire! "+str(name)+" now has "+str(yourhealth)+" HP remaining.")
                time.sleep(3.5)
                clear()
            
            
        


        if (yourhealth <= 0):
          time.sleep(0.75)
          clear()
          print("You, "+str(name)+", have been defeated by the computer. Better luck next time!")
          time.sleep(3)
          score2+=1
          gameinprogress -= 1
          time.sleep(0)

        if (robothealth <= 0):
          time.sleep(0.75)
          clear()
          print("You, "+str(name)+", have defeated the computer! Way to go!")
          time.sleep(3)
          score1+=1
          gameinprogress -= 1
          time.sleep(0)





  
        





    
      

      
    

  