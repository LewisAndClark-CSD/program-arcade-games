#!/usr/bin/env python3
#Chapter 7 Lab
#Bethany DuMontelle
#November 20 2017

#creates the room list
room_list = []

#establishes all the room descriptions and the direction numbers
bedroom = 'There\'s nothing of interest in here. You can either go north into\
the party room or in the dining room east.', 4, 1, None, None

dinning_room = 'There\'s a table in here neatly set up. You can go to the\
 bedroom west, the kitchen north, and the basement east.', 5, 2, None, 0

basement = 'It is very spooky down here. You can\'t see anything.\
You can only go back west to the dining room.', None, None, None, 1

balcony = 'It\'s little chilly out today. You can only go back into the\
party room.', None, 4, None, None

party_room = 'There is a disco ball on the ceiling and a dance floor. \
Other than that, nothing else is here. You can go west to the balcony, \
north to the attic, east to the kitchen, and south to the bedroom.', 6, 5, 0, 3

kitchen = 'The wall is covered in knives. Seems safe enough. You can go \
west to the party room or south to the dining room.', None, None, 1, 4

attic = 'Wow! Look at all the dust. You could make a small garden with \
all the dust in here. You may want to leave before the dust is a mild \
inconvenience. You can only go south back to the\
party room.', None, None, 4, None

#appends it all to the room_list
room_list.append(bedroom)
room_list.append(dinning_room)
room_list.append(basement)
room_list.append(balcony)
room_list.append(party_room)
room_list.append(kitchen)
room_list.append(attic)