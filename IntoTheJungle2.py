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
	time.sleep(1)
	
	#The user has to chose whether to go around or across the river	
	print ('Do you want to try and go around the river(around), or would you like to swim across(across)?')
	river = raw_input('> ')

	#User chose around	
	if river == 'around':
		print('You walk along side the river for what feels like hours...')
		print('Suddenly you hear what sounds like growling in the distance!')
		print('You stop walking and begin to scan your surroundings')
		print('Maybe you are just hearing things?!')
		time.sleep(1)
		
		#The user has to chose whether to swim across the river or continue walking around
		print('Do you want to swim across the river now (swim) or try your luck and continue walking (continue)?')
		swim = raw_input('> ')
		
		#User chose swim
		if swim == 'swim':
			print('You ease yourself into the water...')
			time.sleep(1)
			print('You feel something brush your leg...')
			time.sleep(1)
			print('OH NO! Its a crocodile!')
			time.sleep(1)
			print('You made an excellent snack!')
			
		#User chose continue	
		elif swim == 'continue':
			print('You begin to walk again...')
			time.sleep(1)
			print('You are still using caution and scanning your surroundings')
			time.sleep(1)
			print('GRRRRRRRRRR')
			print('You begin to run, but its too late!')
			time.sleep(1)
			print('You turn around quickly and you are face to face with a huge lion!')
			print('There is no escape.')
			time.sleep(1)
			print('The lion licks his lips and finishes you off!')
		#User inputed an invalid choice	
		else: 
			print('Sorry you did not pick a valid option!')
			
	#User chose across		
	elif river == 'across':
		print('You slowly ease yourself in the river.')
		print('You are not the best swimmer, so you are happy you can touch the rivers bottom.')
		time.sleep(1)
		print('After fighting your way through the oddly agressive current, you finally make it to the other side')
		print('You are feeling quite sleepy, and you also notice the sun is going down')
		time.sleep(1)
		
		#The user has to chose between sleeping, or to continue walking to a better spot to sleep
		print('Do you want to sleep here (here), or continue walking till you find a more cozy location (continue)?')
		sleep = raw_input('> ')
		
		#User chose here
		if sleep == 'here':
			print('Such an uncomfortable place to sleep, but you some how manage to fall asleep.')
			time.sleep(1)
			print('Suddenly, you are awaken by a group of about 10 monkeys punching and pulling at your hair and body!')
			time.sleep(1)
			print('OUCH!')
			print('You think to yourself "what did I ever do these monkeys?"')
			print('You black out.')
		
		#User choose continue	
		elif sleep == 'continue':
			print('After another hour or so of walking you see what looks like a tent in the distance!')
			time.sleep(1)
			print('You begin running toward it!')
			print('Could you be saved?!')
			time.sleep(1)
			print('You trip on the unlevel ground...')
			time.sleep(1)
			print('You open your eyes slowly...')
			time.sleep(1)
			print('You are in your bedroom! It was all just a dream!')
		#User inputed an invalid choice			
		else: 
			print('Sorry you did not pick a valid option!')
		
	#User inputed an invalid choice			
	else: 
		print('Sorry you did not pick a valid option!')
	
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
	print('Sorry you did not pick a valid direction!')
		

