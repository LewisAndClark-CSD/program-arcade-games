#Create an empty array called room_list
room_list = []

#Create a variable called room with an array of five elements.
room = ["North hall", None, 4, 5, 1]
#Append the room to the room list
room_list.append(room)
room = ["Kitchen", None, 0, 2, None]
room_list.append(room)
room = ["Dining room", 1, 3, None, None]
room_list.append(room)
room = ["South hall", 0, 5, 6, 2]
room_list.append(room)
room = ["Bedroom 1", None, None, 5, 0]
room_list.append(room)
room = ["Bedroom 2", 4, None, None, 3]
room_list.append(room)
room = ["Balcony", 3, None, None, None]
room_list.append(room)
#First element create a string with description of the first room.
First = "North hall" + " Pictures of angels fighting demons line the walls."

#Repeat the prior two steps for each foom you want to create. 
#Re-use the room variable
#Make new variable called current_room set it to zero.
current_room = 0
#print the room_list variable run the program to test it.
print(room_list[0])