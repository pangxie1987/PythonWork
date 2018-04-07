from sys import exit

def start():
	print('You are in a dark room.')
	print("There are a door to your right and left")
	print('Which do you take?')
	
	next=input('>')
	
	if next=='left':
		bear_room()
	elif next=='right':
		cthulhu_room()
	else:
		dead('you around the romm until you starve')
	
def dead(why):
	print(why)
	exit(0)
	
def bear_room():
	print('there is a bear here')
	print('the bear has a bunch of honey')
	print('the fat bear is in front of another door ')
	print('how are you going to move the bear')
	bear_moved=False
	
	while True:
		next=input('>')
		
		if next=='take honey':
			dead('the bear looks you then slaps your face off')
			
		elif next=='taunt bear' and not bear_moved:
			print('the bear has moved from the door.you can go throung it now')
			bear_moved=True
			
		elif next=='taunt bear' and bear_moved:
			dead('the bear gets pissed off')
		elif next=='open the door' and bear_moved:
			gold_room()
		else:
			print('I got no idea what that means')
		
def gold_room():
	print('this room is full of gold how much do you take?')
	
	next=input('>')
	if '0' in next or '1' in next:
		how_much=int(next)
	else:
		dead('Man,learn to type a number ')
	if how_much<50:
		print('Nice,you are not greedy ,you win')
		exit(0)
	else:
		dead('you are greedy')
	
def cthulhu_room():
	print('here you see the great evil cthulhu')
	print('he,it ,whatvere stares at you and you go insane')
	print('do you flee for your life or eat your head?')
	
	next=input('>')
	if 'flee' in next:
		start()
	elif 'head' in next:
		dead('Well that was tasty!')
	else:
		cthulhu_room()
		
		
start()
	