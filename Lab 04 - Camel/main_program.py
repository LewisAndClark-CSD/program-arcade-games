#!/usr/bin/env python3
# Camel Game
# Evan Witterholt
# 11/11/17


import random

miles = 0
hunger = 0
cowboys = -20
thirst = 0
horsetiredness = 0

print('Welcome to Stealy Horsey!')
print('You have stolen the Krabby Patty Secret Formula and kidnapped a horse to make your way across the Wild West.')
print('The cowboys want their horse back and are chasing you down! Survive your')
print('western trek and outrun the cowboys.')
   

done = False
while done == False:


   townlocation = random.randint(1,21)
   cowboyslocation = random.randint(7,15)
   milesgone = random.randint(10,21)
   milesbehind = miles - cowboys



   print('A. Drink from canteen.')
   print('B. Continue at moderate speed.')
   print('C. Continue at full speed.')
   print('D. Stop for the night.')
   print('E. Status check.')
   print('Q. Quit.')

   userchoice = input('Your choice: ')

   if userchoice.upper() == 'Q':
    done = True

   elif userchoice.upper() == 'E':
      print('\nMiles traveled:' , str(miles),'\nHunger:' ,str(hunger), '\nThirst:' ,(thirst), '\nHorse Tiredness:',str(horsetiredness),'\nMiles Cowboys have traveled:',str(cowboys),'miles.\n')
    
   elif userchoice.upper() == 'D':
      print('\nYou found more food and water.\n''The horse is well rested.' + '\nCowboys are',str(milesbehind), 'miles behind.\n')
      cowboys += cowboyslocation
      horsetiredness -= horsetiredness
      hunger -= hunger
      thirst -= thirst
      

      

   elif userchoice.upper() == 'C':
      miles = miles + random.randint(15, 23)
      print('\nYou traveled:',str(milesgone), 'miles\n', '\nCowboys are',str(milesbehind), 'miles behind.\n' )
      hunger += 1
      cowboys += cowboyslocation 
      horsetiredness += 4

   elif userchoice.upper() == 'B':
      miles = miles + random.randint(5,13)
      print('\nYou traveled:', str(milesgone), 'miles\n','Cowboys have traveled', str(cowboyslocation),'miles.\n')
      hunger += 1
      cowboys += cowboyslocation
      horsetiredness += 2

   elif userchoice.upper() == 'A':
      thirst -=3
      cowboys += cowboyslocation
      print('You stopped to drink water.\nThe Cowboys traveled', str(cowboyslocation), 'miles.\n')

   if horsetiredness < 9 and horsetiredness > 6:
      print('The horse needs rest now.\n')

   elif horsetiredness > 10:
      print('The horse died.')
      done = True

   elif miles <= cowboys:
      print('You have been killed.')
      done = True

   elif miles >= 200:
      print('You escaped!')
      done = True

   elif hunger <= -5:
      print('You starved to death.')
      done = True

   elif thirst <= -5:
      print('You died of dehydration.')
      doen = True
