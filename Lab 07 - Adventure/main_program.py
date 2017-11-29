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
room = ['You are in the Bedroom.', 1, 0, 7, None]
room_list.append(room)
room = ['You are in the storage room, filled with surgical supplies.', 0, 5, 4, None]
room_list.append(room)
room = ['You have found the hidden storage room! Nothing is here...', 3, None, None, None]
room_list.append(room)
room = ['You are in the lab, there is a dead man strapped to the table.', 6, None, 3, 0]
room_list.append(room)
room = ['You have found an empty room... bummer. Go back to see the dead man now.', None, None, 5, None]
room_list.append(room)
room = ['You Escaped the mansion! Great job!']
room_list.append(room)

while done == False:
    print(room_list[current_room][0])
    print()
    nextMove = input("Which way would you like to go? ")
    if nextMove.lower()[0] == "n":
        next_room = (room_list[current_room][1])
        current_room = next_room
    elif nextMove.lower()[0] == "e":
        next_room = (room_list[current_room][2])
        current_room = next_room
    elif nextMove.lower()[0] == "s":
        next_room = (room_list[current_room][3])
        current_room = next_room
    elif nextMove.lower()[0] == "w":
        next_room = (room_list[current_room][4])
        current_room = next_room
    elif nextMove.lower()[0] == "q":
        break
    if room_list[current_room][1] != None:
        print("\tThere is an exit to the North.")
    if room_list[current_room][2] != None:
        print("\tThere is an exit to the East.")
    if room_list[current_room][3] != None:
        print("\tThere is an exit to the South.")
    if room_list[current_room][4] != None:
        print("\tThere is an exit to the West.")

    if next_room == None:
        print("You can't go that way.")
        print()
    else:
        current_room = next_room
        continue
