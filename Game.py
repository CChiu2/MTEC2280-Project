import sys
import time

#The game consists of six area being, Blacksmith, Church, Street
#Guard Barrack, Home, Mage Tower. Six states are required TBD
invArray = ["Notepad"]
notepadEntry = ["Murder Scene", "Victim"]
area = "0"

def inventoryAccess(playerInv):
	if(playerInv == "i" or playerInv == "Inventory" or playerInv == "I" or playerInv == "inventory"):
		print("_________________________________")
		while(True):
			#Keep the inventory running
			countInv = 0
			while(countInv < len(invArray)):

				print(invArray[countInv])
				time.sleep(0.5)
				countInv = countInv + 1

			print("_________________________________")
			print("Type 'Exit' to exit inventory screen or type an item name to see its detail")
			nextInput = input("")

			if(nextInput == "Notepad" or nextInput == "notepad"):
				time.sleep(0.5)
				print("Notepad: Your notepad where you keep all your notes...")
				print("[View Notes?]")
				print("1. [Yes] \n2. [No]")
				notepadInput = input("")

				if(notepadInput == "1"):
					while(True):
						if('notepadEntry[countNote] == "Murder Scene"'):
							entryDescription = ": Located in an alleyway in the center of the Coronian Market Place. A very busy place, someone must've seen something."
						if('notepadEntry[countNote] == "Victim"'):
							entryDescription = ": Male. Not much is known about the victim except the left side of his face is burnt. He wore typical undergarment when found. He had nothing on him."

						print("_________________________________")
						countNote = 0
						while(countNote < len(notepadEntry)):
							print(notepadEntry[countNote] + entryDescription)
							time.sleep(0.5)
							countNote = countNote + 1

						print("_________________________________")
						print("Type 'Exit' to exit notepad")
						notepadInput = input("")
						print("_________________________________")
						time.sleep(0.5)

						if(notepadInput == "Exit" or notepadInput == "exit"):
							break
							break
			if(nextInput == "Loose Brick" or nextInput == "loose brick" or nextInput == "Loose brick" or nextInput == "loose Brick"):
				time.sleep(0.5)
				print("Loose Brick: A loose brick found in the walls of the alleyway. Perhaps it might be useful for something...")
				time.sleep(0.5)
				print("_________________________________")
				time.sleep(0.5)
			if(nextInput == "White Solid Substance" or nextInput == "white solid substance"):
				time.sleep(0.5)
				print("White Solid Substance: Strange bits of a white solid substance was found in the alleyway")
				time.sleep(0.5)
				print("_________________________________")
				time.sleep(0.5)
			if(nextInput == "item4" or nextInput == "Item4"):
				time.sleep(0.5)
				print("item4: item description")
				time.sleep(0.5)
				print("_________________________________")
				time.sleep(0.5)
			if(nextInput == "Exit" or nextInput == "exit"):
				break
				break



#Additional state/area will be required due to additional dialogue 
#Choices or tutorial/menu other areas etc.

#Will put function on hold until a proper structure is created
#Function probably used for invalid input
#def invalidInput(PInput):
#	if(PInput == 0):
#		print("Invalid response, try again")

while(True):
	if(area == "0"):
		#Menu of the game.
		print("Welcome to (Name of Game TBD) \n Type in a number to proceed \n 1. Start \n 2. Quit")
		userInput = input("")

		if(userInput == "1"):
			area = "1"
		elif(userInput == "2"):
			break

	if(area == "1"):
		#Enter player name 
		print("What is your name?")
		name = input("")
		time.sleep(2)
		#Need to ask professor about function regarding time delays
		#And probably something about text wraps
		print("Greetings, " + name + " \nYou were once a citizen in a city named Corona, \nwhich is the capital of a massive alliance...but none of that really matter")
		time.sleep(1)
		print("Following the footstep of your father you decided to become a city guard.")
		time.sleep(1)
		print("This isn't a tale of grandeur or famous battle...")
		time.sleep(1)
		print("At least the pay is good and less life threatening")

		area = "2"
		#The game begins and move towards its first scene

#_____________________PLAYER HOME, AREA IS 2, __________________________
	if(area == "2"):
		print("____________________________________________")
		hidHomeDialogue = 0
		time.sleep(3)
		#Player home
		print(name + "'s House")
		time.sleep(1)
		print("[You hear the call of a rooster.]")
		time.sleep(1)
		print("[There's a knock on the door..]")
		print("1. [Answer the Door] \n2. [Ignore it]")
		playerResp = input("")

		def areaOne(a1response):
			if(a1response == "1"):
				return(1)
			if(a1response == "2"):
				return(2)
			if(a1response == "3"):
				return(3)

		if(playerResp == "1"):
			time.sleep(1)
			print("[There's a man in tattered clothing standing in your doorway]")
			time.sleep(1)
			print("Messenger: Good morning Mr. " + name + "!")
			print("1. 'Who are you?' \n2. 'Good morning' \n3. [Close the Door]")
			messengerResp = input("")
			dialogueA1 = areaOne(messengerResp)

		if(playerResp == "2"):
			dialogueA1 = areaOne("3")
#------------------------DIALOGUE A1---------------------------------
		if(dialogueA1 == 1):
				print("'I'm the morning messenger sir. I am suppose to wake you this morning'")
				time.sleep(1)
				print(name + ": 'Ah right.'")
				time.sleep(1)
				print("1.'Good morning' \n2.[Close the Door]")
				messengerResp2 = input("")
				if(messengerResp2 == "2"):
					dialogueA1 = areaOne("3")
				elif(messengerResp2 == "1"):
					dialogueA1 = areaOne("2")

		if(dialogueA1 == 2):
				time.sleep(1)
				print("Morning Messenger:'Morning sir, now that I've woke you, I must wake the others.'")
				time.sleep(1)
				print("[The tattered man ran down the street and continue knocking on doors]")

		if(dialogueA1 == 3):
				print("'Mr. " + name + " you need to wake up! It's dawn!'")
				time.sleep(1)
				print("[Finally, you got up and answered the door]")
				time.sleep(2)
				print(name + ": '...Morning'")
				time.sleep(1)
				print("Morning Messenger:'Morning sir, now that I've woke you, I must wake the others.'")
				time.sleep(1)
				print("[The tattered man ran down the street and continue knocking on doors]")
#--------------------------------------------------------------------	
		time.sleep(2)
		print("Today is your first day on the job.")
		time.sleep(2)
		print("Your partner awaits you in the barrack.")
		time.sleep(2)
		print("Your first day as a city guard...just like your father.")
		time.sleep(2)
		print("You don the once proud red armor of your father,")
		time.sleep(2)
		print("a typical Coronian armor that has endured much.")
		time.sleep(2)
		print("And proceeded to the guard barrack.")
		area = "3"
#-----------------SECOND VISIT TO HOME---------------------------------
		#if(hidHomeDialogue == 1 and ):
			#If this is the second time player is in area 2 then different dialogue will be triggered even if the state is the same

#______________________GUARD BARRACK, AREA IS 3,________________________
#Hidden Dialogue:Change the varaible that causes different if statement
	if(area == "3"):
		print("____________________________________________")
		time.sleep(3)
		print("Coronian Guard Barrack")
		time.sleep(1)
		print("A large building with brick exterior and a wooden interior")
		time.sleep(1)
		print("Wooden tables and chairs lying around with racks of weapons and armors to the side")
		time.sleep(1)
		print("The barrck is already full of guards both on and off duty \ndoing different things ranging from playing cards to eating \ntheir breakfast around the tables.")
		time.sleep(2)
		print("You approach the captain of the barrack and salute")
		time.sleep(1)
		print("Captain Faust: 'Welcome " + name + ". We've been expecting you.'")
		time.sleep(1)
		print(name + ": 'Good morning captain.'")
		time.sleep(1)
		print("Captain Faust: 'Nervous about your first day?'")
		print("1. 'Not at all.' \n2. 'A little.' \n3. 'Very..'")
		dialogueA3a = input("")
		if(dialogueA3a == "1"):
			time.sleep(1)
			print("Captain Faust: 'Really? Good keep up that energy.'")
		elif(dialogueA3a == "2"):
			time.sleep(1)
			print("Captain Faust: 'That's to be expected. No worries.'")
		elif(dialogueA3a == "3"):
			time.sleep(1)
			print("Captain Faust: 'Hah! Don't worry son. We don't bite.'")

		time.sleep(1)
		print(name + ": 'Yes sir.'")
		time.sleep(1)
		print("Captain Faust: 'So. have you gotten a chance to meet your partner?'")
		time.sleep(1)
		print(name + ": 'No. I'm afraid not.'")
		time.sleep(1)
		print("Captain Faust: 'Well head on in.'")
		time.sleep(1)
		print("Captain Faust: 'His name is Adam Coleridge. Just look for him near the gambling table.'")
		time.sleep(1)
		print("1. 'Yes sir.' \n2. 'May I ask a few question?'")
		dialogueA3b = input("")
		if(dialogueA3b == "2"):
				time.sleep(1)
				print("Captain Faust: 'Sure, anything to keep me from the paper work.'")
				while(True):
					print("1. 'What's my partner, Coleridge like?' \n2. 'So what's my duty?' \n3. 'Tell me about the city.' \n4. 'Tell me about the barrack' \n5. 'Nevermind.'")
					dialogueA3c = input("")
					if(dialogueA3c == "1"):
						time.sleep(1)
						print("Captain Faust: 'Coleridege eh? Well from a professional standpoint he's a good guard.'")
						time.sleep(1)
						print("Captain Faust: 'On a personal though, he can get a little rowdy.'")
						time.sleep(1)
						print("Captain Faust: 'One of those tough guys but he's a good mentor I assure you just don't ever gamble with him.'")
						time.sleep(1)
						print(name + ": 'Why?'")
						time.sleep(1)
						print("Captain Faust: 'He has a bit of a temper when he loses and he does...a lot.")
						time.sleep(1)
						print("Captain Faust: 'If he's betting on you on a deadpool")
						print("you can bet your ass you'll be untouchable.'")
						time.sleep(1)
						print("Captain Faust: 'Hahaha!'")
						time.sleep(1)
						print("Captain Faust: 'Well! Do you need anything else?'")
						time.sleep(1)
					if(dialogueA3c == "2"):
						print("Captain Faust: 'Duty eh?'")
						time.sleep(1)
						print("Captain Faust: 'What every guard does I suppose. Keep the peace. Simple enough right?'")
						time.sleep(1)
						print(name + ": 'I guess...'")
						time.sleep(1)
						print("Captain Faust: 'Don't worry. Coleridge will brief you.")
						print(name + ": 'Right.'")
						time.sleep(1)
						print("Captain Faust: 'Anything else?'")
						time.sleep(1)
					if(dialogueA3c == "3"):
						print("Captain Faust: 'The city? Didn't you grow up here?'")
						time.sleep(1)
						print(name + ": 'Yes, but in a guard's point of view I suppose.'")
						time.sleep(1)
						print("Captain Faust: 'I suppose there are things we know that a civilian doesn't'")
						time.sleep(1)
						print("Captain Faust: 'Well as you know, Corona is divided in to three sections.")
						time.sleep(1)
						print("Captain Faust: 'The nobles, the commoners and the slums.'")
						time.sleep(1)
						print("Captain Faust: 'Our station is mostly the commons, the market especially.'")
						time.sleep(1)
						print("Captain Faust: 'In fact, you and Coleridge will be patrolling the markets today.'")
						time.sleep(1)
						print("Captain Faust: 'The worst of the market is really just petty thief and the occasion shouting match between merchants.'")
						time.sleep(1)
						print("Captain Faust: 'That's all I can spare for now, but if you want to know more, I'm sure you can find more information in the archive.'")
						time.sleep(1)
						print(name + ": 'Okay, thank you captain.'")
						time.sleep(1)
						print("Captain Faust: 'No problem, anything else?'")
						time.sleep(1)
					if(dialogueA3c == "4"):
						print("Captain Faust: 'The barrack? What's to tell?'")
						time.sleep(1)
						print("Captain Faust: 'Well, let's see..")
						time.sleep(1)
						print("Captain Faust: 'The building is pretty old.")
						time.sleep(1)
						print("Captain Faust: 'The mess hall is where our commons are.'")
						time.sleep(1)
						print("Captain Faust: 'Most of the guards are gathered there when they're off duty.")
						time.sleep(1)
						print("Captain Faust: 'I'm not really strict about the rule.'")
						time.sleep(1)
						print("Captain Faust: 'I only ask that there's no drinking in the barrack for obvious reasons.'")
						time.sleep(1)
						print(name + ": 'Right.'")
						time.sleep(1)
						print("Captain Faust: 'That's all I have to say about the barrack. Anything else?'")
						time.sleep(1)
					if(dialogueA3c == "5"):
						print("Captain Faust: 'Alright. Fair enough.'")
						time.sleep(1)
						print("Captain Faust: 'Head on in, and find Coleridge.'")
						time.sleep(1)
						print(name + ": 'Yes captain.'")
						time.sleep(1)
						break

#--------------------------Starting Dialogue with Partner-------------

		time.sleep(1)
		print("You approach your new partner \nwho sits at one of the table piled with cards and coins")
		time.sleep(1)
		print("[BEWARE OF RESPONSE TO YOUR PARTNER]")
		time.sleep(1)
		print("A gruff, hairy looking man with a weary looking complexion \nbut clearly far too much energy for gambling looks up at you.")
		time.sleep(1)
		print("Coleridge: 'What are you looking at?'")
		print("1. 'Good morning! I'm your partner!' \n2. 'I'm your new partner.' \n3. 'Dumbass, I'm your new partner.'")
		dialogueA3d = input("")
#------------------DIALOGUE A3D---------------------------------------
		if(dialogueA3d == "1"):
			time.sleep(1)
			print("Coleridge: '..You're kidding me..'")
			time.sleep(1)
			print(name + ": 'I'm not.'")
			time.sleep(1)
			print("Coleridge: 'Aw god...'")
			time.sleep(1)
			print(name + ": 'Is there a problem?'")
			time.sleep(1)
			print("Coleridge: 'No, no, absolute not. It's just..too early in the morning for rainbows and sunshine.")
			time.sleep(1)
			partnerRel = 3

		elif(dialogueA3d == "2"):
			time.sleep(1)
			print("[The man looks up and down inspecting you]")
			time.sleep(1)
			print("Coleridge: 'Alright..fair enough, you look competent enough.'")
			time.sleep(1)
			print(name + ": 'Fair enough. It's nice to meet you.'")
			time.sleep(1)
			partnerRel = 5

		elif(dialogueA3d == "3"):
			time.sleep(1)
			print("The man slowly stands up ")
			time.sleep(1)
			print("The other guards around the gambling table stops")
			time.sleep(1)
			print("Coleridge: 'New partner huh...'")
			time.sleep(1)
			print("Coleridge gives you a fake smile")
			time.sleep(1)
			print("Coleridge: 'Nice to meet you too..smart-ass'")
			time.sleep(1)
			parnterRel = 0
#------------------END DIALOGUE FOR AREA 3 FIRST VISIT----------------
		print("Coleridge: 'Name's Coleridge...'")
		time.sleep(1)
		print(name + ": 'Yeah, I know. Captain Faust introduced you already.'")
		time.sleep(1)
		print(name + ": 'My name's " + name + ".'")
		time.sleep(1)
		print("Coleridge: 'Okay, alright. Well, seems like you're all ready to go.'")
		time.sleep(1)
		print(name + ": 'Yeah.'")
		time.sleep(1)
		print("Coleridge: 'Have you got a bag yet?'")
		time.sleep(1)
		print(name + ": 'Uh..bag?'")
		time.sleep(1)
		print("Coleridge: 'Yeah. All of us get a bag, to carry stuff just in case.'")
		time.sleep(1)
		print("[Coleridge tosses an empty brown bag at you.]")
		time.sleep(1)
		print(name + ": 'Uh..thanks.'")
		time.sleep(1)
		area = "4"
		hidBarrackDialogue = 0
#-----------------SECOND VISIT TO THE BARRACKS-------------------------
	if(area == "3.2"):
		print("____________________________________________")
		time.sleep(3)
		print("Corona Barack: Basement/Morgue")
		time.sleep(1)
		print("[The guards lay the body on the wooden table]")
		time.sleep(1)
		print("[Captain Faust, you, and Coleridge surround the body]")
		time.sleep(1)
		print("[A bald man with a goatee in green and golden colored robe enter]")
		time.sleep(1)
		print("Captain Faust: 'Scholar Will. Welcome back.'")
		time.sleep(1)
		print("Scholar Will: 'Considering everytime I return I have to look at a dead body I'd keep your welcome to yourself captain.")
		time.sleep(1)
		print("Captain Faust: 'Right. Well " + name + ", This is Scholar William.'")
		time.sleep(1)
		print("Captain Faust: 'He's a professor at the university nearby and whenever we find a dead body we call him down to examine them.'")
		time.sleep(1)
		print("Scholar William: 'You're new I presume?")
		time.sleep(1)
		print("1. 'Yes I am, nice to meet you.' \n2. 'Mhm..' \n3. 'No shit Sherlock'")
		dialogueA3e = input("")

		if(dialogueA3e == "1"):
			print("Scholar William: 'Good to see manner here. He's a keeper Faust.'")
			time.sleep(1)
			print("[Captain Faust nods on with pride]")
			time.sleep(1)
		if(dialogueA3e == "2"):
			print("Scholar William: 'Eh...Alright.'")
			time.sleep(1)
		if(dialogueA3e == "3"):
			print("Scholar William: 'Ah, that respond reminds me of when I first met Mr.Coleridge.'")
			time.sleep(1)
			print("[Coleridge walks over patting your back.]")
			time.sleep(1)
			print("Coleridge: 'What can I say? I teach them well.'")
			time.sleep(1)
			print("[Captain Faust stands there shaking his head]")
			time.sleep(1)
			partnerRel = partnerRel + 5

		print("[The Scholar begin examining the body]")
		time.sleep(1)
		print("Scholar William: 'Let's go over the obvious first shall we?'")
		time.sleep(1)
		print("Scholar William: 'Obviously, something hot hit him in the face.'")
		time.sleep(1)
		print("Scholar William: 'Pretty bad burns too.'")
		time.sleep(1)
		print("Scholar William: 'Either something very very hot hit him right in the face..'")
		time.sleep(1)
		print("Scholar William: 'Or something hot just stay on his face for a little while.'")
		time.sleep(1)
		print("Scholar William: 'I'll need a little more time to examine him in detail.")
		time.sleep(1)
		print("Scholar William: 'Come back in say an hour or so?")
		time.sleep(1)
		print("Captain Faust: 'Alright then. The two of you should begin your investigation.'")
		time.sleep(1)
		print(name + ": 'Yes sir!'")
		time.sleep(1)
		print("Coleridge: 'Fine...'")
		time.sleep(1)
		area = "100"
#-----------------THIRD VISIT TO THE BARRACKS--------------------------
	#if(area == "3.3"):
		#If this is the second time player is in area 3 then different dialogue will be triggered even if the state is the same
#---------------------------AREA 4 CORONA MARKET-----------------------
	if(area == "4"):
		time.sleep(3)
		print("____________________________________________")
		print("Coronian Market, the area is bustling except for the occasional alley...")
		time.sleep(1)
		print("You're walking around with your partner")
		time.sleep(1)
		print("You notice something in the alley")
		time.sleep(1)
		print(name + ": 'Coleridge, stop. There's something over there.'")
		time.sleep(1)
		print("Coleridge: 'Huh? What?'")
		time.sleep(1)
		print("[Coleridge takes a sip from his alcohol bottle]")
		time.sleep(1)
		print(name + ": 'Really?'")
		time.sleep(1)
		print("Coleridge: 'Captain said I can't drink in the barrack. Never said anything about patrol.'")
		time.sleep(1)
#----------------------FIRST EVENT - BODY IS FOUND----------------------
		print("1. [Go check it out] \n2. [Keep walking]")
		playerA4R1 = input("")

		if(playerA4R1 == "2"):
			print("Coleridge: 'You smell something burning?'")
			time.sleep(1)
			print(name + ": 'A little. Yeah.'")
			time.sleep(1)
			print("Coleridge: 'Cmon kid. Let's check it out.'")
			time.sleep(1)
			print("[Your partner walk down the alley]")
			time.sleep(1)
			print("[You slowly follow him]")
			time.sleep(1)

		print("[There's a man with his back towards you and Coleridge leaning against the garbage can in the middle of the alley.]")
		time.sleep(1)
		print("Coleridge: 'Hey man! Get outta there!'")
		time.sleep(1)
		print("Coleridge: 'There's no scrap for you in there!'")
		time.sleep(1)
		print("[No response]")
		time.sleep(1)
		print(name + ": 'Sir?'")

		print("1. [Turn him over] \n2. [Leave him be]" )
		playerA4R2 = input("")

		if(playerA4R2 == "1"):
			print("[You turn the man over]")
			time.sleep(1)

		if(playerA4R2 == "2"):
			time.sleep(1)
			print("Coleridge: 'Nah kid. This is our district and its our job to keep these bums out of our garbage.'")
			time.sleep(1)
			print(name + "'That's kind of harsh...'")
			print("[He turns the man over]")

		print("[He slums down, dead with the right side of his face black and melted like]")
		time.sleep(1)
		print("[Coleridge backs away cringing slightly]")
		time.sleep(1)
		print(name + ": 'He's dead.'")
		time.sleep(1)
		print("Coleridge: 'No shit kid. Talk about a face only a mother could love...'")
		time.sleep(1)
		print("[You begin examining the body]")
		time.sleep(1)

		while(True):
			print("1. [Examine the face] \n2. [Check his clothing] \n3. [Finish] ")
			playerA4R3 = input("")

			if(playerA4R3 == "1"):
				print("[His face is black and melted like. It seems like a pretty bad burnt]")
				time.sleep(1)
			if(playerA4R3 == "2"):
				print("[He's wearing basic inner clothes. There's no pockets.]")
				time.sleep(1)
			if(playerA4R3 == "3"):
				break
				time.sleep(1)

		print("[You turn to your partners and sees him walking away.]")
		time.sleep(1)
		print(name + ": 'Coleridge! What are you doing?'")
		time.sleep(1)
		print("Coleridge: 'What do you think? I'm calling it into the mage guild.'")
		time.sleep(1)
		print(name + ": 'Mage guild? Why?'")
		time.sleep(1)
		print("Coleridge: 'His face says magic all over it.'")
		time.sleep(1)
		print(name + ": 'You didn't even look at it. What if it isn't?'")
		time.sleep(1)
		print("Coleridge: 'Well, the mage guild can come check it out.")
		time.sleep(1)
		print("Coleridge: 'If it isn't magic then someone hopefully not our shift will investigate it.'")
		time.sleep(1)
		print(name + ": 'We found him. He's our responsibility.'")
		time.sleep(1)
		print("[Coleridge let out a sigh]")
		time.sleep(1)
		print("Coleridge: 'Alright..alright fine but we still got to call it in anyway...'")
		time.sleep(1)
		print("[Coleridge walks off..]")
		time.sleep(1)
#----------------------------------------------------------------------
		print("[The area is swarmming with guards and mages]")
		time.sleep(1.5)
		print("[You stand besides your partner looking over the body with several other guards and mages]")
		time.sleep(1.5)
		print("[Captain Faust approaches]")
		time.sleep(1.5)
		print("Captain Faust: 'First day and already a body.'")
		time.sleep(1.5)
		print("Captain Faust: 'Don't know if you're cursed or blessed.'")
		time.sleep(1.5)
		print(name + ": 'Captain Faust!'")
		time.sleep(1.5)
		print("[You salute the captain]")
		time.sleep(1.5)
		print("Captain Faust: 'What do you have " + name + "?'")
		time.sleep(1.5)
		print(name + ": 'Male body. Burnt on the face.'")
		time.sleep(1.5)
		print(name + ": 'We're still waiting on the mages to tell us if its magic.'")
		time.sleep(1.5)
		print("Captain Faust: 'I see.'")
		time.sleep(1.5)
		print("Mage: 'Its not magic in origin. Just fire.'")
		time.sleep(1.5)
		print("Coleridge: 'God dammit!'")
		time.sleep(1.5)
		print("[Coleridge swings his alcohol bottle up in to the air]")
		time.sleep(1.5)
		print("Captain Faust: 'Coleridge! Are you drinking on patrol?!'")
		time.sleep(1.5)
		print("[Coleridge notices the captain for the first time and hides the bottle behind his back]")
		time.sleep(1.5)
		print("Coleridge: 'Oh heh! Heya cap'n. When did you get here?'")
		time.sleep(1.5)
		print("[Faust narrows his eyes at Coleridge then turn back to you.]")
		time.sleep(1.5)
		print("[Coleridge walks up and join the conversation as the mages begin to leave]")
		time.sleep(1.5)
		print("Captain Faust: 'Well since it isn't magic in origin..this is our case. Its your choice " + name + ".")
		time.sleep(1.5)
		print("Captain Faust: 'Do you want to investigate this or not?'")
		time.sleep(1.5)
		print("Coleridge: 'Why does he get to decide? I'm the senior g-'")
		time.sleep(1.5)
		print("Captain Faust: 'Because we all know your answer Coleridge.'")
		time.sleep(1.5)
		print("Captain Faust: 'Its your first day so I won't hold it against you. Your call.'")
		time.sleep(1.5)
		print(name + ": 'Of course sir. We found him, he's our responsibility.'")
		time.sleep(1.5)
		print("Coleridge: 'Ours?'")
		time.sleep(1.5)
		print("Captain Faust: 'Than its decided. We're taking the body back to the barrack for inspection. Get going you two.'")
		time.sleep(1.5)
		print(name + ": 'Yes sir!'")
		time.sleep(1.5)
		print("Coleridge: 'Fine captain..'")
		time.sleep(1.5)
		print("Captain Faust: 'Coleridge! Go help the other carry the body back!'")
		time.sleep(1.5)
		print("Coleridge: 'But cap'n I...Ah fine!'")
		time.sleep(1.5)
		print("1. [Go help Coleridge] \n2. [Watch him] \n3. [Watch him and laugh]")
		playerA4R4 = input("")
		if(playerA4R4 == "1"):
			print("[You walked over to Coleridge and lend a hand]")
			print("Coleridge: 'Huh...thanks kid.'")
			partnerRel = partnerRel + 5
		if(playerA4R4 == "2"):
			print("[You watch your partner carry the burned man's body and slowly follow behind]")
			partnerRel = partnerRel + 0
		if(playerA4R4 == "3"):
			print("[You watch Coleridge as he carries the body and laugh as he passby..]")
			print("[Coleridge makes a slight growling noise as he pass]")
			partnerRel = partnerRel - 3

		area = "3.2"
#---------------------SECOND VISIT TO CORONA MARKET---------------------
	if(area == "4.2"):
		print("[You and Coleridge return to the market where part of the area including the alley is sealed off by guards]")
		time.sleep(1)
		print("[A guard stands in front of the alleyway]")
		time.sleep(1)
		print("Guard: 'You must be " + name + " and Coleridge...'")
		time.sleep(1)
		print(name + ": 'That's right.'")
		time.sleep(1)
		print("Guard: 'We've been expecting you. Go ahead in. If you're done investigating talk to me.'")
		time.sleep(1)
		print(name + ": 'Got it. Thank you.'")
		time.sleep(1)
		print("[You and Coleridge proceeded in to the alleyway]")
		time.sleep(1)
		print("-BEGIN INVESTIGATION-")
		time.sleep(1)
		print("Coleridge: 'Remember kid, if you found any evidence you can put them in your bag.'")
		time.sleep(1)
		print(name + ": 'Right...I should start taking notes and keep them in my bag as well...'")
		print("-NOTES UPDATED: MURDER SCENE-")
		print("-NOTES UPDATED: VICTIM-")
		print("-TO ACCESS YOUR INVENTORY, TYPE 'i' OR 'inventory' DURING INVESTIGATION OR INTERROGATION-")
		time.sleep(2.5)
		while(True):

			print("1. [Examine the Garbage Can] \n2. [Examine the Alleyway] \n3. [Talk to the Guard]")
			playerInv1 = input("")
			inventoryAccess(playerInv1)

			if(playerInv1 == "1"):
				print("[A typical garbage can....It seems to be empty.]")
				while(True):
					print("1. [Consult Coleridge] \n2. [Examine the lid] \n3. [Look around the can] \n4. [Look underneath the can] \n5. [Back]")
					playerInv1a = input("")
					inventoryAccess(playerInv1a)

					if(playerInv1a == "1"):
						print(name + ": 'What do you think Coleridge?'")
						time.sleep(1)
						print("Coleridge: 'What do I think? It's a garbage can! What do I think...'")
						time.sleep(1)
					if(playerInv1a == "2"):
						print("[You lifted the lit and inspect it from top to bottem]")
						time.sleep(1)
						print("[Its clean...or rather there's nothing suspicious about it...]")
						time.sleep(1)
					if(playerInv1a == "3"):
						print("[You walk around the can looking around the alleyway]")
						time.sleep(1)
						print("Only a few pieces of garbage lying around...nothing relevant it seems")
						time.sleep(1)
					if(playerInv1a == "4"):
						print("[You lift the can and look at the bottem...]")
						time.sleep(1)
						print("[Nothing but more garbage..]")
						time.sleep(1)
					if(playerInv1a == "5"):
						break
						time.sleep(1)

			if(playerInv1 == "2"):
				print("You look around the alley...")
				print("[Nothing seems out of the ordinary...]")
				while(True):
					print("1. [Consult Coleridge] \n2. [Examine the walls] \n3. [Check the ground] \n4. [Back]")
					playerInv1b = input("")
					inventoryAccess(playerInv1a)

					if(playerInv1b == "1"):
						print(name + ": 'Anything Coleridge?'")
						time.sleep(1)
						print("Coleridge: 'Well you gotta praise the guy. He's either desperate or brilliant...'")
						time.sleep(1)
						print(name + ": 'What makes you say that?'")
						time.sleep(1)
						print("Coleridge: 'He dumped a body in an alley surrounded by a crowded market...")
						time.sleep(1)
						print("Coleridge: 'Not to mention this is a pretty frequent patrol route.'")
						time.sleep(1)
						print(name + ": 'Do you think he'd leave a witness?'")
						time.sleep(1)
						print("Coleridge: 'Does a dog have legs?'")
						time.sleep(1)
					if(playerInv1b == "2"):
						print("[You look around the brick wall of the alley...]")
						time.sleep(1)
						print("[You feel around the wall and there seems to be a loose brick..]")
						time.sleep(1)
						print("[Maybe this will come in handy...]")
						time.sleep(1)
						print("-INVENTORY UPDATED: LOOSE BRICK-")
						invArray.insert(1, "Loose Brick")
						time.sleep(1)
						print("Coleridge: 'Really? A brick?'")
						time.sleep(1)
					if(playerInv1b == "3"):
						print("[You examine the ground ]")
						time.sleep(1)
						print("[More garbge..]")
						time.sleep(1)
						print(name + ": 'Hm...what's this?'")
						time.sleep(1)
						print("[There's bits of a solid white substance near the garbage can...]")
						time.sleep(1)
						print("Coleridge: 'What the hell is that?'")
						time.sleep(1)
						print(name + ": 'Don't know. Best get it back to Scholar William.")
						time.sleep(1)
						print("[You place the substance inside a smaller clean bag...]")
						print("-INVENTORY UPDATED: WHITE SOLID SUBSTANCE-")
						invArray.insert(1, "White Solid Substance")
					if(playerInv1b == "4"):
						break
						time.sleep(1)

			if(playerInv1 == "3"):
				print("[You approach the guard...]")
				print("Guard: 'Are you ready to go?'")
				print("1. 'I have some questions...' \n 2. 'Yeah, I'm ready to leave'")
				playerInv2 = input("")

				if(playerInv2 == "1"):
					print("Guard: 'Of course.'")
					while(True):
						print("1. 'Was there any witness?' \n2. 'Tell me about the area...' \n3. 'That's it, thank you.'")
						playerInv2a = input("")

						if(playerInv2a == "1"):
							print("Guard: 'There was a few who saw people going in and out of the alley'")
							time.sleep(1)
							print("Guard: 'But I'm afraid there's nothing concrete.'")
							time.sleep(1)
							print("Guard: 'As crowded as the area is, the place is to busy for anyone to look at some alley.'")
							time.sleep(1)
							print(name + ": 'Fair enough.'")
						if(playerInv2a == "2"):
							print("Guard: 'The market is usually crowded.'")
							time.sleep(1)
							print("Guard: 'The buildings besides the alleyway is a blacksmith and a general store'")
							time.sleep(1)
							print("Guard: 'The alley itself leads into the church courtyard'")
							time.sleep(1)
							print(name + ": 'Thank you. I guess we'll start with those areas then.")
							time.sleep(1)
							print("[The guard nods.]")
							print("-NEW LOCATION: BLACKSMITH")
							print("-NEW LOCATION: GENERAL STORE")
							print("-NEW LOCATION: CHURCH")
							time.sleep(1)
							print("Guard: 'Anything else?'")

				if(playerInv2 == "2"):
					print("Guard: 'Are you sure?'")
					time.sleep(1)
					print("-WARNING: ONCE YOU LEAVE THE AREA ALL NON-COLLECTED EVIDENCE AND WITNESSES WILL BE GONE-")
					time.sleep(1)
					print("1. 'Yes' \n2. 'No'")
					playerInvExit = input("")

					if(playerInvExit == "1"):
						time.sleep(1)
						print("Guard: 'Okay. Take care...'")
						time.sleep(1)
						area = "100.1"
					if(playerInvExit == "2"):
						time.sleep(1)
						print(name + ": 'On second though let me look around some more.'")
						time.sleep(1)
						print("Guard: 'Very well.'")

#-----------------------ISOLATED AREAS----------------------------------
	if(area == "100"):
		print("____________________________________________")
		print("Coleridge: 'Well since its your bright ass idea to investigate this...You can take lead.'")
		print("1. 'Maybe you should take responsibility...(Confront) \n2. 'Fine...'(Accept) \n3. 'What? No!'(Resist) \n4. 'Fine..but..'(Compromise)")
		dialogueAVa = input("")
    
		if(dialogueAVa == "1"):
			print(name + ": 'Maybe you should take responsibility as well.'")
			time.sleep(1)
			print(name + ": 'This is your case as well as mine and even if we didn't find that body, in the end it will still become our case.'")
			time.sleep(1)
			print("Coleridge: 'And you know this how?'")
			time.sleep(1)
			print(name + ": 'Because it's our job Coleridge'")
			time.sleep(1)
			print("Coleridge: 'And I was expecting an answer like, I'm psyhic..'")
			time.sleep(1)
			print("1. 'Is this a game to you?!'(Push) \n2. 'Nevermind..'(Back Off)")
			dialogueAVa1 = input("")

			if(dialogueAVa1 == "1"):
				print(name + ": 'Is this a game to you?!'")
				time.sleep(1)
				print(name + ": 'Why would you become a city guard if this is all a joke for you?!'")
				time.sleep(1)
				print("Coleridge: 'It pays well..now do we have a murderer to catch or you want to keep interrogating me?'")
				time.sleep(1)
				print(name + ": 'Ugh...'")
				time.sleep(1)
				partnerRel = partnerRel - 1

			if(dialogueAVa1 == "2"):
				print(name + ": 'Nevermind. There doesn't seem to be any point in talking.'")
				time.sleep(1)
				print("Coleridge: 'Smartest thing you've said all day kid.")
				time.sleep(1)
				partnerRel = partnerRel + 2

		if(dialogueAVa == "2"):
			print(name + ": 'Fine..I'll take lead in this case.'")
			time.sleep(1)
			print("Coleridge: 'Good, because I sure as hell won't.'")
			time.sleep(1)
			partnerRel = partnerRel + 2

		if(dialogueAVa == "3"):
			print(name + ": 'What? No! I'm only a rookie!'")
			time.sleep(1)
			print("Coleridge: 'And yet we're in this case because of you...")
			time.sleep(1)
			print(name + ": 'We were patrolling the area. It would've been our case even if we didn't find the body.'")
			time.sleep(1)
			print("Coleridge: 'Like you said, you're the rookie. So I say, you're incharge of this case.")
			time.sleep(1)
			print(name + ": 'But...'")
			time.sleep(1)
			print("Coleridge: 'And think of it this way kid. This'll be good experience for you.'")
			time.sleep(1)
			print("Coleridge: 'Now get going.'")
			time.sleep(1)
			print(name + ": ''Okay..fine.")
			time.sleep(1)
			partnerRel = partnerRel + 3

		if(dialogueAVa == "4"):
			print(name + ": 'Fine..but you really should take this seriously.'")
			time.sleep(1)
			print("Coleridge: 'I am taking it seriously. That's why I'm putting you incharge.'")
			time.sleep(1)
			print("Coleridge: 'A four years old wouldn't trust me with his candies.'")
			time.sleep(1)
			print(name + ": 'Worst part is, I think I actually believe you.'")
			time.sleep(1)
			print("[Coleridge gives a big smile]")
			time.sleep(1)
			partnerRel = partnerRel + 5

		print("Coleridge: 'So, where to first rookie?'")
		time.sleep(1)
		print(name + ": 'Lets return to the scene of the crime first.'")
		time.sleep(1)
		print("Coleridge: 'Off we go then.'")
		time.sleep(1)
		area = "4.2"
