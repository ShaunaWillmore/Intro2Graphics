#IntoTheJungle2
#Author: Shauna Willmore
#Last Modified By: Shauna Willmore
#Date Last Modified: May.23/ 2013
#Program Description: Basic text adventure game. User explores a jungle and decides how the story will play out.
#Revision History: May.21/2013(began writing the story without code). May.22/2013 (implemented if statements and prints)
#May.23/2013(finished story, and made sure all outcomes worked).

import time

#intro1
print('Welcome to Into The Jungle!')
print('During the story you will be asked for input on what you would like the character to do.')
print('Make sure you use one the options located in the brackets at the end of each decision!')
time.sleep(1)
print('Here we go...')
time.sleep(4)
print
print

#intro2
print ('You wake up with a terrible headache...')
print ('Where are you?!')
print ('You stand up slowly, and begin to glace around...')
print ('It appears you have awoken in a very dense jungle.')
print ('There are 2 visible paths, leading opposite directions.')
print

	
#Ask the users which direction to go first, the varible "path" equals the users input.
print ('Which direction will you go left or right(left/right)?')
path = raw_input('> ')
print
	
#The user has chose to go left. The value of "path" is "left".
if  path == 'left':
	print ('You begin to walk down the path...')
	print ('The scenery is beautiful...')
	print ('But something feels not right...')
	print
	time.sleep(1)
	print ('You walk for a bit.')
	print ('Unfortunitly you come to a river running right through the path')
	time.sleep(1)
	
	#The user has to chose whether to go around or across the river. The users input will become the value of "river".
	print ('Do you want to try and go around the river, or would you like to swim across(around/across)?')
	river = raw_input('> ')
	print

	#User chose around. The value of "river" is "around".	
	if river == 'around':
		print('You walk along side the river for what feels like hours...')
		print('Suddenly you hear what sounds like growling in the distance!')
		print('You stop walking and begin to scan your surroundings')
		print('Maybe you are just hearing things?!')
		time.sleep(1)
		
		#The user has to chose whether to swim across the river or continue walking around. The users input will become
		#the value of "swim".
		print('Do you want to swim across the river now or try your luck and continue walking (swim/continue)?')
		swim = raw_input('> ')
		print
		
		#User chose swim. The value of "swim" is "swim".
		if swim == 'swim':
			print('You ease yourself into the water...')
			time.sleep(1)
			print('You feel something brush your leg...')
			time.sleep(1)
			print('OH NO! Its a crocodile!')
			time.sleep(1)
			print('You made an excellent snack!')
			
		#User chose continue. The value of "swim" is "continue".	
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
			
	#User chose across. The value of "river" is "across".		
	elif river == 'across':
		print('You slowly ease yourself in the river.')
		print('You are not the best swimmer, so you are happy you can touch the rivers bottom.')
		time.sleep(1)
		print('After fighting your way through the oddly agressive current, you finally make it to the other side')
		print('You are feeling quite sleepy, and you also notice the sun is going down')
		time.sleep(1)
		
		#The user has to chose between sleeping, or to continue walking to a better spot to sleep. The users input will 
		#become the value of "sleep".
		print('Do you want to sleep here, or continue walking till you find a more cozy location (here/continue)?')
		sleep = raw_input('> ')
		print
		
		#User chose here.The value of "sleep" is "here".
		if sleep == 'here':
			print('Such an uncomfortable place to sleep, but you some how manage to fall asleep.')
			time.sleep(1)
			print('Suddenly, you are awaken by a group of about 10 monkeys punching and pulling at your hair and body!')
			time.sleep(1)
			print('OUCH!')
			print('You think to yourself "what did I ever do these monkeys?"')
			print('You black out.')
		
		#User chose continue. The value of "sleep" is "continue"	
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
	
#The user has chose to go right. The value of "path" is "right".
elif path == 'right':
	print ('You begin to walk down the path...')
	print ('The scenery is beautiful...')
	print ('But something feels not right...')
	print
	time.sleep(1)
	print ('You notice something in the distance')
	print ('BAH! Looks like theres a massive tree fallen right across the path!')
	print
	
	#User chooses whether to go over/around the tree. The users input becomes the value of "tree".
	print('Will you go around or over the fallen tree(around/over)?!')
	tree = raw_input ('> ')
	print
	
	#User chose to go around the tree. The value of "tree" is "around".
	if tree == 'around':
		print('This is the biggest tree you have ever seen!')
		print('It takes you nearly 10 mins to get around it!')
		print('On the other side you notice a bush of berries...')
		time.sleep(1)
		print('You feel your tummy growl')
		time.sleep(1)
		print
		
		#User chooses whether to eat the berries. The users input becomes the value of "eat".
		print('Eat the berries?! (yes/no)')
		eat = raw_input('> ')
		
		#User has chose to eat the berries. The value of "eat" is "yes".
		if eat == 'yes':
			print('Mmmmmm these berries are so good!')
			print('So good, that you nearly eat all the berries the bush has to offer')
			time.sleep(1)
			print('Your vision begins to blur...')
			time.sleep(1)
			print('The last thing you remember thinking is "maybe those berries were not such a good idea?!"')
			print
			
		#User has chose to not eat the berries. The value of "eat" is "no".
		elif eat == 'no':
			print('Days pass without anymore signs of food...')
			time.sleep(1)
			print('You begin to think you should of ate those berries...')
			time.sleep(1)
			print('You feel very weak and eventually you pass out from starvation.')
		
		#User did not input a valid value	
		else:
			print('Sorry, you did not pick a valid option!')
				
	#User chose to go over the tree. The value of "tree" is "over".	
	elif tree == 'over':
		print('You begin to climb over the tree...')
		print('As you get to the top, you notice a disgusting spider web drapped right across the scenery in front of you.')
		time.sleep(1)
		print('Your eyes drift to the center of the web...')
		time.sleep(1)
		print('"AHHHHHH!" You scream! There is what appears to the worlds biggest spider lingering in the middle of the web.')
		print
		time.sleep(1)
		
		#User has to choose whether to fight or run from the spider. The users input is the value of "spider".
		print('Do you want to fight the spider or run away?! (fight/run)')
		spider = raw_input('> ')
		print
		
		#User chose to fight. The value of "spider" is "fight".
		if spider == 'fight':
			print('You take a deep breath, and charge at the spider...')
			time.sleep(1)
			print('Adrenaline is pumping though your body.')
			print('You have never felt so fearless...')
			time.sleep(1)
			print('You punch and pull at the spider, but he is too big and too strong...')
			print('He manages to sink his fangs deep into your side...')
			time.sleep(1)
			print('There is no surviving this...')
			print('You wish you had run...')
			
		#User chose to run from the spider. The value of "spider" is "run.	
		elif spider == 'run':
			print('You quickly jump down  off the side you had just managed to climb up...')
			time.sleep(1)
			print('As soon as your feet hit the jungle floor, you begin to run...')
			print('There is no looking back. You never want to see something like that again...')
			time.sleep(1)
			print('You hear a growl behind you. You look behind, but continue to run forward...')
			time.sleep(1)
			print('You feel the floor give way, and suddenly you are falling...')
			time.sleep(1)
			print('You must of missed a hole in the ground.')
			time.sleep(1)
			print('Is this the end for you?!...')
			print
			print('You black out.')
		
		#User did not input a valid value	
		else:
			print('Sorry, you did not pick a valid option!')
			
	#User did not input a valid value	
	else: 
		print('Sorry you did not pick a valid option!')
	
		
#User did not input a valid value	
else: 
	print('Sorry you did not pick a valid direction!')
		

