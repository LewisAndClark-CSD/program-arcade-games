#!/usr/bin/env python3
#Adventure.py
#Jason Cobb
#11/28/17

#Create an empty array called room_list
room_list = []

#Create a variable called room with an array of five elements.
room = ["the North hall pictures of angels fighting demons line the walls.", None, 4, 3, 1]

#Append the room to the room list
room_list.append(room)
room = ["the Kitchen that has pots and pans setup for cooking.", None, 0, 2, None]
room_list.append(room)
room = ["the Dining room that has plates and silverwear set out.", 1, 3, None, None]
room_list.append(room)
room = ["the South hall that has many sets of different armor.", 0, 5, 6, 2]
room_list.append(room)
room = ["Bedroom 1 that has a bed, closet, and bathroom.", None, None, 5, 0]
room_list.append(room)
room = ["Bedroom 2 that also has  a bed, closet, and bathroom.", 4, None, None, 3]
room_list.append(room)
room = ["the Balcony that oversees the lake behind the castle.", 3, None, None, None]
room_list.append(room)

#Make new variable called current_room set it to zero.
current_room = 0

#print the room_list variable run the program to test it.
#print(room_list)

#Use the current_room and room_list to print which room the user is in.

#Since your first room is zero, the output should be the same as before.
done = False
while not done:
    print()
    print("You are in", room_list [current_room][0])
    answer = input("What do you want to do?: ")
    if answer.lower()[0] == "n":
        next_room = room_list[current_room][1]
       
    elif answer.lower()[0] == "e":
        next_room = room_list[current_room][2]
        
    elif answer.lower()[0] == "s":
        next_room = room_list[current_room][3]
        
    elif answer.lower()[0] == "w":
        next_room = room_list[current_room][4]
        
    elif answer.lower()[0] == "q":
        break
    
    if next_room == None:
        print("You can't go that way.")
    else:
        current_room = next_room
        
print("Have a nice day.")