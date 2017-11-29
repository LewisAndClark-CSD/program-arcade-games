#!/usr/bin/env python3
# Lab 7: Adventure
# Conner Walkenhorst
# 11/20/2017

"""Create a text adventure game using python"""

room_list = []
room = ["The Entryway", None, None, 3, None]
room_list.append(room)
room = ["Office Room", None, None, 4, None]
room_list.append(room)
room = ["Ballpit Room", None, None, 5, None]
room_list.append(room)
room = ["West Hall", 0, 4, 6, None]
room_list.append(room)
room = ["Center Hall", 1, 5, 7, 3]
room_list.append(room)
room = ["East Hall", 2, None, 8, 4]
room_list.append(room)
room = ["Weight Room", 3, None, None, None]
room_list.append(room)
room = ["Blade Room", 4, None, None, None]
room_list.append(room)
room = ["Balloon Room", 5, None, None, None]
room_list.append(room)

done = False
current_room = 0

while done == False:
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
    
    user_choice = input("Where would you like to go? ")
    
    if user_choice.lower()[0] == "n":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room = next_room
    
    elif user_choice.lower()[0] == "e":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room = next_room    

    elif user_choice.lower()[0] == "s":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room = next_room
            
    elif user_choice.lower()[0] == "w":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room = next_room
    
    else:
        print("say again?")
