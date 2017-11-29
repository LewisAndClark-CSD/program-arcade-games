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

# 2
room = ["You are in the bedroom hallway.",None,3,None,1]

room_list.append(room)
# 3
room = ["You are in the bedroom. ",4,None,None,2]

room_list.append(room)
# 4
room = ["You are in the hallway between the bathroom and the bedroom. ",5,None,3,None]

room_list.append(room)
# 5
room = ["You are in the Bathroom.",None,None,4,None]

room_list.append(room)


current_room = 0

done = False

while not done:
    print()
    print(room_list[current_room][0])    
    
    if room_list[current_room][1] != None:
        print("There is an exit to the North")
    if room_list[current_room][2] != None:
        print("There is an exit to the East")
    if room_list[current_room][3] != None:
        print("There is an exit to the South")
    if room_list[current_room][4] != None:
        print("There is an exit to the West")
        
    user_direction = input("What direction would you like to go? ")
    print()
    # Printing the exits
    
    
    if user_direction == "n" or user_direction == "north":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room      
            
    
    elif user_direction == "e" or user_direction == "east":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way")    
        else:
            current_room = next_room   
            
    elif user_direction == "s" or user_direction == "south":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way") 
        else:
            current_room = next_room
            
    elif user_direction == "w" or user_direction == "west":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way")    
        else:
            current_room = next_room  
            
    else:
        print("The program does not understand what you typed")
            
            
            
            
    