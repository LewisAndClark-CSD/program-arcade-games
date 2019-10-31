#!/usr/bin/env
# main_program.py
# jacob poncher
# 11/20/17

''' first draft of a text adventure game '''

room_list = []
room = [ "you are in the entrance.there is a passage south  to the rest of the house ",None, None, 3, None]
room_list.append(room)
room = ["you are in the office, go west to the front hall ",None,None,None,10]
room_list.append(room)
room = [ "  you are in the kitchen,go east to the front hall ", None,3 ,None,None]
room_list.append(room)
room = [ "  you are in the west front hall,kitchen is to the west,living room is south ,and office is to the east,entrance is north", 0 ,10, 4, 2]
room_list.append(room)
room = [ " You are in the living room,go north to the front hall ",3 ,None ,None ,None]
room_list.append(room)
room = ["you are in the bedroom,the back hall is to the east",None,8,None,None]
room_list.append(room)
room = [ " you are in the bedroom, go west to the center hall",None,None,None,9]
room_list.append(room)
room = ["you are in  the bathroom,the back hall is to the west" ,None,None,None,8]
room_list.append(room)
room = [ "you are in the back hall,bedroom is to the west ,center hall is north ,and bathroom is to the east", 9 , 7 ,None,5] 
room_list.append(room)
room = [" you are in the center hall,north is the east front hall ,south is the back hall and the bedroom is  east " , 10, 6, 8, None]
room_list.append(room)
room = [" you are in the east front hall, office is to the east,center hall is south,west front hall is west",None,1,9,3]
room_list.append(room)

current_room = 0 
done = False 
while done == False:
    print(room_list[current_room][0])
    print()
    next_room = current_room
    user_choice = input("what do you want to do: ")
    if user_choice == "south":
        next_room = room_list[current_room][3]
        if next_room == None:
            print('you cant go that way')
        else:
            current_room = next_room
    
    if user_choice == "north":
        next_room = room_list[current_room][1]
        if next_room == None:
            print('you cant go that way')
        else:
            current_room = next_room
    
    if user_choice == "east":
        next_room = room_list[current_room][2]
        if next_room == None:
            print('you cant go that way')
        else:
            current_room = next_room    
            
    if user_choice == "west":
        next_room = room_list[current_room][4]
        if next_room == None:
            print('you cant go that way')
        else:
            current_room = next_room 
            
    if user_choice == "quit":
        done = True 