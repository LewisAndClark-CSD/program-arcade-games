#!/usr/bin/env python3
#main_program.py
#Justin Riebow
#11/20/2017

"""A text based adventure game"""

room_list=[]
room = ["You are in front of the house. The door is open.", None, None, 1, None]
room_list.append(room)
room = ["You are in the lobby. There are four passages including the door you came in", 1, 6, 3, 2]
room_list.append(room)
room = ["You are in a narrow hallway. There seems to be a light coming from the end of the passage", None, 1, 4, None]
room_list.append(room)
room = ["You are in a hall. The lobby is to the North. There's a light coming from the West. There is a door leading outside to the East.", 1, 7, None, 4]
room_list.append(room)
room = ["This seems to be the kitchen. It reeks of rotten meat. There are two halls to the North and East. There is a door to the South.", 2, 3, 5, None]
room_list.append(room)
room = ["There is a candle-lit table with golden silverware and plates. The kitchen is to the North.", 4, None, None, None]
room_list.append(room)
room = ["This is the garage. There is a car and tools in here. The lobby is to the West", None, None, None, 1]
room_list.append(room)
room = ["You are outside. You see a shed to the South. There is a doorway leading inside to the West.", None, None, 8, 3]
room_list.append(room)
room = ["The room is very dark and tight. The door is to the North.", 7, None, None, None]

current_room = 0
done = False

while done == False:
    print (" " + room_list[current_room][0])

