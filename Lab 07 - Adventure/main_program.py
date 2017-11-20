#!/usr/bin/env python3
#Chapter 7 Lab
#Bethany DuMontelle
#November 20 2017

room_list = [bedroom, dinning_room, basement, balcony, party_room, 
             kitchen, attic]

bedroom = ['As soon as you walk into the bedroom, it becomes apparent\
that you are not alone in this room. The adjacent rooms illuminate\
the one you\'re currently in; no lights exist in here. You can only see a bed\
covered in dark gray rags and an old wooden dresser that would\
fall apart if you happen to move past it. You can either go to the party room\
north or the dinning room east.', 4, 1, None, None]

dinning_room = ['The chadelier hangs from the ceiling above the long dinner \
table. The table itself is neatly organzed: the red table cloth is at equal \
length on all sides, plates correspond to each chair, the spoons, knives, and\
forks are all to the side of each plate, chairs neatly tucked in, and all the \
decor matches the rest of the table It\'s as if you walked in just before the\
food was placed on the table. You can go the kitchen north, the bedroom west,\
or the basement west.', 5, 2, None, 0]

basement = ['As you walk into the basement, you can hear what is most likely \
water dripping, echoing with each drop. Darkness engulfs the room when \
you walk further into it. It smells musty. If you walk any further into the\
basement, you feel like you will never find your way back out You can only\
go west back to the dining room.', None, None, None, 1]

balcony = ['The outdoors are far brighter than inside the house, despite\
it being night. The air is nippy, and all you can see are trees past the\
balcony. You can only go east back to the party room.', None, 4, None, None]

party_room = [' ', 6, 5, 0, 3]

kitchen = [' ', None, None, 1, 4]

attic = [' ', None, None, 4, None]

