#!/usr/bin/env python3
#main_program.py
#Steven Thompson
#November 17th 2017

""" Adventure game """
#The list for the rooms
room_list = []
#boolean variable to keep the while loop going
done = False
#keeps track of your current room
current_room = 0
#This appends the room to a list that contains all the rooms
room = ["You're standing on the great lawn of a gigantic castle.\nYou take your eyes off the castle for a second and notice a shed in the west. ", 1, None, None, 2]
room_list.append(room)

room = ["You're standing in the great entrance hall to the castle.\nThere is an alluring smell coming from the dining hall. ", 4, 3, 0, None]
room_list.append(room)

room = ["You're in the castle's shed. There are many tools to keep the lawn tidy", None, 0, None, None]
room_list.append(room)

room = ["The cooks are preparing a delicious meal. You look past the table and see a hallway in front of you.", 5, None, None, 1]
room_list.append(room)

room = ["You're in a long corridor that seems to only lead to another equally long corridor.", None, 5, 1, None]
room_list.append(room)

room = ["You can smell the meal coming from the dining room and see an entrance to a bedroom.", 6, None, 3, 4]
room_list.append(room)

room = ["You have made it all the way to the kings spotless bedroom. It is the most amazing thing you have ever seen", None, None, 5, None]
room_list.append(room)
#Main loop for the program
while done == False:
    print()
    print("Press Q to quit at anytime")
    print()
    print(room_list[current_room][0])
    
    user_input = input("Which direction do you want to explore? ").lower()
    #Controls directions for north
    if user_input == "north" or user_input == "n":
            next_room = room_list[current_room][1]
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = next_room            
    #Controls directions for eat
    elif user_input == "east" or user_input == "e":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room = next_room        
    #Controls directions for south
    elif user_input == "south" or user_input == "s":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room = next_room        
    #Controls directions for west
    elif user_input == "west" or user_input == "w":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room = next_room        
    #Exits the while loop if q is entered
    elif user_input == "q":
        done = True