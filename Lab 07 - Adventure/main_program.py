#!/usr/bin/env
#Lab 7: Adventure
#Evie Nelson
#11/20/17
''' An adventure game where the user can move through different rooms using north, east, south, and west. '''
#First, sketch the layout of the dungeon
#All of the rooms:
roomZero = ["You are in the main hall. There is a room to the north, to the east, and to the west.", 3, 2, None, 1]
roomOne = ["You are in the ballroom. There is a room to the east.", None, 0, None, None]
roomTwo = ["You are in the study. There is a room to the north and to the west.", 4, None, None, 0]
roomThree = ["You are in the west hall. There is a room to the east, to the south , and to the west.", None, 4, 0, 7]
roomFour = ["You are in the east hall. There is a room to the north, to the east, to the south, and to the west.", 6, 5, 2, 3]
roomFive = ["You are in the weapon room. There is a room to the west.", None, None, None, 4]
roomSix = ["You are in the meeting room. There is a room to the south.", None, None, 4, None]
roomSeven = ["You are in the bedroom. There is a large tapestry to the north and a room to the east.", 8, 3, None, None]
roomEight = ["You are in the secret room. There is a room to the south.", None, None, 7, None]
roomList = [roomZero, roomOne, roomTwo, roomThree, roomFour, roomFive, roomSix, roomSeven, roomEight]
currentRoom= 0
#print(roomList)
currentRoom= 0
done = False
while done != True:
  print()
  print(roomList[currentRoom][0])
  userInput = input("What direction? ")
#directions
  if userInput.lower()[0] == "n":
    nextRoom = roomList[currentRoom][1] 
  elif userInput.lower()[0] == "e":
    nextRoom = roomList[currentRoom][2]  
  elif userInput.lower()[0] == "s":
    nextRoom = roomList[currentRoom][3]
  elif userInput.lower()[0] == "w":
    nextRoom = roomList[currentRoom][4]
  elif userInput.lower()[0] == "q":
    break
#if there isn't a room
  if nextRoom == None:
    print()
    print("You can't go that way.")
  else:
    currentRoom = nextRoom
