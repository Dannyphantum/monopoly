import random
import re
print('Let''s play Monopoly!')
pieces = 'Top Hat \n Racecar \n Cannon \n Battleship \n Thimble'
print(pieces)

pattern = r'Thimble|Racecar|Cannon|Battleship|Top Hat'
print('Choose your piece!')
chosen_piece = input()
match = re.findall(pattern, chosen_piece)
print('Alright! You have selected the ' + chosen_piece + '!')


#Board Spaces
space_0 = 'GO'
space_1 = 'Mediterranean Avenue'
space_2 = 'Community Chest'
space_3 = 'Baltic Avenue'
space_4 = 'Income tax'
space_5 = 'Reading Railroad'
space_6 = 'Central Avenue'
space_7 = 'Chance'
space_8 = 'Vermont Avenue'
space_9 = 'Connecticut Avenue'
space_10 = 'Just Visiting'
space_11 = 'St.Charles Place'
space_12 = 'Electric Company'
space_13 = 'Statue Avenue'
space_14 = 'Virginia Avenue'
space_15 = 'Pennsylvania Railroad'
space_16 = 'St James Place'
space_17 = 'Community Chest'
space_18 = 'Tennesse Avenue'
space_19 = 'New York Avenue'
space_20 = 'Free Parking'
space_21 = 'Kentucky Avenue'
space_22 = 'Chance'
space_23 = 'Indiana Avenue'
space_24 = 'Illinois Avenue'
space_25 = 'B&O Railroad'
space_26 = 'Atlantic Avenue'
space_27 = 'Ventnor Avenue'
space_28 = 'Water Works'
space_29 = 'Marvin Gardens'
space_30 = 'Go to Jail'
space_31 = 'Pacific Avenue'
space_32 = 'North Carolina Avenue'
space_33 = 'Community Chest'
space_34 = 'Pennsylvania Avenue'
space_35 = 'Short Line'
space_36 = 'Chance'
space_37 = 'Park Place'
space_38 = 'Luxury Tax'
space_39 = 'Boardwalk'

print('The ' + chosen_piece + ' is at ' + space_0 + '.')

print('Will you roll?')
player_roll = input()

roll = str(random.randint(1, 12))

print('You rolled a ' + roll)




