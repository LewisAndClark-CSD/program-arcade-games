import random
print('Welcome to Camel!')
print('You have stolen a camel to make your way across the great Mobi desert.')
print('The natives want their camel back and are chasing you down! Survive your')
print('desert trek and outrun the natives.')
done = False
milestraveled = 0
thirst = 0
cameltiredness = 0
natives = -20
canteen = 3

while done == False:
    print('A. Drink from your canteen.')
    print('B. Ahead moderate speed.')
    print('C. Ahead full speed.')
    print('D. Stop for the night.')
    print('E. Status check.')
    print('Q. Quit.')
    userchoice = input('Your choice? ').upper()
    if userchoice == ('Q'):
        done = True
        
    elif userchoice == ('E'):
        print('Miles traveled:',milestraveled)
        print('Drinks in canteen',thirst)
        print('The natives are',natives,'miles behind you')
    elif userchoice == ('D'):
        cameltiredness = 0
        print('Your camel is happy.')
        n1 = random.randint(7,14)
        natives = natives + n1
    elif userchoice == ('C'):
        n2 = random.randint(10,20)
        milestraveled = milestraveled + n2
        print(milestraveled, 'Miles traveled')
        thirst + 1
        n3 = random.randint(1,3)
        cameltiredness = cameltiredness + n3
        n1 = random.randint(7,14)
        natives = natives + n1
    elif userchoice == ('B'):
        n2 = random.randint(5,12)
        milestraveled = milestraveled + n2
        print(milestraveled)
        thirst + 1
        cameltiredness + 1
        n1 = random.randint(7,14)
        natives = natives + n1
    elif userchoice == ('A'):
        if canteen > 0:
            canteen = canteen - 1
        else:
            print('You dont have enough water.')
    if thirst > 6:
        print('You died of thirst!')
        done = True
    elif thirst > 4:
        print('You are thirsty!')
        

    elif cameltiredness > 5:
        print('Your camel is dead :(')
        done = True
    elif cameltiredness >= 8:
        print('Your camel is getting tired.')

    if abs(natives - milestraveled) <= 15:
        print('The natives are getting close!')
    chance = random.randint(1,20)
    if chance == 5:
        canteen = o
        thirst = 0
        cameltiredness = 0
        print('You found an oasis')

    if milestraveled >= 200 and done == False:
        print('You made it across the Mobi Desert!') 
        

        
        
        
    
        
              
