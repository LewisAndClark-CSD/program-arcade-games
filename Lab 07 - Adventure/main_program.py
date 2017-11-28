#Lab 7: Adventure
#First, sketch the layout of the dungeon
roomList = [roomZero, roomOne, roomTwo, roomThree, roomFour, roomFive, roomSix, roomSeven, roomEight]
#All of the rooms:
roomZero = ["Main hall", 3, 2, None, 1]
roomOne = ["Ballroom", None, 0, None, None]
roomTwo = ["Study", 4, None, None, 0]
roomThree = ["West Hall", None, 4, 0, 5]
roomFour = ["East Hall", 6, 5, 2, 3]
roomFive = ["Weapon Room", None, None, None, 4]
roomSix = ["Meeting Room", None, None, 4, None]
roomSeven = ["Bedroom", 8, 3, None, None]
roomEight = ["Secret Room", None, None, 7, None]
currentRoom = 0
print(roomList)
