#!/usr/bin/env python3
#Lab 6
#Christian Groves
#11/20/17
roomList = []
#CMN
room = ['You are in Computer Maintinance Networking. \nCentral hallway to the North.', 3, None, None, None]
roomList.append(room)
#CSD
room = ['You are in Computer Software Development. \nEast hallway to the North.', 4, None, None, None]
roomList.append(room)
#HALL0
room = ['You are in the West Hallway. \nBathroom is to the North. Central hallway is to the East.', 5, 3, None, None]
roomList.append(room)
#HALL1
room = ['You are in the Central Hallway. \nWelding is to the North. East hallway is to the East. \nCMN is to the South. West hallway is to the West.', 6, 4, 0, 2]
roomList.append(room)
#HALL2
room = ['You are in the East Hallway. \nAuto Collision is to the North. CSD is to the South. \nCentral hallway is to the West.', 7, None, 1, 3]
roomList.append(room)
#BATHROOM
room = ['You are in the Bathroom. \nWest hallway is to the south.', None, None, 2, None]
roomList.append(room)
#WELDING
room = ['You are in Welding. \nCentral hallway is to the south.', None, None,6, None]
roomList.append(room)
#AUTO
room = ['You are in Auto Collision. \nEast hallway is to the south.', None, None, 4,  None]
roomList.append(room)

nextRoom = 0
currentRoom = 0
done = False
while done == False:
    print()
    print(roomList[currentRoom][0])
    dirChoice = input('What direction do you want to go? ')
    if dirChoice == 'North':
        if [currentRoom][1] == 2:
            nextRoom = roomList[currentRoom][1]
        elif [currentRoom][1] == None:
            print("You can't go that way. ")
        else:
            currentRoom = nextRoom
            
    