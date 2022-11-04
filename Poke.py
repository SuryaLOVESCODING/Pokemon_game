import random
import turtle
import sys

wn=turtle.Screen()
charizard=turtle.Turtle()
blastoise=turtle.Turtle()
raqyuaza=turtle.Turtle()
mewto=turtle.Turtle()
alakazam=turtle.Turtle()
arceus=turtle.Turtle()

pokemon=input("Pick a pokemon:")



# ✅ prefix string with r
file_name = r'C:\Users\NMURUGAP\Downloads\charizard.gif'



    
wn.register_shape(file_name)#Done
wn.register_shape(r"C:\Users\NMURUGAP\Downloads\blastoise3.gif")#Done
wn.register_shape(r"C:\Users\NMURUGAP\Downloads\raqyuaza.gif")
wn.register_shape(r"C:\Users\NMURUGAP\Downloads\mewto.gif")
wn.register_shape(r"C:\Users\NMURUGAP\Downloads\charizard.gif")
wn.register_shape(r"C:\Users\NMURUGAP\Downloads\alakazam.gif")
charizard.penup()
charizard.shape(file_name)
charizard.setpos(400,300)
charizard.pendown()

blastoise.penup()
blastoise.shape(r"C:\Users\NMURUGAP\Downloads\blastoise3.gif")
blastoise.setpos(-100,300)
blastoise.pendown()

raqyuaza.penup()
raqyuaza.shape(r"C:\Users\NMURUGAP\Downloads\raqyuaza.gif")
raqyuaza.setpos(-600,290)
raqyuaza.pendown()


charizardmoves=[
    "Overheat",
    "Air Slash",
    "Fire Spin"
    ]

blastoisemoves=[
    "Hydro Pump",
    "Frustration",
    "Bite"
]
raqyuazamoves=[
    "Outrage",
    "Dragon Tail",
    "AirSlah"
    
]
arceusmoves=[  
    "Hyper Beam",
    "Iron Tail",
    "Shadow Claw"
    ]

mewtomoves=[
   "Earthquake",
   "confusion",
   "Pyscho Cut"
   ]

alakazammoves=[
   "Counter",
   "Focus Blast",
   "Frustration"
   ]
random=random.randint(1,3)

if random==1:
   import random
   arceus.penup()
   arceus.shape("arceus.gif")
   arceus.setpos(400,-300)
   arceus.pendown()
  
   randomarceus=random.choice(arceusmoves)
   pokenemy="Arceus"

if random==2:
   import random
   mewto.penup()
   mewto.shape("mewto.gif")
   mewto.setpos(400,-300)
   mewto.pendown()
   randommewto=random.choice(mewtomoves)
   pokenemy="Mewtwo"
   


if random==3:
   import random
   alakazam.penup()
   alakazam.shape("alakazam.gif")
   alakazam.setpos(400,-300)
   alakazam.pendown()
   randomalakazam=random.choice(alakazammoves)

   pokenemy="Alakazam"





opphealth=200
playerhealth=200
print(pokemon+" health = "+str(playerhealth))
print("Your opponent is ",pokenemy)
print("Your opponent's health = ",str(opphealth))
if pokemon=="charizard":
      import random
      charizard.penup()
      charizard.setpos(-400,-300)
      charizard.pendown()
      
      charizardmove=input("Pick a move for charizard to use, Overheat, Air Slash or Fire Spin: ")
      
     

      
if charizardmove == charizardmoves[0]:
    charizard.penup()
    charizard.setpos(150,-300)
    charizard.pendown()
    charizard.penup()
    charizard.setpos(-400,-300)
    charizard.pendown()
    opphealth-=160
    print("Your opponent's health is now", opphealth)

elif charizardmove == charizardmoves[1]:
    charizard.penup()
    charizard.setpos(150,-300)
    charizard.pendown()
    charizard.penup()
    charizard.setpos(-400,-300)
    charizard.pendown()
    opphealth-=14
    print("Your opponent's health is now", opphealth)

elif charizardmove == charizardmoves[2]:
    charizard.penup()
    charizard.setpos(150,-300)
    charizard.pendown()
    charizard.penup()
    charizard.setpos(-400,-300)
    charizard.pendown()
    opphealth-=14
    print("Your opponent's health is now", opphealth)
    
   #Blastoise
elif pokemon=="blastoise":
     import random

     blastoise.penup()
     blastoise.setpos(-400,-300)
     blastoise.pendown()
     
     blastoisemove=input("Pick a move for blastoise to use, Hydro Pump, Bite, Water Gun: ")


     
if blastoisemove == blastoisemoves[0]:
   blastoise.penup()
   bastoise.setpos(150,-300)
   blastoise.pendown()
   blastoise.penup()
   blastoise.setpos(150,-300)
   blastoise.pendown()
   opphealth-=130
   print("Your opponent's health is now", opphealth)

elif blastoisemove == blastoisemoves[1]:
   blastoise.penup()
   bastoise.setpos(150,-300)
   blastoise.pendown()
   blastoise.penup()
   blastoise.setpos(150,-300)
   blastoise.pendown()
   opphealth-=10
   print("Your opponent's health is now", opphealth)


elif blastoisemove == blastoisemoves[2]:
   blastoise.penup()
   bastoise.setpos(150,-300)
   blastoise.pendown()
   blastoise.penup()
   blastoise.setpos(150,-300)
   blastoise.pendown()
   opphealth-=6
   print("Your opponent's health is now", opphealth)

 #Raqyuaza
elif pokemon=="raqyuaza":
    import random
 
    raqyuaza.penup()
    raqyuaza.setpos(-400,-300)
    raqyuaza.pendown()
    
    raqyuazamove=input("Pick a move for raqyuaza to use, Hydro Pump, Bite, Water Gun: ")
