#!/usr/bin/env python3
#main_program.py
#Justin Riebow
#11/20/2017

"""A text based adventure game"""

#Create a list of room descriptions and hooked rooms
room_list=[]
room = ["You are in front of the house.", None, None, 1, None]
room_list.append(room)
room = ["You are in the lobby.", 0, 6, 3, 2]
room_list.append(room)
room = ["You are in a narrow hallway.", None, 1, 4, None]
room_list.append(room)
room = ["You are in a large hallway", 1, 7, None, 4]
room_list.append(room)
room = ["You are in the kitchen.", 2, 3, 5, None]
room_list.append(room)
room = ["You are in the dining room.", 4, None, None, None]
room_list.append(room)
room = ["You are in the garage.", None, None, None, 1]
room_list.append(room)
room = ["You are outside.", None, None, 8, 3]
room_list.append(room)
room = ["You are in the shed.", 7, None, None, None]
room_list.append(room)

#Set variable for current room
current_room = 0
done = False

#Keeps the game running
while not done:
    print()
    print(room_list[current_room][0])
    #print exits
    if room_list[current_room][1] != None:
        print("\tThere is an exit to the North.")
    if room_list[current_room][2] != None:
        print("\tThere is an exit to the East.")
    if room_list[current_room][3] != None:
        print("\tThere is an exit to the South.")
    if room_list[current_room][4] != None:
        print("\tThere is an exit to the West.")
    print("What will you do?")
    user_input = input(" ").lower()
    
    #Make north direction
    if user_input == "go north" or user_input == "n":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way.")
        else: 
            current_room = next_room
    
    #Make east direction
    elif user_input == "go east" or user_input == "e":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way.")
        else: 
            current_room = next_room
    
    #Make south direction
    elif user_input == "go south" or user_input == "s":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way.")
        else: 
            current_room = next_room
    
    #Make west direction
    elif user_input == "go west" or user_input == "w":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way.")
        else: 
            current_room = next_room
    #quits the game
    elif user_input == "quit" or user_input == "q":
        done = True
    #When the input is invalid
    else:
        print("Invalid Entry")
    



