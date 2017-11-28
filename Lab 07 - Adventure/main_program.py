#!/usr/bin/env python3
# main_program chapter 07
# Brady Ballmann
# 11/20/2017

room_list = []


# 0
room = ["You are in a entrance room. There is a passage to the north",1,None,None,None]

room_list.append(room)
# 1
room = ["You are in the Diner. There is a passage way to the  east, and south",None,2,0,None]

room_list.append(room)

# 3
room = ["You are in the bedroom hallway. There is a passage way to the East and West",None,3,None,1]

room_list.append(room)
# 4
room = ["You are in the bedroom. There is a passage way to the North and West",8,None,None,2]

room_list.append(room)
# 5
room = ["You are in the hallway between the bathroom and the bedroom. There is a passage way to the north and south",3,None,7,None]

room_list.append(room)
# 6
room = ["You are in the Bathroom. There is a passage way to the South and West",None,None,8,6]

room_list.append(room)
# 7
room = ["You are in the hallway between the balcony and the bathroom. There is a passage way to the East and West",None,7,None,5]

room_list.append(room)
# 8
room = ["You are outside on the balcony. There is a passage way to the  East",None,None,4,None]

room_list.append(room)


current_room = 0



done = False

while not done:
    print()
    print(room_list[current_room][0])
    user_direction = input("What direction would you like to go? ")
    print()
    next_room = room_list[current_room][1]
    if user_direction == "n":
        print(next_room)
    
        