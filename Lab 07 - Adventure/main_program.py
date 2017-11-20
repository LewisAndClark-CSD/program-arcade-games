#!/usr/bin/env python3
# main_program.py
# Ryan Moore
# 11/20/2017

""" runs a map then the game """

room_list = [ ]
room = ["You have just awoken in a jail cell of a ship(can only go North)",0,None,None,None]
room_list.append(room)
room = ["You are in a big hallway",1,None,None,None]
room_list.append(room)
room = [" You are in the hang out area with only a few people(you can go North)",4,None,None,None]
room_list.append(room)
room = ["You are in a hallway and can kinda see what is on the other side(you can go East or West)",None,5,None,3]
room_list.append(room)
room = ["You are in the guard's room but the people are asleep",None,None,None,2]
room_list.append(room)
room = ["You are in a hallway and smell something getting stronger(can go East)",None,5,None,None]
room_list.append(room)
room = ["You see something on the stove but you don't want to make any noise",None,6,None,None]
room_list.append(room)

current_room = 0
done = False 
while not done:
    print()
    print(room_list[current_room][0])
    usr_direction = input("What way do you want to go? " )
    if usr_direction == "north": 
        print('hi')