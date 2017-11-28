#!
# Evie Nelson
# 11/20/17
# First class
#Lab 7: Adventure
#First, sketch the layout of the dungeon
#All of the rooms:
roomZero = ["You are in the main hall. There is a room to the north, to the east, and to the west.", 3, 2, None, 1]
roomOne = ["You are in the ballroom. There is a room to the east.", None, 0, None, None]
roomTwo = ["You are in the study. There is a room to the north and to the west.", 4, None, None, 0]
roomThree = ["You are in the west hall. There is a room to the east, to the south , and to the west.", None, 4, 0, 5]
roomFour = ["You are in the east hall. There is a room to the north, to the east, to the south, and to the west.", 6, 5, 2, 3]
roomFive = ["You are in the weapon room. There is a room to the west.", None, None, None, 4]
roomSix = ["You are in the meeting room. There is a room to the south.", None, None, 4, None]
roomSeven = ["You are in the bedroom. There is a large tapestry to the north and a room to the east."]
roomEight = ["You are in the secret room. There is a room to the south.", None, None, 7, None, 8, 3, None, None]
roomList = [roomZero, roomOne, roomTwo, roomThree, roomFour, roomFive, roomSix, roomSeven, roomEight]
currentRoom= 0
#print(roomList)
currentRoom= 0
done = False
while done != True:
  print()
  print(roomList[currentRoom][0])
  userInput = input("What direction? ")
#north  
  if userInput == "n":
    nextRoom = roomList[currentRoom][1] 
  elif userInput == "e":
    nextroom = roomList[currentRoom][2]  
  elif userInput == "s":
    nextroom = roomList[currentRoom][3]
  elif userInput == "w":
    nextRoom = roomList[currentRoom][4]
  elif userInput == "q":
    break
  
  if nextRoom == None:
    print("You can't go that way.")
  else:
    currentRoom = nextRoom
