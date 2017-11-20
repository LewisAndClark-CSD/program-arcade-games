#Chapter 7 Lab

room_list = []
room = ["You are standing in the entrance of the Mystery House.\nTo the south is the rest of the rooms.", None, None, 2, None]
room_list.append(room)

room = ["You are standing in the Mystery Children's Room.\nTo the south and east are the other rooms.", None, 2, 4, None]
room_list.append(room)

room = ["You are standing in the hallway of the Mystery house.\nThere are rooms in all directions.", 0, 3, 5, 1]
room_list.append(room)

room = ["You are standing in the Mystery Bathroom.\nThe rest of the Mystery House is to the west.", None, None, None, 2]
room_list.append(room)

room = ["You are standing in the Mystery Children's Closet.\nThere is a room to the north.", 1, None, None, None]
room_list.append(room)

room = ["You are standing in the Mystery Parent's Room.\nTwo rooms lay to the north and south.", 2, None, 6, None]
room_list.append(room)

room = ["You are in the Mystery Parent's Bathroom.\nOne room is to the north.", 5, None, None, None]
room_list.append(room)

current_room = 0

print('You are in a room. There is a passage to the south.', room_list[0])

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
        
    
    
            
    
        
