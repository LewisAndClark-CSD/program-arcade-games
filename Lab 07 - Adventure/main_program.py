#!/usr/bin/env python3
#Adventure Game
#Ryan Rosvall
#11/28/17

''' first draft of a text adventure game '''

#room template: [description, N, E, S, W]


current_room = 0
next_room = 0

done = False

room_list = []
room = ['You are in the Main Room. ', 1, 5, 3, 2]
room_list.append(room)
room = ['You are in the Window Room, overlooking the extravagant garden. ', None, None, 0, 2]
room_list.append(room)
room = ['You are in the Bedroom.', 1, 0, None, None]
room_list.append(room)
room = ['You are in the storage room, filled with surgical supplies.', 0, 5, 4, None]
room_list.append(room)
room = ['You have found the hidden storage room! Nothing is here...', 3, None, None, None]
room_list.append(room)
room = ['You are in the lab, there is a dead man strapped to the table.', 6, None, 3, 0]
room_list.append(room)
room = ['You have found an empty room... bummer. Go back to see the dead man now.', None, None, 5, None]
room_list.append(room)

while done == False:

    print(room_list[current_room][0])
    print()
    if room_list[current_room][1] != None:
        print("\tThere is an exit to the North.")
    if room_list[current_room][2] != None:
        print("\tThere is an exit to the East.")
    if room_list[current_room][3] != None:
        print("\tThere is an exit to the South.")
    if room_list[current_room][4] != None:
        print("\tThere is an exit to the West.")
    next_move = input("Which way would you like to go? ")
    if next_move.lower()[0] == "n":
        next_room = (room_list[current_room][1])
    elif next_move.lower()[0] == "e":
        next_room = (room_list[current_room][2])
    elif next_move.lower()[0] == "s":
        next_room = (room_list[current_room][3])
    elif next_move.lower()[0] == "w":
        next_room = (room_list[current_room][4])
    elif next_move.lower()[0] == "q":
        break

    if next_room == None:
        print("You can't go that way.")
        print()
    else:
        current_room = next_room



