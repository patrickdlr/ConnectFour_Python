#possible 4connectgame
from pprint import pprint
rowlabel = ''

def spawler(hi):
	innerdicty = {}
	subnumber = 0
	for i in range(hamecolumn):
		subnumber += 1
#		innerdicty.setdefault((str(hi) + '.' + str(subnumber)), str(hi) + '-'	+ str(subnumber)) #to reveal numbers
		innerdicty.setdefault((str(hi) + '.' + str(subnumber)), '___')
	return innerdicty

def boardbuilder():
	for i in range(hamerow):
		global rowlabel	
		rowlabel = 'row-' + str(i + 1)
		dicty.setdefault(rowlabel, spawler(i+1))
while True:
	dicty = {}
	hamecolumn = int(input('how many columns? (7 or higher): ')) #must be 7 or higher?
	if hamecolumn >= 7:
		hamerow = int(input('how many rows?: (6 or higher)')) #must be 6 or higher
		if hamerow >= 6:
			boardbuilder()
			break
	else:
		continue

def finalboardlook():
	topperline = "v"
	print('\n' + 'Welcome to Connect Four'.center( 6 * hamecolumn))
	for i in range(hamecolumn):
		topperline += '______'
	pique = len(topperline) - 2
	print(' ' + ('_' * pique))
	for i in range(hamerow): #6 rows typically
		prime = '|'
		adjustednum1 = i + 1
		prime0 = '|'
	#	baka = 1
		for a in range(hamecolumn): #7 blocks typically
			baka = a + 1
			prime += '_' + str(dicty.get('row-' + str(adjustednum1)).get(str(adjustednum1) + '.' + str(baka))) + '_|' #1.1, 1.2, 1.3, 1.4
			prime0 += "     |"
		print(prime0)
		print(prime)
	bottomnumber = '  '
	for a in range(hamecolumn):
		bottomnumber += str(str(a + 1) + '  ').center(5) + ' '
	print(bottomnumber)
finalboardlook()

import random
numberofplayers = int(input('how many human players?: '))
numberofbots = int(input('how many bots?: '))

def numberorline(uu):
	if uu <= 8:
		return '_'
	else:
		return ''

playernumberdictionary = {}
for p in range(numberofplayers):
#	playernumberdictionary.setdefault('P' + str(int(p)+1), str('P' + str(int(p)+1) + '').ljust(3))
	playernumberdictionary.setdefault('P' + str(int(p)+1), str('P' + str(int(p)+1) + str(numberorline(p))).ljust(3))
print(playernumberdictionary) #to be hidden

botnumberdictionary = {}
for b in range(numberofbots):
#	botnumberdictionary.setdefault('b' + str(int(b)+1), str('_' + str(int(b)+1) + '').ljust(3))
	botnumberdictionary.setdefault('b' + str(int(b)+1), str('_' + str(int(b)+1) + str(numberorline(b))).ljust(3))
print(botnumberdictionary) #to be hidden

def whichrow(columnpick): #must return last row number
	rowey = hamerow
	while rowey > 0: #example hamerow = 6
		if dicty['row-' + str(rowey)][str(rowey) + '.' + str(columnpick)] == '___':
			dicty['row-' + str(rowey)][str(rowey) + '.' + str(columnpick)] = str(playerid)
			break
		else:
			rowey -= 1 
			continue

def whichrowbot(columnpick): #must return last row number
	rowey = hamerow
	while rowey > 0: #example hamerow = 6
		if dicty['row-' + str(rowey)][str(rowey) + '.' + str(columnpick)] == '___':
			dicty['row-' + str(rowey)][str(rowey) + '.' + str(columnpick)] = str(botid)
			break
		else:
			rowey -= 1 
			continue

def randomnumberpicker():  #make it more intelligent pl0x
	return int(random.randint(1,hamecolumn))

def dictywinlabeler(selection, ug, uy): #use string value if this dictywinlabeler doesnt activate
	if selection == '1':
		dicty['row-' + str(ug-0)][str(ug-0) + '.' + str(uy)] = 'win'
		dicty['row-' + str(ug-1)][str(ug-1) + '.' + str(uy)] = 'win'
		dicty['row-' + str(ug-2)][str(ug-2) + '.' + str(uy)] = 'win'
		dicty['row-' + str(ug-3)][str(ug-3) + '.' + str(uy)] = 'win'
	elif selection == '2':
		dicty['row-' + str(ug)][str(ug) + '.' + str(uy+0)] = 'win'
		dicty['row-' + str(ug)][str(ug) + '.' + str(uy+1)] = 'win'
		dicty['row-' + str(ug)][str(ug) + '.' + str(uy+2)] = 'win'
		dicty['row-' + str(ug)][str(ug) + '.' + str(uy+3)] = 'win'
	elif selection == '4':	#/
		dicty['row-' + str(ug-0)][str(ug-0) + '.' + str(uy+0)] = 'win'
		dicty['row-' + str(ug-1)][str(ug-1) + '.' + str(uy+1)] = 'win'
		dicty['row-' + str(ug-2)][str(ug-2) + '.' + str(uy+2)] = 'win'
		dicty['row-' + str(ug-3)][str(ug-3) + '.' + str(uy+3)] = 'win'	
	elif selection == '3':	#\
		dicty['row-' + str(ug+0)][str(ug+0) + '.' + str(uy+0)] = 'win'
		dicty['row-' + str(ug+1)][str(ug+1) + '.' + str(uy+1)] = 'win'
		dicty['row-' + str(ug+2)][str(ug+2) + '.' + str(uy+2)] = 'win'
		dicty['row-' + str(ug+3)][str(ug+3) + '.' + str(uy+3)] = 'win'	

def checkwin(id, playertype): #it works, works only if separated into several for loops (one for loop for each 4-dot winning position) - think deeply why
	global gamegame
	global whowon	
	#|
	for ug in range(1, hamerow+1):
		if gamegame == False:
			break 
		else:
			try:
				try:
					for uy in range(1, hamecolumn+1):
						if dicty['row-' + str(ug-0)][str(ug-0) + '.' + str(uy)] == str(id) and dicty['row-' + str(ug-1)][str(ug-1) + '.' + str(uy)] == str(id) and dicty['row-' + str(ug-2)][str(ug-2) + '.' + str(uy)] == str(id) and dicty['row-' + str(ug-3)][str(ug-3) + '.' + str(uy)] == str(id):
							dictywinlabeler('1', ug, uy)
							whowon = str(playertype) + ' ' + str(id) + ' wins'
							gamegame = False
							break
						else:
		 					gamegame = True
				except KeyError:
		 			gamegame = True
			except TypeError:
				gamegame = True
				
 	#checks horizontal left-to-right
	for ug in range(1, hamerow+1):
		if gamegame == False:
			break
		else:
			for uy in range(1, hamecolumn+1):
				try:
					try:
						if dicty['row-' + str(ug)][str(ug) + '.' + str(uy+0)] == str(id) and dicty['row-' + str(ug)][str(ug) + '.' + str(uy+1)] == str(id) and dicty['row-' + str(ug)][str(ug) + '.' + str(uy+2)] == str(id) and dicty['row-' + str(ug)][str(ug) + '.' + str(uy+3)] == str(id):
							dictywinlabeler('2', ug, uy)  #use string value to make sure that dictywinlabeler works. Idk if thats the real solution
							whowon = str(playertype) + ' ' + str(id) + ' wins'
							gamegame = False
							break
						else:
		 					gamegame = True
					except KeyError:
						gamegame = True
				except TypeError: #typeerror "catching classes that do not inherit from BaseException is n....." possible solution: TypeError instead or TypeError()
					gamegame = True 		
 	#checks diagonally /
	for ug in range(1, hamerow+1):
		if gamegame == False:
			break
		else:
			for uy in range(1, hamecolumn+1):
				try:
					try:
						if dicty['row-' + str(ug+0)][str(ug+0) + '.' + str(uy+0)] == str(id) and dicty['row-' + str(ug+1)][str(ug+1) + '.' + str(uy+1)] == str(id) and dicty['row-' + str(ug+2)][str(ug+2) + '.' + str(uy+2)] == str(id) and dicty['row-' + str(ug+3)][str(ug+3) + '.' + str(uy+3)] == str(id):
							dictywinlabeler('3', ug, uy)  #use string value to make sure that dictywinlabeler works. Idk if thats the real solution
							whowon = str(playertype) + ' ' + str(id) + ' wins'
							gamegame = False
							break
						else:
		 					gamegame = True
					except KeyError:
						gamegame = True
				except TypeError: #typeerror "catching classes that do not inherit from BaseException is n....." possible solution: TypeError instead or TypeError()
					gamegame = True					
	#checks diagonally \
	for ug in range(1, hamerow+1):
		if gamegame == False:
			break
		else:
			for uy in range(1, hamecolumn+1):
				try:
					try:
						if dicty['row-' + str(ug-0)][str(ug-0) + '.' + str(uy+0)] == str(id) and dicty['row-' + str(ug-1)][str(ug-1) + '.' + str(uy+1)] == str(id) and dicty['row-' + str(ug-2)][str(ug-2) + '.' + str(uy+2)] == str(id) and dicty['row-' + str(ug-3)][str(ug-3) + '.' + str(uy+3)] == str(id):
							dictywinlabeler('4', ug, uy)  #use string value to make sure that dictywinlabeler works. Idk if thats the real solution
							whowon = str(playertype) + ' ' + str(id) + ' wins'
							gamegame = False
							break
						else:
		 					gamegame = True
					except KeyError:
						gamegame = True
				except TypeError:
					gamegame = True

whowon = 'no one won.'
totaltries = 1
gamegame = True
while totaltries < ((hamerow)*(hamecolumn) +1) and gamegame == True:
	for r in range(numberofplayers):
		playerid = playernumberdictionary['P' + str(r+1)]
		if gamegame == False:
			break
		else:
			while totaltries < ((hamerow)*(hamecolumn) +1):
				playerXcolumnpick = input('player ' + str(playerid) + ', pick column #: ') 
#				playerXcolumnpick = randomnumberpicker()
				try:
					if dicty['row-1']['1.' + str(playerXcolumnpick)] != '___':
						print('this column # already used up')
						continue
					else:
						whichrow(playerXcolumnpick)
						totaltries += 1	
						checkwin(playerid, 'player')	
						finalboardlook()
#						pprint(dict(dicty))		
						break	 						
				except KeyError:
					print('invalid input')
					continue
	for r in range(numberofbots):	
		botid = botnumberdictionary['b' + str(r+1)]			
		if gamegame == False:
			break
		else:
			while totaltries < ((hamerow)*(hamecolumn) +1):
				stonenumber = randomnumberpicker()
				print('bot ' + str(botid) + ' picked: ' + str(stonenumber))
				if dicty['row-1']['1.' + str(stonenumber)] != '___':
					print('bot picked wrong column')
					continue
				else:
					whichrowbot(stonenumber)
					totaltries += 1
					checkwin(botid, 'bot')
					finalboardlook()
#					pprint(dict(dicty))
					break 

print(whowon)
print('game over')
input('Type to end this program.')