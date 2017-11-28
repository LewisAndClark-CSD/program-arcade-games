#Create an empty array called room_list
room_list = []

#Create a variable called room with an array of five elements.
room = ["North hall pictures of angels fighting demons line the walls.", None, 4, 5, 1]

#Append the room to the room list
room_list.append(room)
room = ["Kitchen", None, 0, 2, None]
room_list.append(room)
room = ["Dining room", 1, 3, None, None]
room_list.append(room)
room = ["South hall", 0, 5, 6, 2]
room_list.append(room)
room = ["This is our Bedroom 1.", None, None, 5, 0]
room_list.append(room)
room = ["This is the Bedroom 2.", 4, None, None, 3]
room_list.append(room)
room = ["This is the Balcony.", 3, None, None, None]

#Make new variable called current_room set it to zero.
current_room = 0

#print the room_list variable run the program to test it.
#print(room_list)

#Use the current_room and room_list to print which room the user is in.
print("You are in", room_list [current_room][0])
#Since your first room is zero, the output should be the same as before.
