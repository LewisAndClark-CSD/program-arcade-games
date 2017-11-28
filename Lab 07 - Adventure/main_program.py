#!usr/bin/env python3
# Chapter 7 Lab
# Jessica Lyles
# 11/28/2017

room_list = []
room = ["You are standing in the entrance of the Mystery House.", None, None, 2, None]
room_list.append(room)

room = ["You are standing in the Mystery Children's Room.", None, 2, 4, None]
room_list.append(room)

room = ["You are standing in the hallway of the Mystery house.", 0, 3, 5, 1]
room_list.append(room)

room = ["You are standing in the Mystery Bathroom.", None, None, None, 2]
room_list.append(room)

room = ["You are standing in the Mystery Children's Closet.", 1, None, None, None]
room_list.append(room)

room = ["You are standing in the Mystery Parent's Room.", 2, None, 6, None]
room_list.append(room)

room = ["You are in the Mystery Parent's Bathroom.", 5, None, None, None]
room_list.append(room)

current_room = 0


done = False

while done == False:
    print("")
    print(room_list[current_room][0])
    
    print('Options: North, South, East, or West.')
    user_choice = input("Where would you like to go? ")
    
    if user_choice == "North":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room = next_room
            
    elif user_choice == "East":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room = next_room
            
    elif user_choice == "South":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room = next_room
            
    elif user_choice == "West" :
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way.")
        else:
            current_room = next_room
            
    else:
        print("Program does not understand your choice, please reenter it below.")
        
    
    
            
    
        
