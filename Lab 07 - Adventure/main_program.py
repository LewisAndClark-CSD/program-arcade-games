#!/usr/bin/env python3
#main_program.py
#Steven Thompson
#November 17th 2017

""" Adventure game """

room_list = []

done = False

current_room = 0

room = ["You're standing on the great lawn of a gigantic castle", 1, None, None, 2]
room_list.append(room)
room = ["You're in the castle's shed. There are many tools to keep the lawn tidy", None, 0, None, None]
room_list.append(room)
room = ["You're standing in the great entrance hall to the castle.\nThere are numerous guards and the room is decorated with a gigantic chandelier on the celing", 4, 3, 0, None]
room_list.append(room)
room = ["Dining Room", 5, None, None, 1]
room_list.append(room)
room = ["Center Hallway", None, 5, 1, None]
room_list.append(room)
room = ["East Hallway", 6, None, 3, 4]
room_list.append(room)
room = ["Bed Room", None, None, 5, None]

print(room_list[current_room][0])
