#!/usr/bin/env python3
#Lab 6 Maze Game
#Christian Groves
#11/20/17

'''Maze adventure'''

roomList = []
#CMN
room = ['You are in Computer Maintinance Networking.', 3, None, None, None]
roomList.append(room)
#CSD
room = ['You are in Computer Software Development.', 4, None, None, None]
roomList.append(room)
#HALL0
room = ['You are in the West Hallway.', 5, 3, None, None]
roomList.append(room)
#HALL1
room = ['You are in the Central Hallway.', 6, 4, 0, 2]
roomList.append(room)
#HALL2
room = ['You are in the East Hallway.', 7, None, 1, 3]
roomList.append(room)
#BATHROOM
room = ['You are in the Bathroom.', None, None, 2, None]
roomList.append(room)
#WELDING
room = ['You are in Welding.', None, None, 3, None]
roomList.append(room)
#AUTO
room = ['You are in Auto Collision.', None, None, 4,  None]
roomList.append(room)

nextRoom = 0
currentRoom = 0

done = False
while done == False:
    posibleRooms = []
    print()
    print(roomList[currentRoom][0])
    if (roomList[currentRoom][1]) != None:
        posibleRooms.append('North ') 
    if (roomList[currentRoom][2]) != None:
        posibleRooms.append('East ')
    if (roomList[currentRoom][3]) != None:
        posibleRooms.append('South ')
    if (roomList[currentRoom][4]) != None:
        posibleRooms.append('West ')
               
    print('You can go ',end = '')
    for i in range(len(posibleRooms)):
        print(str(posibleRooms[i]),end= ' ')
    dirChoice = input('\nWhat direction do you want to go? ')
   
   #dirChoice direction
    if dirChoice.upper()[0] == 'N':
        dirChoice = 0
    elif dirChoice.upper()[0] == 'S':
        dirChoice = 1
    elif dirChoice.upper()[0] == 'W':
        dirChoice = 2
    elif dirChoice.upper()[0] == 'E':
        dirChoice = 3
    elif dirChoice == 'cry':
        print("\nCrying won't do anything for you! ")
        continue
    elif dirChoice.upper()[0] == 'Q':
        break
        
    #North    
    if dirChoice == 0:
        if (roomList[currentRoom][1]) == None:
            print("\nYou can't go that way! ")
            continue
        else:
            currentRoom = (roomList[currentRoom][1])
            
    #South
    if dirChoice == 1:
        if (roomList[currentRoom][3]) == None:
            print("\nYou can't go that way! ")
            continue
        else:
            currentRoom = (roomList[currentRoom][3])
            
    #West
    if dirChoice == 2:
        if (roomList[currentRoom][4]) == None:
            print("\nYou can't go that way! ")
            continue                
        else:
            currentRoom = (roomList[currentRoom][4]) 
            
    #East
    if dirChoice == 3:
        if (roomList[currentRoom][2]) == None:
            print("\nYou can't go that way! ")
            continue
        else:
            currentRoom = (roomList[currentRoom][2])    