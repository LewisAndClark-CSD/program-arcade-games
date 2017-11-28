#!/usr/bin/env python3
# main_program chapter 07
# Brady Ballmann
# 11/20/2017


'''First draft of a Program to navigate through a dungeon'''
# Template of the room: [Room desc. , N, E, S, W]
room_list = []


# 0
room = ["You are in an entrance room.",1,None,None,None]

room_list.append(room)
# 1
room = ["You are in the Diner. ",None,2,0,None]

room_list.append(room)

# 3
room = ["You are in the bedroom hallway.",None,3,None,1]

room_list.append(room)
# 4
room = ["You are in the bedroom. ",8,None,None,2]

room_list.append(room)
# 5
room = ["You are in the hallway between the bathroom and the bedroom. ",3,None,7,None]

room_list.append(room)
# 6
room = ["You are in the Bathroom.",None,None,8,6]

room_list.append(room)
# 7
room = ["You are in the hallway between the balcony and the bathroom.",None,7,None,5]

room_list.append(room)
# 8
room = ["You are outside on the balcony. There is a passage way to the  East",None,None,4,None]

room_list.append(room)


current_room = 0



done = False

while done == False:
    print()
    print(room_list[current_room][0])
    user_direction = input("What direction would you like to go? ")
    print()
    if user_direction == "n" or "north":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
    elif user_direction == "e":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way")    
        else:
            current_room = next_room        