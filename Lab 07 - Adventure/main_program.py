#!/usr/bin/env python3
#main_program.py
#Ethan Dall
#11-20-17

"""Factory Escape"""

#Created an empty list for room
room_list = []

#Set Closet
room = ['A cramped and cluttered closet. Just north is the door', 1, None, None, None]
room_list.append(room)

#Set West Hall
room = ['Opening up into a long hallway. With a staircase north,\nleading up, and more hall to the east.', 5, 2, 0, None]
room_list.append(room)

#Set Staircase
room = ['A velvet staircase, reaching north to a door.', 6, None, 1, None]
room_list.append(room)

#Set East Hall
room = ['The end of the hall, with doors to the north, east, and south of you.', 4, None, 3, 1]
room_list.append(room)

#Set Garage
room = ['Dark and dusty, the room appears to be a garage with two large doors to the east.', 2, 8, None, None]
room_list.append(room)

#Set Production
room = ['Quite and unmoving machines appear frozen, with wires and arms intricatly placed about the room. A wire fence lays north of you.', 7, None, 2, None]
room_list.append(room)

#Set Power
room = ['A room with one panel, lays open waiting to be used. The exit is south of you.', None, None, 4, None]
room_list.append(room)

#Set Office
room = ['Red Carpet and Cubicals allows a homely feel and a great window overlooking the production area. The exit door is south of you.', None, None, 5, None]
room_list.append(room)

#Set Outside
room = ['Finally the brisk air hits your face and your ready to go home.', None, None, None, 3]
room_list.append(room)

#Room Currently in
current_room = 0

#Condition
done = False

#Checks for direction
while not done:
    
    #Seperator / blank line
    print()
    
    #Room Description
    print(room_list[current_room][0])
    
    #Player direction
    direction = input('Where would you like to go? ')
    
    #Check input
    if direction == 'north':
        next_room = room_list[current_room][1]
     
    if next_room == None:
        print('You can\'t go that way')
    else:
        current_room = next_room