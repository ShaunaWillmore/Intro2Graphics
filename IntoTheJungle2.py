#IntoTheJungle2
#Author: Shauna Willmore
#Last Modified By: Shauna Willmore
#Date Last Modified: May.22/ 2013
#Program Description: Basic text adventure game. User explores a jungle and decides where how the story will play out.
#Revision History: 

import time

#intro
print ('You wake up with a terrible headache...,')
print ('Where are you?!')
print ('You stand up slowly, and begin to glace around...')
print ('It appears you have awoken in a very dense jungle.')
print ('There are 2 visible paths, leading opposite directions.')
print

	
#Ask the users which direction to go first, the varible "path" equals the users input
print ('Which direction will you go left or right?')
path = raw_input('> ')
	
#The user has chose to go left	
if  path == 'left':
	print ('You begin to walk down the path...')
	print ('The scenery is beautiful...')
	print ('But something feels not right...')
	print
	time.sleep(1)
	print ('You walk for a bit.')
	print ('Unfortunitly you come to a river running right through the path')
	
#The user has chose to go right	
elif path == 'right':
	print ('You begin to walk down the path...')
	print ('The scenery is beautiful...')
	print ('But something feels not right...')
	print
	time.sleep(1)
	print ('You notice something in the distance')
	print ('BAH! Looks like theres a massive tree fallen right across the path!')
	
#User inputed an invalid choice	
else: 
	print('HEY!...Pick a valid direction!')
		

