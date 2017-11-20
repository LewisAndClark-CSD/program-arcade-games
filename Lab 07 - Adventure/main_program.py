#Chapter 7 Lab

room_list = []
room = ["You are standing in the entrance of the Mystery House. To the south is the rest of the rooms.", None, None, 2, None]
room_list.append(room)
room = ["You are standing in the Mystery Children's Room. To the south and east are the other rooms.", None, 2, 4, None]
room_list.append(room)
room = ["You are standing in the hallway of the Mystery house. There are rooms in all directions.", 0, 3, 5, 1]
room_list.append(room)
room = ["You are standing in the Mystery Bathroom. The rest of the Mystery House is to the west.", None, None, None, 2]
room_list.append(room)
room = ["You are standing in the Mystery Children's Closet. There is a room to the north.", 1, None, None, None]
room_list.append(room)
room = ["You are standing in the Mystery Parent's Room. Two rooms lay to the north and south.", 2, None, 6, None]
room_list.append(room)
room = ["You are in the Mystery Parent's Bathroom. One room is to the north.", 5, None, None, None]
room_list.append(room)
current_room = 0
print('You are in a room. There is a passage to the south.', room_list[0])
done = False
while done == False:
    print("")
    print(room_list[current_room][0])
    print('Options: North, South, East, or West.')
    user_choice = input("Where would you like to go? ")
    
        


    
    
