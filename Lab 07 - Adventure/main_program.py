#!/usr/bin/env python3
#Chapter 7 Lab
#Bethany DuMontelle
#November 20 2017

"""Just a program that lets you go into a variety of rooms"""

#creates the room list
room_list = []

#establishes all the room descriptions and the direction numbers
#note: the number direction order is: north, east, south, west
#the layout is in my notebook on page 37
bedroom = ['You\'re in the bedroom. There\'s nothing of interest in here. \
You can either go \nnorth into the party room or in the \
dining room east.', 4, 1, None, None]

dinning_room = ['This is the dinning room. There\'s a table in here neatly \
set up. You can go to the bedroom\nwest, the kitchen north, \
and the basement east.', 5, 2, None, 0]

basement = ['You are in the basement. It is very spooky down here.\
You can\'t see anything. You can\nonly go back west \
to the dining room.', None, None, None, 1]

balcony = ['You\'re on the balcony. It\'s little chilly out today. You \
can only go back\ninto the party room east.', None, 4, None, None]

party_room = ['It\'s the party room! There is a disco ball on the ceiling and \
a dance floor. Other than\nthat, nothing else is here. You can go west to the \
balcony, north to the\nattic, east to the kitchen, and south to the \
bedroom.', 6, 5, 0, 3]

kitchen = ['This is the kitchen. The wall is covered in knives. Seems safe e\
nough.\nYou can go west to the party room or south to the dining r\
oom.', None, None, 1, 4]

attic = ['You\'re in the attic. Wow! Look at all the dust. You could make a \
small garden with all the\ndust in here. You may want to leave before the dus\
t is a mild inconvenience.\nYou can only go south, back to the p\
arty room.', None, None, 4, None]

#appends it all to the room_list
room_list.append(bedroom)
room_list.append(dinning_room)
room_list.append(basement)
room_list.append(balcony)
room_list.append(party_room)
room_list.append(kitchen)
room_list.append(attic)

#whatever room you are in
current_room = 0

#sets up the loop
done = False

#starts the game loop
while done == False:
    print()
    print(room_list[current_room][0])
    direction = str(input('Where would you like to go now? '))
    
    #all the directions possible to go, the else statement stops impossible
    #movement for each direction
    if direction.lower() == 'n' or direction.lower() == 'north':
        if room_list[current_room][1] != None:
            current_room = room_list[current_room][1]
        else:
            print('You can\'t go that way!')
    
    elif direction.lower() == 'e' or direction.lower() == 'east':
        if room_list[current_room][2] != None:
            current_room = room_list[current_room][2]
        else:
            print('You can\'t go that way!')
        
    elif direction.lower() == 's' or direction.lower() == 'south':
        if room_list[current_room][3] != None:
            current_room = room_list[current_room][3]
        else:
            print('You can\'t go that way!')
            
    elif direction.lower() == 'w' or direction.lower() == 'west':
        if room_list[current_room][4] != None:
            current_room = room_list[current_room][4]
        else:
            print('You can\'t go that way!')
            
    #ends the game
    elif direction.lower() == 'quit':
        print('Okay.')
        done = True
        
    #If the statement doesn't equal any of the above words this will print
    else:
        print('I don\'t understand.')