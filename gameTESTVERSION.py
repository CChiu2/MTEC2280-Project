import sys
import time

locationArray = ["Blacksmith", "General Store", "Church"]
countArray = ["1. ", "2. ", "3. "]


invArray = ["Notepad"]
notepadEntry = ["Murder Scene", "Victim"]
area = "0"
#Mira's Testimony(Theft), Lawrance, Father Merwin(VICTIM), Lawrance's Testimony, Father Cornealius's Testimony, Mira's Testimony on Merwin, Mira's Testimony on Father Cornealius, Mira's Testimony on Lawrance
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
				print("Notepad: Your notepad where you keep all your notes...")
				print("[View Notes?]")
				print("1. [Yes] \n2. [No]")
				notepadInput = input("")

				if(notepadInput == "1"):
					while(True):
						gendelsRock = "Gendel's Rock"
						if('notepadEntry[countNote] == "Murder Scene"'):
							entryDescription = ": Located in an alleyway in the center of the Coronian Market Place. A very busy place, someone must've seen something."
						if('notepadEntry[countNote] == "Victim"'):
							entryDescription = ": Male. Not much is known about the victim except the left side of his face is burnt. He wore typical undergarment when found. He had nothing on him."
						if('notepadEntry[countNote] == "Gendel the Blacksmith"'):
							entryDescription = ": A dwarven blacksmith who works in the blacksmith store besides the alley where the body was found."
						if('notepadEntry[countNote] == "Gendels Rock"'):
							entryDescription = ": A family heirloom and a rather expensive piece of marble that Gendel claim was stolen around the day of the murder."
						if('notepadEntry[countNote] == "Gendels Testimony"'):
							entryDescription = ": Working in the forge and besides the furnance all day and night, he was no able to see or hear anything besides his store."
						if('notepadEntry[countNote] == "Handprint in Gendels"'):
							entryDescription = ": A strange handprint in the window of Gendel's storage closet. Too bad and too tall to be Gendel's."
						if('notepadEntry[countNote] == "Mira the General Shopkeeper"'):
							entryDescription = ": A small old lady who owns the general shop besides the alley where the body was found."
						if('notepadEntry[countNote] == "Eidar the Homeless"'):
							entryDescription = ": A homeless man who sneaked into Mira's basement earlier today."
						if('notepadEntry[countNote] == "The Basement"'):
							entryDescription = ": The basement normally locked had its locks broken before the night of the murder."
						if('notepadEntry[countNote] == "Miras Testimony"'):
							entryDescription = ": Did not see or hear anything while tending the store."
						if('notepadEntry[countNote] == "Miras Testimony(Theft)"'):
							entryDescription = ": While the store suffer no robbery, Mira claims she sees a young boy exiting Gendel's shop on the day of the murder."
						if('notepadEntry[countNote] == "Lawrance"'):
							entryDescription = ": A young boy who ran from his orphanage and shortly taken in by Father Cornealius but not an offically a church member."
						if('notepadEntry[countNote] == "Father Merwin(VICTIM)"'):
							entryDescription = ": The victim of the case. Burnt in the face but was killed upon repeated strikes to the head with a blunt object."
						if('notepadEntry[countNote] == "Lawrances Testimony"'):
							entryDescription = ": Did not see anything but was aware that there was a murder."
						if('notepadEntry[countNote] == "Father Cornealiuss Testimony"'):
							entryDescription = ": Claims no one stole from the church."
						if('notepadEntry[countNote] == "Miras Testimony on Merwin"'):
							entryDescription = ": Mira recalls Merwin as a young, ambitious and somewhat overzealous man. Perhaps a tad judgement to non-believers."
						if('notepadEntry[countNote] == "Miras Testimony on Father Cornealius"'):
							entryDescription = ": Mira recalls Father Cornealius spending a great deal of time with a young lady a decade ago."
						if('notepadEntry[countNote] == "Miras Testimony on Lawrance"'):
							entryDescription = ": Mira recalls several rumors about Lawrance being kicked out of his orphanage as a troubled youth. "

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
				print("Loose Brick: A loose brick found in the walls of the alleyway. Perhaps it might be useful for something...")
				print("_________________________________")
			if(nextInput == "White Solid Substance" or nextInput == "white solid substance"):
				print("White Solid Substance: Strange bits of a white solid substance was found in the alleyway")
				print("_________________________________")
			if(nextInput == "Mysterious Black Robe" or nextInput == "mysterious black robe"):
				print("Mysterious Black Robe: A mysterious set of black robes found stashed in the basement. Found and given by Eidar.")
				print("_________________________________")
			if(nextInput == "Priest Robe" or nextInput == "priest robe"):
				print("Priest Robe: A set of priest robes that was found by Eidar in Miras basement.")
				print("_________________________________")
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
		print("Welcome to An Insignificant Tale \n Type in a number to proceed \n 1. Start \n 2. Quit")
		userInput = input("")

		if(userInput == "1"):
			area = "1"
		elif(userInput == "2"):
			break
#Might need to initilize boolean here
	if(area == "1"):
		secondVisitHome = False
		investigateEnd = False
		genStoreSecondVisit = False
		#Enter player name
		print("What is your name?")
		name = input("")
		#Need to ask professor about function regarding time delays
		#And probably something about text wraps
		print("Greetings, " + name + " \nYou were once a citizen in a city named Corona, \nwhich is the capital of a massive alliance...but none of that really matter")
		print("Following the footstep of your father you decided to become a city guard.")
		print("This isn't a tale of grandeur or famous battle...")
		print("At least the pay is good and less life threatening")

		area = "2"
		#The game begins and move towards its first scene

#_____________________PLAYER HOME, AREA IS 2, __________________________
	if(area == "2" and secondVisitHome == False):
		print("____________________________________________")
		hidHomeDialogue = 0
		#Player home
		print(name + "'s House")
		print("[You hear the call of a rooster.]")
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
			print("[There's a man in tattered clothing standing in your doorway]")
			print("Messenger: Good morning Mr. " + name + "!")
			print("1. 'Who are you?' \n2. 'Good morning' \n3. [Close the Door]")
			messengerResp = input("")
			dialogueA1 = areaOne(messengerResp)

		if(playerResp == "2"):
			dialogueA1 = areaOne("3")

#------------------------DIALOGUE A1---------------------------------
		if(dialogueA1 == 1):
				print("'I'm the morning messenger sir. I am suppose to wake you this morning'")
				print(name + ": 'Ah right.'")
				print("1.'Good morning' \n2.[Close the Door]")
				messengerResp2 = input("")
				if(messengerResp2 == "2"):
					dialogueA1 = areaOne("3")
				elif(messengerResp2 == "1"):
					dialogueA1 = areaOne("2")

		if(dialogueA1 == 2):
				print("Morning Messenger:'Morning sir, now that I've woke you, I must wake the others.'")
				print("[The tattered man ran down the street and continue knocking on doors]")

		if(dialogueA1 == 3):
				print("'Mr. " + name + " you need to wake up! It's dawn!'")
				print("[Finally, you got up and answered the door]")
				print(name + ": '...Morning'")
				print("Morning Messenger:'Morning sir, now that I've woke you, I must wake the others.'")
				print("[The tattered man ran down the street and continue knocking on doors]")
#--------------------------------------------------------------------
		print("Today is your first day on the job.")
		print("Your partner awaits you in the barrack.")
		print("Your first day as a city guard...just like your father.")
		print("You don the once proud red armor of your father,")
		print("a typical Coronian armor that has endured much.")
		print("And proceeded to the guard barrack.")
		area = "3"
	if(area == "2" and secondVisitHome == True):
		print("____________________________________________")
		print("[You've returned home and rest...]")
		print("[Next morning...]")
		print("[There's a knock on the door...]")
		print("Coleridge: 'Rookie wake up!'")
		print("[You got up to answer the door]")
		print("1. 'Come in Coleridge...' 2. 'What do you want?' 3. 'How did you know where I live?'")
		dialogueA2b = input("")

		if(dialogueA2b == "1"):
			print("Coleridge: 'Wow, thanks. Most people stop being people in the morning'")
			partnerRel = partnerRel + 5
		if(dialogueA2b == "2"):
			print("Coleridge: 'Well how do you do too sleepy head, you gonna invite me in?'")
			partnerRel = partnerRel - 3
		if(dialogueA2b == "3"):
			print("Coleridge: 'I'm your partner of course I know where you live.'")
			print(name + ": '...Alright'")

		print("[Coleridge enters the home on his own]")
		print("Coleridge: 'Small place, real cozy. Love it.'")
		print(name + ": 'Thanks but why?'")
		print("Coleridge: 'You're my partner I can't give you a visit?'")
		print(name + ": 'You're my partner, not my friend.'")
		print("Coleridge: 'Harsh but true. '")
		print(name + ": 'So, what is it Coleridge?'")
		print("Coleridge: 'You know that bald priest back at the church?'")
		print(name + ": 'Father Cornealius?'")
		if(cornealiusRobe == True):
			print("Coleridge: 'Yeah, he was down in the barrack hoping to see that corpse.'")
			print(name + ": 'Did you show it to him?'")
			print("Coleridge: 'Yeah but I had most of the face covered and just told him it was gruesome. He still manage to identify him.'")
			print(name + ": 'Okay, let me just change and we'll head down to the barracks. Is the father still there?'")
			print("Coleridge: 'No, he left after seeing the body, saying he needs a bit of time.'")
			print(name + ": 'Understandable, give me a sec..'")
		if(cornealiusRobe == False):
			print("Coleridge: 'Yeah he was in the barrack asking about the other priest, Father Merwin.'")
			print(name + ": 'Oh?'")
			print("Coleridge: 'Yeah, when Merwin didn't show up at the church again, Cornealius paid him a visit.'")
			print("Coleridge: 'Man's missing.'")
			print(name + ": 'A missing man, a murder and a theft all in the same week in the same area?'")
			print("Coleridge: 'I know, too weird to be coincendence, I took him down to the morgue on a hunch.'")
			print("Coleridge: 'It paid off, our victim, Merwin. I covered up the ugly parts, probably too much for the man but he still manage to identify him.'")
			print(name + ": 'Is Father Cornealius still there?'")
			print("Coleridge: 'No, he left awhile ago to grief.'")
			print(name + ": 'I see. Give me a sec, I need to change.'")
			print("Coleridge: 'Alright.'")
		print("-NOTES UPDATED: FATHER MERWIN(VICTIM)-")
		notepadEntry.remove("Father Merwin")
		notepadEntry.remove("Victim")
		notepadEntry.append("Father Merwin(Victim)")
		print(name + ": 'Now that we know who the victim is we have a better foothold on the investigation.'")
		print("Coleridge: 'I think it's safe to say whatever the hell happened began at that church.'")
		print(name + ": 'Alright well where do we begin now?'")
		print("Coleridge: 'The general store.'")
		print(name + ": 'Really Coleridge?'")
		print("Coleridge: 'I'm serious just hear me out first.'")
		print(name + ": 'Okay, what?'")
		print("Coleridge: 'Yesterday, we asked Mira if she sees anything suspicious around but not in the church.'")
		print(name + ": 'She goes to the church?'")
		print("Coleridge: 'That's right. If there's something fishy about that church, Mira might know something.'")
		print(name + ": 'Alright, fine let's go then.'")
		print("Coleridge: 'Gladly.'")
		genStoreSecondVisit = True
		area = "6"
#______________________GUARD BARRACK, AREA IS 3,________________________
#Hidden Dialogue:Change the varaible that causes different if statement
	if(area == "3" and investigateEnd == False):
		print("____________________________________________")
		print("Coronian Guard Barrack")
		print("A large building with brick exterior and a wooden interior")
		print("Wooden tables and chairs lying around with racks of weapons and armors to the side")
		print("The barrck is already full of guards both on and off duty \ndoing different things ranging from playing cards to eating \ntheir breakfast around the tables.")
		print("You approach the captain of the barrack and salute")
		print("Captain Faust: 'Welcome " + name + ". We've been expecting you.'")
		print(name + ": 'Good morning captain.'")
		print("Captain Faust: 'Nervous about your first day?'")
		print("1. 'Not at all.' \n2. 'A little.' \n3. 'Very..'")
		dialogueA3a = input("")
		if(dialogueA3a == "1"):
			print("Captain Faust: 'Really? Good keep up that energy.'")
		elif(dialogueA3a == "2"):
			print("Captain Faust: 'That's to be expected. No worries.'")
		elif(dialogueA3a == "3"):
			print("Captain Faust: 'Hah! Don't worry son. We don't bite.'")

		print(name + ": 'Yes sir.'")
		print("Captain Faust: 'So. have you gotten a chance to meet your partner?'")
		print(name + ": 'No. I'm afraid not.'")
		print("Captain Faust: 'Well head on in.'")
		print("Captain Faust: 'His name is Adam Coleridge. Just look for him near the gambling table.'")
		print("1. 'Yes sir.' \n2. 'May I ask a few question?'")
		dialogueA3b = input("")
		if(dialogueA3b == "2"):
				print("Captain Faust: 'Sure, anything to keep me from the paper work.'")
				while(True):
					print("1. 'What's my partner, Coleridge like?' \n2. 'So what's my duty?' \n3. 'Tell me about the city.' \n4. 'Tell me about the barrack' \n5. 'Nevermind.'")
					dialogueA3c = input("")
					if(dialogueA3c == "1"):
						print("Captain Faust: 'Coleridege eh? Well from a professional standpoint he's a good guard.'")
						print("Captain Faust: 'On a personal though, he can get a little rowdy.'")
						print("Captain Faust: 'One of those tough guys but he's a good mentor I assure you just don't ever gamble with him.'")
						print(name + ": 'Why?'")
						print("Captain Faust: 'He has a bit of a temper when he loses and he does...a lot.")
						print("Captain Faust: 'If he's betting on you on a deadpool")
						print("you can bet your ass you'll be untouchable.'")
						print("Captain Faust: 'Hahaha!'")
						print("Captain Faust: 'Well! Do you need anything else?'")
					if(dialogueA3c == "2"):
						print("Captain Faust: 'Duty eh?'")
						print("Captain Faust: 'What every guard does I suppose. Keep the peace. Simple enough right?'")
						print(name + ": 'I guess...'")
						print("Captain Faust: 'Don't worry. Coleridge will brief you.")
						print(name + ": 'Right.'")
						print("Captain Faust: 'Anything else?'")
					if(dialogueA3c == "3"):
						print("Captain Faust: 'The city? Didn't you grow up here?'")
						print(name + ": 'Yes, but in a guard's point of view I suppose.'")
						print("Captain Faust: 'I suppose there are things we know that a civilian doesn't'")
						print("Captain Faust: 'Well as you know, Corona is divided in to three sections.")
						print("Captain Faust: 'The nobles, the commoners and the slums.'")
						print("Captain Faust: 'Our station is mostly the commons, the market especially.'")
						print("Captain Faust: 'In fact, you and Coleridge will be patrolling the markets today.'")
						print("Captain Faust: 'The worst of the market is really just petty thief and the occasion shouting match between merchants.'")
						print("Captain Faust: 'That's all I can spare for now, but if you want to know more, I'm sure you can find more information in the archive.'")
						print(name + ": 'Okay, thank you captain.'")
						print("Captain Faust: 'No problem, anything else?'")
					if(dialogueA3c == "4"):
						print("Captain Faust: 'The barrack? What's to tell?'")
						print("Captain Faust: 'Well, let's see..")
						print("Captain Faust: 'The building is pretty old.")
						print("Captain Faust: 'The mess hall is where our commons are.'")
						print("Captain Faust: 'Most of the guards are gathered there when they're off duty.")
						print("Captain Faust: 'I'm not really strict about the rule.'")
						print("Captain Faust: 'I only ask that there's no drinking in the barrack for obvious reasons.'")
						print(name + ": 'Right.'")
						print("Captain Faust: 'That's all I have to say about the barrack. Anything else?'")
					if(dialogueA3c == "5"):
						print("Captain Faust: 'Alright. Fair enough.'")
						print("Captain Faust: 'Head on in, and find Coleridge.'")
						print(name + ": 'Yes captain.'")
						break


#--------------------------Starting Dialogue with Partner-------------

		print("You approach your new partner \nwho sits at one of the table piled with cards and coins")
		print("[BEWARE OF RESPONSE TO YOUR PARTNER]")
		print("A gruff, hairy looking man with a weary looking complexion \nbut clearly far too much energy for gambling looks up at you.")
		print("Coleridge: 'What are you looking at?'")
		print("1. 'Good morning! I'm your partner!' \n2. 'I'm your new partner.' \n3. 'Dumbass, I'm your new partner.'")
		dialogueA3d = input("")
#------------------DIALOGUE A3D---------------------------------------
		if(dialogueA3d == "1"):
			print("Coleridge: '..You're kidding me..'")
			print(name + ": 'I'm not.'")
			print("Coleridge: 'Aw god...'")
			print(name + ": 'Is there a problem?'")
			print("Coleridge: 'No, no, absolute not. It's just..too early in the morning for rainbows and sunshine.")
			partnerRel = 3

		elif(dialogueA3d == "2"):
			print("[The man looks up and down inspecting you]")
			print("Coleridge: 'Alright..fair enough, you look competent enough.'")
			print(name + ": 'Fair enough. It's nice to meet you.'")
			partnerRel = 5

		elif(dialogueA3d == "3"):
			print("The man slowly stands up ")
			print("The other guards around the gambling table stops")
			print("Coleridge: 'New partner huh...'")
			print("Coleridge gives you a fake smile")
			print("Coleridge: 'Nice to meet you too..smart-ass'")
			parnterRel = 0
#------------------END DIALOGUE FOR AREA 3 FIRST VISIT----------------
		print("Coleridge: 'Name's Coleridge...'")
		print(name + ": 'Yeah, I know. Captain Faust introduced you already.'")
		print(name + ": 'My name's " + name + ".'")
		print("Coleridge: 'Okay, alright. Well, seems like you're all ready to go.'")
		print(name + ": 'Yeah.'")
		print("Coleridge: 'Have you got a bag yet?'")
		print(name + ": 'Uh..bag?'")
		print("Coleridge: 'Yeah. All of us get a bag, to carry stuff just in case.'")
		print("[Coleridge tosses an empty brown bag at you.]")
		print(name + ": 'Uh..thanks.'")
		area = "4"
		hidBarrackDialogue = 0
#-----------------SECOND VISIT TO THE BARRACKS-------------------------
	if(area == "3" and investigateEnd == True):
		print("____________________________________________")
		print("[You and Coleridge returns to see Captain Faust waiting]")
		print(name + ": 'Captain.'")
		print("Captain Faust: 'Ah, you've return. Scholar William awaits downstairs.")
		print(name + ": 'Best not keep him waiting.'")
		print("Captain Faust: Agreed.")
		print("[The three of you head downstairs]")
		print("Scholar William: 'Ah good you've returned.'")
		print("Scholar William: 'Let's not waste anytime than.'")
		print("Coleridge: 'Yeah, my shift is almost over.'")
		print("Scholar William: 'Come around then.'")
		print("[Everyone gather around the table with the dead body]")
		print("Scholar William: 'As you can see something burnt the man's face but that's not what killed him.'")
		print("Coleridge: 'Could've fooled me.'")
		print("Scholar William: 'I'm sure many things can Mr.Coleridge.'")
		print("Scholar William: 'Anyway, the man had his head beaten in.'")
		print("Coleridge: 'So someone hit him in the head with a flaming hammer? How does this not scream magic?'")
		print("Scholar William: 'It isn't so much a single strike more of a repeated one.'")
		print("Scholar William: 'The flame wasn't particularly intense but the constant strikes would've burnt the man's face pretty heavily.'")
		print("Scholar William: 'Good news for the lad though, he was dead before he was burnt.'")
		print("Scholar William: 'Bad news, he probably felt most of the blows before he dies.'")
		print("Coleridge: 'Sounds like he really pissed someone off.'")
		print(name + ": 'Well thank you Scholar William.'")
		print("Scholar William: 'Uh-huh. Happy to come in at look at dead people.'")
		print("Scholar William: 'Captain Faust.'")
		print("[Scholar William takes a bow towards the captain and exits]")
		print("Captain Faust: 'So hows the investigation?'")
		print(name + ": 'We're making some progress.'")
		print("Coleridge: 'I think that's debatable.'")
		print("Captain Faust: 'Well I'm sure you two have done plenty and are exhausted.'")
		print("Captain Faust: 'Head home and get a fresh start tomorrow.'")
		print(name + ": 'Yes captain.'")
		print("Coleridge: 'Finally!'")
		secondVisitHome = True
		area = "2"
	if(area == "3.2"):
		print("____________________________________________")
		print("Corona Barack: Basement/Morgue")
		print("[The guards lay the body on the wooden table]")
		print("[Captain Faust, you, and Coleridge surround the body]")
		print("[A bald man with a goatee in green and golden colored robe enter]")
		print("Captain Faust: 'Scholar Will. Welcome back.'")
		print("Scholar Will: 'Considering everytime I return I have to look at a dead body I'd keep your welcome to yourself captain.")
		print("Captain Faust: 'Right. Well " + name + ", This is Scholar William.'")
		print("Captain Faust: 'He's a professor at the university nearby and whenever we find a dead body we call him down to examine them.'")
		print("Scholar William: 'You're new I presume?")
		print("1. 'Yes I am, nice to meet you.' \n2. 'Mhm..' \n3. 'No shit Sherlock'")
		dialogueA3e = input("")

		if(dialogueA3e == "1"):
			print("Scholar William: 'Good to see manner here. He's a keeper Faust.'")
			print("[Captain Faust nods on with pride]")
		if(dialogueA3e == "2"):
			print("Scholar William: 'Eh...Alright.'")
		if(dialogueA3e == "3"):
			print("Scholar William: 'Ah, that respond reminds me of when I first met Mr.Coleridge.'")
			print("[Coleridge walks over patting your back.]")
			print("Coleridge: 'What can I say? I teach them well.'")
			print("[Captain Faust stands there shaking his head]")
			partnerRel = partnerRel + 5

		print("[The Scholar begin examining the body]")
		print("Scholar William: 'Let's go over the obvious first shall we?'")
		print("Scholar William: 'Obviously, something hot hit him in the face.'")
		print("Scholar William: 'Pretty bad burns too.'")
		print("Scholar William: 'Either something very very hot hit him right in the face..'")
		print("Scholar William: 'Or something hot just stay on his face for a little while.'")
		print("Scholar William: 'I'll need a little more time to examine him in detail.")
		print("Scholar William: 'Come back in say an hour or so?")
		print("Captain Faust: 'Alright then. The two of you should begin your investigation.'")
		print(name + ": 'Yes sir!'")
		print("Coleridge: 'Fine...'")
		area = "100"
#---------------------------AREA 4 CORONA MARKET-----------------------
	if(area == "4"):
		print("____________________________________________")
		print("Coronian Market, the area is bustling except for the occasional alley...")
		print("You're walking around with your partner")
		print("You notice something in the alley")
		print(name + ": 'Coleridge, stop. There's something over there.'")
		print("Coleridge: 'Huh? What?'")
		print("[Coleridge takes a sip from his alcohol bottle]")
		print(name + ": 'Really?'")
		print("Coleridge: 'Captain said I can't drink in the barrack. Never said anything about patrol.'")
#----------------------FIRST EVENT - BODY IS FOUND----------------------
		print("1. [Go check it out] \n2. [Keep walking]")
		playerA4R1 = input("")

		if(playerA4R1 == "2"):
			print("Coleridge: 'You smell something burning?'")
			print(name + ": 'A little. Yeah.'")
			print("Coleridge: 'Cmon kid. Let's check it out.'")
			print("[Your partner walk down the alley]")
			print("[You slowly follow him]")

		print("[There's a man with his back towards you and Coleridge leaning against the garbage can in the middle of the alley.]")
		print("Coleridge: 'Hey man! Get outta there!'")
		print("Coleridge: 'There's no scrap for you in there!'")
		print("[No response]")
		print(name + ": 'Sir?'")

		print("1. [Turn him over] \n2. [Leave him be]" )
		playerA4R2 = input("")

		if(playerA4R2 == "1"):
			print("[You turn the man over]")

		if(playerA4R2 == "2"):
			print("Coleridge: 'Nah kid. This is our district and its our job to keep these bums out of our garbage.'")
			print(name + "'That's kind of harsh...'")
			print("[He turns the man over]")

		print("[He slums down, dead with the right side of his face black and melted like]")
		print("[Coleridge backs away cringing slightly]")
		print(name + ": 'He's dead.'")
		print("Coleridge: 'No shit kid. Talk about a face only a mother could love...'")
		print("[You begin examining the body]")

		while(True):
			print("1. [Examine the face] \n2. [Check his clothing] \n3. [Finish] ")
			playerA4R3 = input("")

			if(playerA4R3 == "1"):
				print("[His face is black and melted like. It seems like a pretty bad burnt]")
			if(playerA4R3 == "2"):
				print("[He's wearing basic inner clothes. There's no pockets.]")
			if(playerA4R3 == "3"):
				break

		print("[You turn to your partners and sees him walking away.]")
		print(name + ": 'Coleridge! What are you doing?'")
		print("Coleridge: 'What do you think? I'm calling it into the mage guild.'")
		print(name + ": 'Mage guild? Why?'")
		print("Coleridge: 'His face says magic all over it.'")
		print(name + ": 'You didn't even look at it. What if it isn't?'")
		print("Coleridge: 'Well, the mage guild can come check it out.")
		print("Coleridge: 'If it isn't magic then someone hopefully not our shift will investigate it.'")
		print(name + ": 'We found him. He's our responsibility.'")
		print("[Coleridge let out a sigh]")
		print("Coleridge: 'Alright..alright fine but we still got to call it in anyway...'")
		print("[Coleridge walks off..]")
#----------------------------------------------------------------------
		print("[The area is swarmming with guards and mages]")
		print("[You stand besides your partner looking over the body with several other guards and mages]")
		print("[Captain Faust approaches]")
		print("Captain Faust: 'First day and already a body.'")
		print("Captain Faust: 'Don't know if you're cursed or blessed.'")
		print(name + ": 'Captain Faust!'")
		print("[You salute the captain]")
		print("Captain Faust: 'What do you have " + name + "?'")
		print(name + ": 'Male body. Burnt on the face.'")
		print(name + ": 'We're still waiting on the mages to tell us if its magic.'")
		print("Captain Faust: 'I see.'")
		print("Mage: 'Its not magic in origin. Just fire.'")
		print("Coleridge: 'God dammit!'")
		print("[Coleridge swings his alcohol bottle up in to the air]")
		print("Captain Faust: 'Coleridge! Are you drinking on patrol?!'")
		print("[Coleridge notices the captain for the first time and hides the bottle behind his back]")
		print("Coleridge: 'Oh heh! Heya cap'n. When did you get here?'")
		print("[Faust narrows his eyes at Coleridge then turn back to you.]")
		print("[Coleridge walks up and join the conversation as the mages begin to leave]")
		print("Captain Faust: 'Well since it isn't magic in origin..this is our case. Its your choice " + name + ".")
		print("Captain Faust: 'Do you want to investigate this or not?'")
		print("Coleridge: 'Why does he get to decide? I'm the senior g-'")
		print("Captain Faust: 'Because we all know your answer Coleridge.'")
		print("Captain Faust: 'Its your first day so I won't hold it against you. Your call.'")
		print(name + ": 'Of course sir. We found him, he's our responsibility.'")
		print("Coleridge: 'Ours?'")
		print("Captain Faust: 'Than its decided. We're taking the body back to the barrack for inspection. Get going you two.'")
		print(name + ": 'Yes sir!'")
		print("Coleridge: 'Fine captain..'")
		print("Captain Faust: 'Coleridge! Go help the other carry the body back!'")
		print("Coleridge: 'But cap'n I...Ah fine!'")
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
		print("____________________________________________")
		print("[You and Coleridge return to the market where part of the area including the alley is sealed off by guards]")
		print("[A guard stands in front of the alleyway]")
		print("Guard: 'You must be " + name + " and Coleridge...'")
		print(name + ": 'That's right.'")
		print("Guard: 'We've been expecting you. Go ahead in. If you're done investigating talk to me.'")
		print(name + ": 'Got it. Thank you.'")
		print("[You and Coleridge proceeded in to the alleyway]")
		print("-BEGIN INVESTIGATION-")
		print("Coleridge: 'Remember kid, if you found any evidence you can put them in your bag.'")
		print(name + ": 'Right...I should start taking notes and keep them in my bag as well...'")
		print("-NOTES UPDATED: MURDER SCENE-")
		print("-NOTES UPDATED: VICTIM-")
		print("-TO ACCESS YOUR INVENTORY, TYPE 'i' OR 'inventory' DURING INVESTIGATION OR INTERROGATION-")
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
						print("Coleridge: 'What do I think? It's a garbage can! What do I think...'")
					if(playerInv1a == "2"):
						print("[You lifted the lit and inspect it from top to bottem]")
						print("[Its clean...or rather there's nothing suspicious about it...]")
					if(playerInv1a == "3"):
						print("[You walk around the can looking around the alleyway]")
						print("Only a few pieces of garbage lying around...nothing relevant it seems")
					if(playerInv1a == "4"):
						print("[You lift the can and look at the bottem...]")
						print("[Nothing but more garbage..]")
					if(playerInv1a == "5"):
						break
			if(playerInv1 == "2"):
				print("You look around the alley...")
				print("[Nothing seems out of the ordinary...]")
				while(True):
					print("1. [Consult Coleridge] \n2. [Examine the walls] \n3. [Check the ground] \n4. [Back]")
					playerInv1b = input("")
					inventoryAccess(playerInv1a)

					if(playerInv1b == "1"):
						print(name + ": 'Anything Coleridge?'")
						print("Coleridge: 'Well you gotta praise the guy. He's either desperate or brilliant...'")
						print(name + ": 'What makes you say that?'")
						print("Coleridge: 'He dumped a body in an alley surrounded by a crowded market...")
						print("Coleridge: 'Not to mention this is a pretty frequent patrol route.'")
						print(name + ": 'Do you think he'd leave a witness?'")
						print("Coleridge: 'Does a dog have legs?'")
					if(playerInv1b == "2"):
						print("[You look around the brick wall of the alley...]")
						print("[You feel around the wall and there seems to be a loose brick..]")
						print("[Maybe this will come in handy...]")
						print("-INVENTORY UPDATED: LOOSE BRICK-")
						invArray.insert(1, "Loose Brick")
						print("Coleridge: 'Really? A brick?'")
					if(playerInv1b == "3"):
						print("[You examine the ground ]")
						print("[More garbge..]")
						print(name + ": 'Hm...what's this?'")
						print("[There's bits of a solid white substance near the garbage can...]")
						print("Coleridge: 'What the hell is that?'")
						print(name + ": 'Don't know. Best get it back to Scholar William.")
						print("[You place the substance inside a smaller clean bag...]")
						print("-INVENTORY UPDATED: WHITE SOLID SUBSTANCE-")
						invArray.insert(1, "White Solid Substance")
					if(playerInv1b == "4"):
						break
			if(playerInv1 == "3"):
				print("[You approach the guard...]")
				print("Guard: 'Are you ready to go?'")
				print("1. 'I have some questions...' \n2. 'Yeah, I'm ready to leave'")
				playerInv2 = input("")

				if(playerInv2 == "1"):
					print("Guard: 'Of course.'")
					while(True):
						print("1. 'Was there any witness?' \n2. 'Tell me about the area...' \n3. 'That's it, thank you.'")
						playerInv2a = input("")

						if(playerInv2a == "1"):
							print("Guard: 'There was a few who saw people going in and out of the alley'")
							print("Guard: 'But I'm afraid there's nothing concrete.'")
							print("Guard: 'As crowded as the area is, the place is too busy for anyone to look at some alley.'")
							print(name + ": 'Fair enough.'")
							print("Guard: 'Anything else?'")
						if(playerInv2a == "2"):
							print("Guard: 'The market is usually crowded.'")
							print("Guard: 'The buildings besides the alleyway is a blacksmith and a general store'")
							print("Guard: 'The alley itself leads into the church courtyard'")
							print(name + ": 'Thank you. I guess we'll start with those areas then.")
							print("[The guard nods.]")
							print("-NEW LOCATION: BLACKSMITH")
							print("-NEW LOCATION: GENERAL STORE")
							print("-NEW LOCATION: CHURCH")
							smithDialogue = 1
							genDialogue = 1
							churchDialogue = 1
							print("Guard: 'Anything else?'")
						if(playerInv2a == "3"):
							print("Guard: 'You're welcome.'")
							break

				if(playerInv2a == "2"):
					print("Guard: 'Are you sure?'")
					print("-WARNING: ONCE YOU LEAVE THE AREA ALL NON-COLLECTED EVIDENCE AND WITNESSES WILL BE GONE-")
					print("1. 'Yes' \n2. 'No'")
					playerInvExit = input("")

					if(playerInvExit == "1"):
						print("Guard: 'Okay. Take care...'")
						area = "100.1"

					if(playerInvExit == "2"):
						print(name + ": 'On second though let me look around some more.'")
						print("Guard: 'Very well.'")
#------------------------AREA 5 BLACKSMITH------------------------------
	if(area == "5"):
		print("____________________________________________")
		blacksmith = True
		print("[With Coleridge following shortly behind you, you walked into the blacksmith besides the alleyway]")
		print("[You knocked on the door]")
		print("[You can hear the sound of hot steel going into cool water]")
		print("[The door creaks opens on its own...]")
		print("[You see the stout dwarven blacksmith who is holding a hot blade in his hand]")
		print("1.[Tap Him on the Shoulder] \n2. [Come Back Later]")
		dialogueA5a1 = input("")

		if(dialogueA5a == "1"):
			print(name + ": 'Excuse me sir.'")
		if(dialogueA5a == "2"):
			print(name + ": 'We'll just..come back later.")
			print("Coleridge: 'That's just a waste of time.'")
			print("[Coleridge walks up to the blacksmith and reaches for him]")
			print(name + ": 'I don't think that's a good id-'")
#-----------------------------DIALOGUE A5A CONTINUE----------------------
		print("Blacksmith: 'Thief!'")
		print("[The dwarf quickly turns aiming the heated blade towards you and Coleridge.]")
		print("Coleridge: 'Holy hell! What the-'")
		print(name + ": 'Calm down sir! We're city guards!'")
		print("Blacksmith: 'Oh! Hahah! Sorry, sorry my bad.'")
		print("Coleridge: 'The hell is wrong with you dwarf? We knocked before coming in!'")
		print("Blacksmith: 'Yer did? I'm sorry I miss a lot what with the furnance blasting all day.")
		print("Blacksmith: 'I can't hear a damn dragon roaring behind me with the damn thing.")
		print("...And yet Coleridge and I hear each other perfectly fine.")
		print("[He gesture towards the furnance besides him and turns it off. The blacksmith quiet downs.]")
		print("[He drops the blade into the water and steam bubbles out of the water.]")
		print("Blacksmith: 'Are ye here bout my lost trinkets?'")
		print(name + ": 'Uhm...lost trinket Mr...?'")
		print("Blacksmith: 'Name's Gendel.")
		print(name + ": 'Right, Mr.Gendel.'")
		print("Gendel: 'Please just Gendel. Sounds old calling me Mr. Gendel.'")
		print("Coleridge: '..And how old are you?'")
		print("Gendel: 'Why I just turn twenty-three last month!'")
		print("[Both you and your partner looks down at the dwarf with a large beer belly and brown beard reach down to his belt]")
		print("Coleridge: 'Uh huh.'")
		print("-NOTES UPDATED: GENDEL THE BLACKSMITH-")
		notepadEntry.append("Gendel the Blacksmith")
		#ADD GENDEL THE BLACKSMITH TO LIST OF JOURNAL ENTRY + ADD TO ARRAY
		print("Gendel: 'Anyway why don't you two take a seat? Here!'")
		print("[He places two dwarven stool in front of you and Coleridge...]")
		print("[You and Coleridge stares at each other and he shrugs.]")
		print(name + ": 'No thank you. We're only here briefly.'")
		print("Coleridge: 'Pass I've been sitting on my ass all day.'")
		print("Gendel: 'Aye. Suit yourself.'")
		print("[Gendel kicks the stool aside and looks up at you]")
		print("Gendel: 'So, what can I do for the boys in red?'")
		print("-INTERVIEW BEGIN-")
		gendelInterview = True
#-------------------AREA 5 INTERVIEW: GENDEL THE BLACKSMITH--------------
		while(gendelInterview == True):
			print("You may access inventory during interviews")
			print("1. [Ask him about the stolen trinket] \n2. [Ask about the case] \n3. [Look around the shop] \n4. [Done]")
			interviewA5a == input("")
			inventoryAccess(interviewA5a)

			if(interviewA5a == "1"):
				print(name + ": 'So you were talking about something being stolen from you?'")
				print("Gendel: 'Uh yeah.'")
				print(name + ": 'Well...What was stolen?'")
				print("[The dwarf is spacing out...]")
				print(name + ": 'What was stolen from you Gendel?'")
				print("[Coleridge let out a sigh]")
				print("Coleridge: 'This dwarf is so drunk. Hey Gendel! Wake up!'")
				print("Gendel: 'Huh?! Oh! Right! I lost my rock!'")
				print(name + ": 'I'm sorry, your rock?")
				print("Coleridge: 'That's it. He's drunk.'")
				print("Gendel : 'I assure you I am not drunk. I'm an angry drunk!'")
				print("Coleridge: 'And...you're not angry right now?'")
				print(name + ": 'Nevermind that Coleridge.'")
				print(name + ": 'Was there something special about this rock?'")
				print("Gendel: 'Aye. It was a family heirloom. A big ol'chunk of marble.'")
				print("1. [Keep asking about the rock] \n2. [Return to the original topic]")
				interviewA5a1 == input("")

				if(interviewA5a1 == "1"):
					GendelRockDialogue = True
					print(name + ": 'So when did you lose this rock?'")
					print("Coleridge: 'You're kidding right? What does thi-'")
					print(name + ": 'Coleridge please.'")
					parnterRel = parnterRel - 1
					print("Gendel: 'Well, let's see, about yesterday afternoon.'")
					print("Gendel: 'I always rub the rock for good luck before I smith.'")
					print("Gendel: 'When I was working on a sword around lunch time I put it back in my bedroom but when I went to get it a few hours later it's gone.")
					print(name + ": 'And how valuable is this rock?'")
					print("Gendel: 'It's a family heirloom! It's priceless.'")
					print("Coleridge: 'He meant as in value dwarf.'")
					print("Gendel: 'Oh! About 50,000 coins!'")
					print("[Coleridge makes a choking sound]")
					print("Coleridge: Don't worry Gendel! We're on it!")
					partnerRel = partnerRel + 5
					print("[You give Coleridge a look]")
					print("Coleridge: 'What? It's a guard's duty to recover stolen things right?'")
					print("Gendel: 'I'd be very grateful if you find it!'")
					print(name + ": 'Very well. We'll do our best and keep an eye out.'")
					print("-NOTES UPDATED: GENDELS ROCK-")
					notepadEntry.append("Gendels Rock")
					print("Gendel: 'Now is there anything else?'")
			#gendelRockDialogue
			if(interviewA5a == "2"):
				gendelCaseDialogue = True
				print(name + ": 'So Gendel, were you aware that there was a murder besides your shop.'")
				print("Gendel: 'Uh...you mean people murder or animal murders?'")
				print("Coleridge: 'What? Why would we investigate animal murders?'")
				print("Gendel: 'Oh sorry...just lots of cats and mouse...'")
				print(name + ": 'It's people murder Gendel. A man was found in an alley besides your store.'")
				print("Gendel: 'Oh...that's bad.'")
				print("Coleridge: 'No shit. Now do you know anything or not?'")
				print("Gendel: 'Hm...Afraid not. I've been working the forge nonstop.")
				print("Gendel: 'I couldn't see anything muchless hear anything.'")
				print("Coleridge: 'This is a waste of time.'")
				print("Gendel: 'I'd offer whatever I can to help but I'm afraid I got nothing.'")
				print("-NOTES UPDATED: GENDELS TESTIMONY-")
				notepadEntry.append("Gendels Testimony")
				print("Gendel: 'Is there anything else?'")
			#gendelHandPrint
			if(interviewA5a == "3"):
				print(name + ": 'May I look around the store?'")
				print("Gendel: 'Go right ahead. You can buy a few things too if you like!'")
				gendelStore = True
				while(gendelStore == True):
					print("1. [Gendel's Bedroom] \n2. [The Forge] \n3. [Storage] \n4. [Living Room] \n5. [Done]")
					gendelStoreExplore = input(" ")

					if(gendelStoreExplore == "1"):
						print("[You proceed up the stairs behind the forge to a small humble little room.]")
						print("Sparesly furnitured and rather dusty. It appears Gendel doesn't spend much time here...")
					if(gendelStoreExplore == "2"):
						print("[You look at the large black furnance that sits in the middle of the room.]")
						print("[There are tools lying around the side but the center is suprisingly clean]")
					if(gendelStoreExplore == "3"):
						print("[You proceed to the back of the forge you find a small storage closet with a window. It's littered with weapons and tool.]")
						print(name + ": 'What's this?'")
						print("[The window is looking directly out in to the alley.]")
						print("[There's a handprint on the window that disturb some of the dust]")
						print("Strange...the handprint is too big to be Gendel's and the window is too tall anyway...")
						print("NOTES UPDATED: HANDPRINT IN GENDELS")
						notepadEntry.append("Handprint in Gendels")

						gendelHandPrint = True
					if(gendelStoreExplore == "4"):
						print("[You walked behind the forge to a small living room]")
						print("[A typical dining room. A single chair to the side, some kitchen utensil and a table in the center...]")
						print("Judging by the dust, it seems Gendel only use this room to cook.")
						print("He most likely does everything in the forge...")
					if(gendelStoreExplore == "5"):
						print(name + ": 'Thank you Gendel. Your home is lovely.'")
						print("Gendel: 'Thank you lad!'")
						gendelStore == False
			if(interviewA5a == "4"):
				print(name + ": 'Well thank you Gendel. We'll come back if we need anything else.")
				print("Gendel: 'Alright lads Let me know if you need anything else. From swords to armor! And please find me trinket.'")
				print(name + ": 'Will do Gendel.'")
				print("[Coleridge got up and gave a sigh. The two of you exit the blacksmith.]")
				gendelInterview = False
			print("Coleridge: 'That was a waste of time...'")
			if(gendelRockDialogue == True and gendelHandPrint == True):
				print(name + ": 'No it wasn't, we have a witness.'")
				print("Coleridge: 'Yeah a drunk dwarf'")
				print(name + ": 'No...someone else.'")
				print(name + ": 'I found a handprint on a window to the alley in Gendel's storage closet.'")
				print("Coleridge: 'So Gendel might have saw the murder?'")
				print(name + ": 'The hand is too big to be Gendel and the window is too tall.'")
				print(name + ": 'No I think it's someone else. You know how he said he lost his rock?")
				print("Coleridge: 'Oh I see. You think that someone broke in to steal his rock and might've witness the murder...'")
				print(name + ": 'Yeah but it's a stretch. We need to know when the murder takes place.")
				print("Coleridge: I'm impressed rookie.")
				partnerRel = parnterRel + 6
				print(name + ": 'Thanks.'")
			elif(gendelRockDialogue == True):
				print(name +  ": 'Perhaps. Still recovering Gendel's rock is part of our job.")
				print("Coleridge: 'Yeah...yes it is...'")
				print(name + ": 'Recover...Coleridge..recover'")
				print("Coleridge: 'Right, right. Recover...'")
			else:
				print(name + ": 'I suppose so. We'll figure it out.'")
				print("Coleridge: 'I don't care about that...'")
				print(name + ": 'Let's just move on.'")
				partnerRel = parnterRel - 2
			area = "100.1"
#---------------------AREA 6 GENERAL STORE-------------------------------
	if(area == "6" and genStoreSecondVisit == False):
		print("____________________________________________")
		genStore = True
		print("[You and Coleridge proceed to the general store]")
		print("Coleridge: 'Ah, I love coming to this place.'")
		print("Coleridge: 'Nothing like the sweet smell of random junk.'")
		print("Coleridge: 'I used to come here every week to look at what people left behind. Found some sweet stuff in this place.'")
		print(name + ": 'So this store is kind of like a pawn store?'")
		print("Coleridge: 'Basically. Let's head on in. I know the store owner.'")
		print(name + ": 'Okay..I suppose.'")
		print("[Coleridge head into the store ahead of you with enthusiasm]")
		print("[The interior of the store isn't all that big...]")
		print("[but the amount of random junks and item littered around makes the place looks like a market of its own...]")
		print("[Behind the counter stands an old jolly looking lady.]")
		print("Coleridge: 'Hey there Mira, how are you doing?'")
		print("Mira: Oh I'm well Coleridge. Is this your new partner?'")
		print(name + ": 'Nice to meet you ma'am I'm " + name + ".'")
		print(name + ": 'Ma'am we're short on time would you mind if we ask you some questions?'")
		print("Coleridge: '" + name + " where's your manner?'")
		print("Mira: 't's quite alright. I know all of you are busy. So ask away.'")
		print("[Coleridge begin wandering around the store looking at random items...")
		print("-NOTES UPDATED: MIRA THE GENERAL SHOPKEEPER-")
		notepadEntry.append("Mira the General Shopkeeper")
		print("-INTERVIEW BEGIN-")
		miraInterview = True
#-----------AREA 6 INTERVIEW: MIRA THE GENERAL SHOPKEEPER--------------
		while(miraInterview == True):
			if(blacksmith == False):
				print("You may access inventory during interview")
				print("1. [Ask her about the case] \n2. [Ask her about Coleridge] \n3. [Look around the shop] \n4. [Done]")
				interviewA6a = input("")
				inventoryAccess(interviewA6a)

				if(interviewA6a == "1"):
					print(name + ": 'So Mira, did you recently see anything or hear anything suspicious?'")
					print("Mira: 'Suspicious is hardly specific.'")
					print("Mira: 'Does this have something to do with why the guards and mages were crowding the streets earlier?'")
					print("Mira: 'Did something happen in the alley?'")
					print(name + ": 'Uh, yes ma'am. We found a dead body dumped in the alley.'")
					print("Mira: 'Oh dear...do you know who it was?'")
					print(name + ": 'Afraid not. We're trying to figure that out now.'")
					print("Mira: 'Hm...the alley. I'm afraid I don't know anything. The streets are crowded and noisy enoug.'")
					print(name + ": 'Of course.'")
					print("-NOTES UPDATED: MIRAS TESTIMONY-")
					notepadEntry.append("Miras Testimony")
				#miraColeridgeDialogue
				if(interviewA6a == "2"):
					print(name + ": 'May I ask you something unoffically?'")
					print("Mira: 'Is it about Coleridge?'")
					print(name + ": 'Uh, yes ma'am.'")
					miraColeridgeDialogue = True
					print("Mira: 'That's alright he's your partner ask away.'")
					print(name + ": 'How do you know Coleridge?'")
					print("Mira: 'Before I got this store, I was a caretaker. You can imagine where I'm going with this.'")
					print(name + ": 'Uh yes. Hard to imagine Coleridge as a kid.'")
					print("Mira: 'Hah. I can still imagine Coleridge as a boy..'")
				#genStore
				if(interviewA6a == "3"):
					print(name + ": 'May I look around your store ma'am.'")
					print("Mira: 'By all means. Go ahead.'")
					genStore = True
					while(genStore == True):
						print("1. [Upstair Rooms] \n2. [The Store] \n3. [Storage Closet] \n4. [Basement] \n5. [Done]")
						genStoreExplore = input("")
						inventoryAccess(genStoreExplore)

						if(genStoreExplore == "1"):
							print("[You walk up the stairs looking around...]")
							print("[There are several doorless attics room...]")
							print("[The rooms are mostly covered in old hays and crates]")
							print("[The windows upstairs looks down onto the alleyway and blacksmith across from the generla store...]")
							print("There's nothing here...")
						if(genStoreExplore == "2"):
							print("[The store is full across shelves with random assortment of junks and items.]")
							print("Coleridge: 'Hey kid. Does Mira know anything?'")
							print(name + ": 'Afraid not. I'm just looking around for clues.'")
							print("Coleridge: 'What did you expect to find here?'")
							print(name + ": 'Not sure...'")
							print("Coleridge: 'Well too bad...can I borrow 50 coins?'")
							print("Coleridge: 'I saw something I want and I'm short.'")
							print("1. 'Fine...' \n2. 'No'")
							interviewA6a1 = input("")

							if(interviewA6a1 == "1"):
								print(name + ": 'Fine...but pay me back.'")
								print("Coleridge: 'Haha! Thanks rookie. See ya!'")
								partnerRel = partnerRel - 3
								print("[Coleridge runs off happily]")
							if(interviewA6a2 == "2"):
								print(name + ": 'No.'")
								print("Coleridge: 'Please! Come on rookie!'")
								print(name + ": 'No way.'")
								print("Coleridge: 'Fine...I'll go find something I CAN get.'")
								parnterRel = parnterRel - 2
								print("[Coleridge walks off with a grim expression]")
						if(genStoreExplore == "3"):
							print("[You move across the store trimming through each closet]")
							print("[As expected, more items except covered in dust...]")
						if(genStoreExplore == "4"):
							print("[You walked to the back of the store in to the alleyway where the body was found...]")
							print("[There appears to be a trapdoor leaning towards the general store...]")
							print("[You return to Mira in the store front...]")
							print(name + ": 'Mira, I notice there's a trapdoor in the alleyway. Does that lead down to a basement?'")
							print("Mira: 'Oh yes, I use it as additional storage. Let me get the key for you...'")
							print(name + ": 'Key?'")
							print("Mira: 'Yes, I keep it locked.'")
							print(name + ": 'I didn't see any locks.'")
							print("Mira: 'Oh dear, I've always kept it locked...'")
							print(name + ": 'Alright, stay here. Coleridge! Come here!'")
							print("[You walked upto the basement door and pulls out your sword.]")
							print("[Coleridge follows shortly afterward]")
							print("Coleridge: 'What happened?'")
							print(name + ": 'Mira said she keeps her basement locked.'")
							print("[You point to the broken lock on the ground]")
							print("Coleridge: 'Ah shit. And I thought I wouldn't have to do any actual work today.'")
							print("[Coleridge pulls his sword out as well.]")
							print(name + ": 'You want me to go in first?'")
							print("Coleridge: 'Nah you're still a rookie let me head in first.'")
							print("[Coleridge kick the basement door open and ran in.]")
							print("Coleridge: 'Corona Guards! Anyone here?'")
							print("[A ragged bearded man burst out of his blanket in the corner of the basement]")
							print("Old Man: 'D-Don't hurt me!'")
							print("[You and Coleridge both sheath your swords.]")
							print(name + ": 'Sir we have a few question for you..'")
							print("Old Man: 'A-Am I going to be thrown into the dungeon?'")
							print("Coleridge: 'Probably.'")
							print(name + ": 'Ignore him...Sir we just like to ask you a few things.'")
							print("[The old man gives a silent nod]")
							print("-INTERVIEW BEGIN-")
							
							eidarInterview = True

							while(eidarInterview == True):
								print("1. [Ask about personal information] \n2.[Ask about the basement] \n3.[Ask about the case] \n4.[Done]")
								interviewA6b = input("")

								if(interviewA6b == "1"):
									print(name + ": 'Sir, what's your name?'")
									print("Homeless Man: 'Uh...E-Eidar.'")
									print("-NOTES UPDATED: EIDAR THE HOMELESS-")
									notepadEntry.append("Eidar the Homeless")
									print(name + ": 'What are you doing here Mr.Eidar. There are shelters you can goto no?'")
									print("Eidar: 'I did but...they do not have much rooms and their condition are terrible...'")
									print("Coleridge: 'For a homeless guy you certainly speak well.'")
									print("[Eidar gave a long sigh]")
									print("Eidar: 'It maybe hard to believe but I wasn't born homeless Mr.Guard.'")
									print("Eidar: But as I was saying, the conditions in the shelter have been on a decline since the death of King Ulthas.'")
									print("Eidar: Now that damn Red Tyrant's been sinking all of the money in to whatever sick twisted thing that boy likes.'")
									print(name + ": 'You don't seem too happy with the king?'")
									print("Eidar: 'Is anyone? He's called the Red Tyrant for a reason but enough rant of an old man.'")
									print("Eidar: 'I'm sure you're here for something else...'")
								if(interviewA6b == "2"):
									print(name + ": 'So Eidar, how did you get in here?'")
									print("Eidar: 'What do you mean how I got in here?'")
									print(name + ": 'The door was locked but someone broke the lock. The owner didn't even realize till now.'")
									print("Eidar: 'I don't know. I saw this place was open so I took shelter here for a while.'")
									print(name + ": 'And when did you come in here?'")
									print("Eidar: 'Last night. Around nine I think.'")
									print("-NOTES UPDATED: THE BASEMENT-")
								if(interviewA6b == "3"):
									print(name + ": 'Did you see anyone entering or exiting the basement before you?'")
							
									print("Eidar: 'Nobody except you two.'")
									
									print(name + ": 'Did you hear anything?'")
									
									print("Eidar: 'Not particularly, this basement is really sound proof. Best night of sleep I've had in years.'")
									
									print("Eidar: 'Why are you asking these questions anyway'")
									
									print(name + ": 'Someone was recently murdered around here.'")
									
									print("Eidar: 'Should I be suprise or concern?'")
									
									print(name + ": 'I wouldn't know sir but if you have anymore informat-...'")
									
									print("Eidar: 'Yeah, yeah.'")
								if(interviewA6b == "4"):
									print(name + ": 'Well thank you Eidar.'")
									
									print("Eidar: 'Sorry I can't help you....well'")
									
									print(name + ": 'Is there something else?'")
									
									print("Eidar: 'I did find something here but...'")
									
									print(name + ": 'Yes?'")
									
									print("Eidar: 'Well I would like to have it back.'")
									
									print("Coleridge: 'We should just throw this guy in the dungeon and throw all his stuff.'")
									
									print(name + ": 'Coleridge please...I'll return it when I'm done with it Eidar, I promise.'")
									
									print("Eidar: 'Alright. You got a trustworthy face kid.'")
									
									print("[Eidar puls out a black robe from his blanket...]")
									
									print(name + ": 'What's this?'")
									
									print("Eidar: 'Some robe I found stuffed in to the corner here. If you ask me someone tried to hide this.'")
									
									print(name + ": 'Coleridge can you ask if this belongs to Mira?'")
									
									print("Coleridge: 'Sure...'")
									
									print(name + ": 'We'll return it to you as soon as we can.'")
									
									print("Eidar: 'Mhm. Okay.'")
									
									print("-INVENTORY UPDATED: MYSTERIOUS BLACK ROBE-")
									invArray.append("Mysterious Black Robe")
									eidarInterviewed = True
									eidarInterview = False

							print(name + ": 'Can you show me where you found the robe?'")
							
							print("[Eidar point over to the corner of the barely lit basement]")
							
							print("[You begin analyzing the area...]")
							
							print("[It's clear this place have been touched recently...the dust here is not as much]")
							
							print("[There isn't anything else here though..]")
							
							print("Coleridge: 'It's not Miras.'")
							
							print(name + ": 'Thank you Eidar.'")
							
							print("Eidar: 'Uh-huh.'")
							
							print("[You and Coleridge return to the general store]")
							
							print("[Mira walks out of the kitchen with a tub of water.]")
							
							print("Coleridge: 'Mira, what are you doing.'")
							
							print("Mira: 'There's a homeless man living below my shop yes?'")
							
							print("Coleridge: 'Yea, so?'")
							
							print("Mira: 'Well I'm taking this to him so he can clean himself up.'")
							
							print("[Mira walk out towards her basement with the tub of water]")
							
							print("Coleridge: Wha-...")
							
							print(name + ": 'Hah. What a lady.'")
							
							print("[Coleridge gave a shrug.]")
							
							print("[Mira continues to carry items back and fourth until she finally settles back down behind her counter]")
						if(genStoreExplore == "5"):
							print(name + ": 'Well thanks Mira. I got everything I need.'")
							
							print("Mira: 'Alright. Take care and watch over Coleridge for me.'")
							
							print(name + ": 'Will do ma'am.'")
							
							miraInterview = False
							break
				if(interviewA6a == "4"):
					print(name + ": 'Thank you for the information ma'am. I think I have all I need for now.'")
					
					print("Mira: 'You and Coleridge are welcome anytime.'")
					
					print("Mira: 'Please visit me again, offical business or not.'")
					
					print(name + ": 'We will ma'am. Thank you.'")
					miraInterview = False
			if(blacksmith == True):
				print("1. [Ask her about the case] \n2. [Ask her about Coleridge] \n3. [Look around the shop] \n4. [Ask about recent theft] \n5. [Done]")
				interviewA6a = input("")
				inventoryAccess(interviewA6a)

				if(interviewA6a == "1"):
					print(name + ": 'So Mira, did you recently see anything or hear anything suspicious?'")
					
					print("Mira: 'Suspicious is hardly specific.'")
					
					print("Mira: 'Does this have something to do with why the guards and mages were crowding the streets earlier?'")
					
					print("Mira: 'Did something happen in the alley?'")
					
					print(name + ": 'Uh, yes ma'am. We found a dead body dumped in the alley.'")
					
					print("Mira: 'Oh dear...do you know who it was?'")
					
					print(name + ": 'Afraid not. We're trying to figure that out now.'")
					
					print("Mira: 'Hm...the alley. I'm afraid I don't know anything. The streets are crowded and noisy enoug.'")
					
					print(name + ": 'Of course.'")
					
					print("-NOTES UPDATED: MIRAS TESTIMONY-")
					notepadEntry.append("Miras Testimony")
				#miraColeridgeDialogue
				if(interviewA6a == "2"):
					print(name + ": 'May I ask you something unoffically?'")
					
					print("Mira: 'Is it about Coleridge?'")
					
					print(name + ": 'Uh, yes ma'am.'")
					
					miraColeridgeDialogue = True
					print("Mira: 'That's alright he's your partner ask away.'")
					
					print(name + ": 'How do you know Coleridge?'")
					
					print("Mira: 'Before I got this store, I was a caretaker. You can imagine where I'm going with this.'")
					
					print(name + ": 'Uh yes. Hard to imagine Coleridge as a kid.'")
					
					print("Mira: 'Hah. I can still imagine Coleridge as a boy..'")
					
				#genStore
				if(interviewA6a == "3"):
					print(name + ": 'May I look around your store ma'am.'")
					
					print("Mira: 'By all means. Go ahead.'")
					genStore = True
					while(genStore == True):
						print("1. [Upstair Rooms] \n2. [The Store] \n3. [Storage Closet] \n4. [Basement] \n5. [Done]")
						genStoreExplore = input("")
						inventoryAccess(genStoreExplore)

						if(genStoreExplore == "1"):
							print("[You walk up the stairs looking around...]")
							
							print("[There are several doorless attics room...]")
							
							print("[The rooms are mostly covered in old hays and crates]")
							
							print("[The windows upstairs looks down onto the alleyway and blacksmith across from the generla store...]")
							
							print("There's nothing here...")
							
						if(genStoreExplore == "2"):
							print("[The store is full across shelves with random assortment of junks and items.]")
							
							print("Coleridge: 'Hey kid. Does Mira know anything?'")
							
							print(name + ": 'Afraid not. I'm just looking around for clues.'")
							
							print("Coleridge: 'What did you expect to find here?'")
							
							print(name + ": 'Not sure...'")
							
							print("Coleridge: 'Well too bad...can I borrow 50 coins?'")
							
							print("Coleridge: 'I saw something I want and I'm short.'")
							
							print("1. 'Fine...' \n2. 'No'")
							interviewA6a1 = input("")

							if(interviewA6a1 == "1"):
								print(name + ": 'Fine...but pay me back.'")
								
								print("Coleridge: 'Haha! Thanks rookie. See ya!'")
								
								partnerRel = partnerRel - 3
								print("[Coleridge runs off happily]")
							if(interviewA6a2 == "2"):
								print(name + ": 'No.'")
								
								print("Coleridge: 'Please! Come on rookie!'")
								
								print(name + ": 'No way.'")
								
								print("Coleridge: 'Fine...I'll go find something I CAN get.'")
								parnterRel = parnterRel - 2
								
								print("[Coleridge walks off with a grim expression]")
								
						if(genStoreExplore == "3"):
							print("[You move across the store trimming through each closet]")
							
							print("[As expected, more items except covered in dust...]")
							
						if(genStoreExplore == "4"):
							print("[You walked to the back of the store in to the alleyway where the body was found...]")
							
							print("[There appears to be a trapdoor leaning towards the general store...]")
							
							print("[You return to Mira in the store front...]")
							
							print(name + ": 'Mira, I notice there's a trapdoor in the alleyway. Does that lead down to a basement?'")
							
							print("Mira: 'Oh yes, I use it as additional storage. Let me get the key for you...'")
							
							print(name + ": 'Key?'")
							
							print("Mira: 'Yes, I keep it locked.'")
							
							print(name + ": 'I didn't see any locks.'")
							
							print("Mira: 'Oh dear, I've always kept it locked...'")
							
							print(name + ": 'Alright, stay here. Coleridge! Come here!'")
							
							print("[You walked upto the basement door and pulls out your sword.]")
							
							print("[Coleridge follows shortly afterward]")
							
							print("Coleridge: 'What happened?'")
							
							print(name + ": 'Mira said she keeps her basement locked.'")
							
							print("[You point to the broken lock on the ground]")
							
							print("Coleridge: 'Ah shit. And I thought I wouldn't have to do any actual work today.'")
							
							print("[Coleridge pulls his sword out as well.]")
							
							print(name + ": 'You want me to go in first?'")
							
							print("Coleridge: 'Nah you're still a rookie let me head in first.'")
							
							print("[Coleridge kick the basement door open and ran in.]")
							
							print("Coleridge: 'Corona Guards! Anyone here?'")
							
							print("[A ragged bearded man burst out of his blanket in the corner of the basement]")
							
							print("Old Man: 'D-Don't hurt me!'")
							
							print("[You and Coleridge both sheath your swords.]")
							
							print(name + ": 'Sir we have a few question for you..'")
							
							print("Old Man: 'A-Am I going to be thrown into the dungeon?'")
							
							print("Coleridge: 'Probably.'")
							
							print(name + ": 'Ignore him...Sir we just like to ask you a few things.'")
							
							print("[The old man gives a silent nod]")
							
							print("-INTERVIEW BEGIN-")
							
							eidarInterview = True

							while(eidarInterview == True):
								print("You may access inventory during interview")
								
								print("1. [Ask about personal information] \n2.[Ask about the basement] \n3.[Ask about the case] \n4.[Done]")
								interviewA6b = input("")
								inventoryAccess(interviewA6b)

								if(interviewA6b == "1"):
									print(name + ": 'Sir, what's your name?'")
									
									print("Homeless Man: 'Uh...E-Eidar.'")
									
									print("-NOTES UPDATED: EIDAR THE HOMELESS-")
									
									print(name + ": 'What are you doing here Mr.Eidar. There are shelters you can goto no?'")
									
									print("Eidar: 'I did but...they do not have much rooms and their condition are terrible...'")
									
									print("Coleridge: 'For a homeless guy you certainly speak well.'")
									
									print("[Eidar gave a long sigh]")
									
									print("Eidar: 'It maybe hard to believe but I wasn't born homeless Mr.Guard.'")
									
									print("Eidar: But as I was saying, the conditions in the shelter have been on a decline since the death of King Ulthas.'")
									
									print("Eidar: Now that damn Red Tyrant's been sinking all of the money in to whatever sick twisted thing that boy likes.'")
									
									print(name + ": 'You don't seem too happy with the king?'")
									
									print("Eidar: 'Is anyone? He's called the Red Tyrant for a reason but enough rant of an old man.'")
									
									print("Eidar: 'I'm sure you're here for something else...'")
								if(interviewA6b == "2"):
									print(name + ": 'So Eidar, how did you get in here?'")
									
									print("Eidar: 'What do you mean how I got in here?'")
									
									print(name + ": 'The door was locked but someone broke the lock. The owner didn't even realize till now.'")
									
									print("Eidar: 'I don't know. I saw this place was open so I took shelter here for a while.'")
									
									print(name + ": 'And when did you come in here?'")
									
									print("Eidar: 'Last night. Around nine I think.'")
									
								if(interviewA6b == "3"):
									print(name + ": 'Did you see anyone entering or exiting the basement before you?'")
									
									print("Eidar: 'Nobody except you two.'")
									
									print(name + ": 'Did you hear anything?'")
									
									print("Eidar: 'Not particularly, this basement is really sound proof. Best night of sleep I've had in years.'")
									
									print("Eidar: 'Why are you asking these questions anyway'")
									
									print(name + ": 'Someone was recently murdered around here.'")
									
									print("Eidar: 'Should I be suprise or concern?'")
									
									print(name + ": 'I wouldn't know sir but if you have anymore informat-...'")
									
									print("Eidar: 'Yeah, yeah.'")
								if(interviewA6b == "4"):
									print(name + ": 'Well thank you Eidar.'")
									
									print("Eidar: 'Sorry I can't help you....well'")
									
									print(name + ": 'Is there something else?'")
									
									print("Eidar: 'I did find something here but...'")
									
									print(name + ": 'Yes?'")
									
									print("Eidar: 'Well I would like to have it back.'")
									
									print("Coleridge: 'We should just throw this guy in the dungeon and throw all his stuff.'")
									
									print(name + ": 'Coleridge please...I'll return it when I'm done with it Eidar, I promise.'")
									
									print("Eidar: 'Alright. You got a trustworthy face kid.'")
									
									print("[Eidar puls out a black robe from his blanket...]")
									
									print(name + ": 'What's this?'")
									
									print("Eidar: 'Some robe I found stuffed in to the corner here. If you ask me someone tried to hide this.'")
									
									print(name + ": 'Coleridge can you ask if this belongs to Mira?'")
									
									print("Coleridge: 'Sure...'")
									
									print(name + ": 'We'll return it to you as soon as we can.'")
									
									print("Eidar: 'Mhm. Okay.'")
									
									print("-INVENTORY UPDATED: MYSTERIOUS BLACK ROBE-")
									eidarInterviewed = True
									eidarInterview = False

							print(name + ": 'Can you show me where you found the robe?'")
							
							print("[Eidar point over to the corner of the barely lit basement]")
							
							print("[You begin analyzing the area...]")
							
							print("[It's clear this place have been touched recently...the dust here is not as much]")
							
							print("[There isn't anything else here though..]")
							
							print("Coleridge: 'It's not Mira's.'")
							
							print(name + ": 'Thank you Eidar.'")
							
							print("Eidar: 'Uh-huh.'")
							
							print("[You and Coleridge return to the general store]")
							
							print("[Mira walks out of the kitchen with a tub of water.]")
							
							print("Coleridge: 'Mira, what are you doing.'")
							
							print("Mira: 'There's a homeless man living below my shop yes?'")
							
							print("Coleridge: 'Yea, so?'")
							
							print("Mira: 'Well I'm taking this to him so he can clean himself up.'")
							
							print("[Mira walk out towards her basement with the tub of water]")
							
							print("Coleridge: Wha-...")
							
							print(name + ": 'Hah. What a lady.'")
							
							print("[Coleridge gave a shrug.]")
							
							print("[Mira continues to carry items back and fourth until she finally settles back down behind her counter]")
						if(genStoreExplore == "5"):
							print(name + ": 'Well thanks Mira. I got everything I need.'")
							
							print("Mira: 'Alright. Take care and watch over Coleridge for me.'")
							
							print(name + ": 'Will do ma'am.'")
							
							miraInterview = False
							break
				#miraTestimonytheft
				if(interviewA6a == "4"):
					print(name + ": 'Mira, have there been any recent theft?'")
					
					print("Mira: 'Theft? No I don't think so. Why do you ask?'")
					
					print(name + ": 'The blacksmith next door recently had a theft.'")
					
					print("Mira: 'Oh that's too bad. I should bring something over to Gendel...'")
					
					print("Mira: 'No I haven't had any recent theft but I do remember something.'")
					
					print(name + ": 'Yes? What is it?'")
					
					print("Mira: 'Well I remember seeing a young boy coming out of Gendel's shop...'")
					
					print("Mira: 'But it was in the middle of the day, I thought he must have been a customer or an apprentice.'")
					
					print(name + ": 'Well thanks for the information Mira.'")
					
					print("Mira: 'Of course.'")
					
					print("-NOTES UPDATED: MIRAS TESTIMONY-")
					notepadEntry.remove("Miras Testimony")
					notepadEntry.append("Miras Testimony(Theft)")
					miraTestimonytheft = True
					
				if(interviewA6a == "5"):
					print(name + ": 'Thank you for the information ma'am. I think I have all I need for now.'")
					
					print("Mira: 'You and Coleridge are welcome anytime.'")
					
					print("Mira: 'Please visit me again, offical business or not.'")
					
					print(name + ": 'We will ma'am. Thank you.'")
					miraInterview = False
		if(eidarInterviewed == True and miraTestimonytheft == True):
			print(name + ": 'We got more information than expected here.'")
			
			print("Coleridge: 'Yeah we did! What uh, what exactly did we get?'")
			
			print(name + ": 'Whoever broke in to Gendel also broke in to Mira's basement.'")
			
			print(name + ": 'And thanks to Eidar we know the murderer tried to hide evidence in the basement.'")
			
			print("Coleridge: 'But we're no closer to figureing out who did it though.'")
			
			print(name + ": 'Yes but at least we have a better idea of what happened.'")
			
			print("Coleridge: 'Alright somethings better than nothing I suppose.'")
			
			print("Coleridge: 'Cmon, lets get moving now.'")
			
			area = "100.1"
		elif(eidarInterviewed == True):
			print(name + ": 'We got more information than expected here.'")
			
			print("Coleridge: 'Yeah we did! What uh, what exactly did we get?'")
			
			print(name + ": 'Thanks to Eidar we know the murderer tried to hide evidence in the basement.'")
			
			print("Coleridge: 'But we're no closer to figureing out who did it though.'")
			
			print(name + ": 'Yes but at least we have a better idea of what happened.'")
			
			print("Coleridge: 'Somethings better than nothing I suppose.'")
			
			print("Coleridge: 'Cmon, lets get moving now.'")
			
			area = "100.1"
		else:
			print(name + ": 'Doesn't seem like we got much.'")
			
			print("Coleridge: 'You didn't, I did!'")
			
			print("Coleridge: 'Duh! Its a shop!'")
			
			print(name + ": 'That's not what I'm trying to say.'")
			
			print("Coleridge: 'Well keep whatever it is you want to say. Now let's go.'")
			
			area = "100.1"
#-----------------------AREA 7 CHURCH-----------------------------------
	if(area == "6" and genStoreSecondVisit == True):
		print("____________________________________________")
		
		print("Coleridge: 'Mira! Good to see you soon.'")
		
		print("Mira: 'Hello dear, I find it funny how you visit me more on busy than you do casually.'")
		
		print("Coleridge: 'Its a tough job, a lot of hours.'")
		
		print(name + ": 'Many of which you spend drinking and gambling.'")
		
		print("Coleridge: 'Ha-Ha..yeah'")
		
		print("Mira: 'Good to see you too dear. So do you have more questions for me?'")
		
		print(name + ": 'Yes Mira, Coleridge tells me you goto the church nearby regularly.'")
		
		print("Mira: 'Yes that's right. Why does that case of yours have something to do with the church?'")
		
		print(name + ": 'Yes ma'ma, I'm afraid the man who was killed was Father Merwin.'")
		
		print("Mira: 'Oh dear...'")
		print("-INTERVIEW BEGIN-")
		miraInterview2 = True
		while(miraInterview2 == True):
			print("You may access inventory during interview")
			
			print("1. [Ask about Father Merwin] \n2. [Ask about Father Cornealius] \n3.[Ask about Lawrance] \n4. [Done]")
			interviewA6b = input("")
			inventoryAccess(interviewA6b)

			if(interviewA6b == "1"):
				print(name + ": 'What was Father Merwin like?'")
				
				print("Mira: 'He was a young priest and a very ambitious one at that.'")
				
				print("Mira: 'The man is half my age and yet sometimes he acts twice my age.'")
				
				print("Mira: 'Not to speak ill of the dead but ambitious, religious and young doesn't make a good combination.'")
				
				print("Mira: 'All of us always say that Father Merwin as young as he is a grouch walking into an early grave.'")
				
				print("Mira: 'Now I feel guilty that he did.'")
				
				print("Coleridge: 'Rest assured Mira, it wasn't you who sent him.'")
				
				print(name + ": 'Did he have any enemy?'")
				
				print("Mira: 'I wouldn't say enemy but he was often quite stubborn and a bit overzealous.'")
				
				print("Mira: 'He wasn't loved by anyone but nothing warrants murder.'")
				
				print("Mira: 'Of course the man that he is, he can be uhm, difficult around non-believers.'")
				
				print("Coleridge: 'Ah, the crazy preachy type huh?'")
				
				print("Mira: 'Yes, somewhat like that.'")
				
				print("-NOTES UPDATED: MIRAS TESTIMONY ON MERWIN")
				notepadEntry.append("Miras Testimony on Merwin")
			if(interviewA6b == "2"):
				print(name + ": 'What about Father Cornealius?'")
				
				print("Mira: 'He's certainly what they call a gentle giant.'")
				
				print("Mira: 'Been around the church since I was a lass and he still somehow looks younger than I.'")
				
				print("Coleridge: 'Pft, Mira you still got a good half a century on you.'")
				
				print("Mira: 'Oh please, even you're getting wrinkles beneath your eyes boy and I practically raise you.'")
				
				print("Coleridge: 'That's why I don't compliment women.'")
				
				print(name + ": 'Its probably from the drinking anyway.'")
				
				print("Coleridge: 'I'm not ashamed.'")
				
				print(name + ": 'So Father Cornealius, does he have a family life? Anything outside of church?'")
				
				print("Mira: 'Well Father Cornealius is a pretty shy man. I rarely see him outside the church.'")
				
				print("Mira: 'He always seems so tired and lonely but there was this one lady whom he was close with...'")
				
				print(name + ": 'And this lady who is she?'")
				
				print("Mira: 'Not sure, it felt like a lifetime ago but the father did seem to take a liking to this girl.'")
				
				print("Mira: 'A young drifter who passed by the town. Whenever she visits she's always at the church with the father.'")
				
				print(name + ": 'And what would they be doing?'")
				
				print("Mira: 'Just talking. She would attend the church whenever the father is preaching and when he's done they just talk.'")
				
				print("Mira: 'I haven't seen her in maybe a decade or a little more though. Since than, the father is ..well who he is now.'")
				print("-NOTES UPDATED: MIRAS TESTIMONY ON FATHER CORNEALIUS-")
				notepadEntry.append("Miras Testimony on Father Cornealius")
			if(interviewA6b == "3"):
				print(name + ": 'Mira, do you happen to know anything about the boy that Father Cornealius took in?'")
				
				print("Mira: 'Oh how could I not. The poor boy was subject of gossip for months.'")
				
				print(name + ": 'Um why?'")
				
				print("Mira: 'Well in a church with two man and suddenly a boy in priest robe appears asking for donation?'")
				
				print("Mira: 'Obviously the boy wasn't either of their son, so everyone was wondering where he came from.'")
				
				print(name + ": 'Father Cornealius took him in, what's so odd about that?'")
				
				print("Mira: 'That's not the weird part. We heard the boy was kicked out of an orphanage because he was troubled.'")
				
				print(name + ": 'Troubled, like how?'")
				
				print("Mira: 'Something about being rough with other kids and stealing, things like that. It apparently got real bad.'")
				
				print("Mira: 'Father Cornealius personally agreed to take him in.'")
				
				print(name + ": 'I see...'")
				
				print("-NOTES UPDATED: MIRAS TESTIMONY ON LAWRANCE")
				notepadEntry.append("Miras Testimony on Lawrance")
			if(interviewA6b == "4"):
				print(name + ": 'Well thank you Mira, you've been a major help.'")
				
				print("Mira: 'I'm help. Bring justice to Father Merwin you two...no one deserve to be murdered.'")
				
				print("[You nod to Mira]")
				miraInterview2 == False

		print("Coleridge: 'So it seems like everything is tying together.'")
		
		print(name + ": 'Yeah, now we just need the final piece of evidence.'")
		
		area = "8"
	if(area == "7"):
		print("____________________________________________")
		church = True
		print("[You walked pass the alleyway towards the church with Coleridge]")
		
		print("Coleridge: 'Haven't been here since I was..twelve I think.'")
		
		print(name + ": 'You're not a holy man I take it?'")
		
		print("Coleridge: 'I am, I just don't worship characters from some old legends.'")
		
		print(name + ": 'Legends are usually made of something real.'")
		
		print("Coleridge: 'Hah, yeah and I'm expected to believe some ball of light made all the people, dwarves, elves and every vile disgusting thing in the world?")
		
		print("Coleridge: 'If there is a god, he'd most likely live in a bottle of whiskey.'")
		
		print("Coleridge: 'What about you rookie, you worship those balls of lights?'")
		
		print(name + ": 'Not really, I consider it just fables I used to hear as a kid.'")
		
		print("Coleridge: 'Well there ya go kid. Let's get in there shall we?'")
		
		print("[You nod towards Coleridge and the two of you begin to make your way in.]")
		
		print("[Upon opening the door you see a large bald priest on his knee in front of a large statue]")
		
		print("[There are rows of candles behind the statue stack and lined nice and neatly]")
		
		print("Coleridge: 'Father, sorry to interrupt you.'")
		
		print("[A young boy with brown curly hair and a black robe walks up to you]")
		
		print("Boy: 'Excuse me, but Father Cornealius is in prayer right now, how may I help you?'")

		if(eidarInterviewed == True):
			print(name + ": 'Coleridge the robes.'")
			
			print("[Coleridge looks at the robe on the boy and the priest and nods.]")
			
			print("-NOTES UPDATED: PRIEST ROBE-")
			invArray.remove("Mysterious Robe")
			invArray.append("Priest Robe")
			

		print(name + ": 'We have some questions for Father Cornealius.'")
		
		print("Boy: 'I'm afraid he cannot be interrupted. Come back later or perhaps I can answer a few questions.'")
		
		print(name + ": 'Very well.'")
		
		print("Coleridge: 'Do you mind if I look around?'")
		
		print("Boy: 'As long as you do not interrupt the father, you may.'")
		
		print("[Coleridge gives a sarcastic smile and walks off]")
		print("-INTERVIEW BEGIN-")
		lawranceInterview = True

		while(lawranceInterview == True):
			if(eidarInterviewed == False):
				print("You may access inventory during interview")
				
				print("1. [Ask about the boy] \n2. [Ask about the church] \n3. [Ask about the case] \n4. [Done]")
				interviewA7a = input("")
				inventoryAccess(interviewA7a)

				if(interviewA7a == "1"):
					print(name + ": 'What's your name?'")
					
					print("Boy: 'My name is Lawrance sir, you are a city guard yes?'")
					
					print(name + ": 'Are you an altar boy of some kind?'")
					
					print("Lawrance: 'I suppose I can be considered an altar boy.'")
					
					print(name + ": 'You sound unsure.'")
					
					print("Lawrance: 'Well, to be honest sir, I live here.'")
					
					print("Lawrance: 'I was an orphan but Father Cornealius took me in.'")
					
					print("Lawrance: 'Since then, I've lived here and helped out but I'm not religious or anything.'")
					
					print(name + ": 'I see, why didn't you goto an orphanage.'")
					
					print("Lawrance: 'Well, I used to live in one but I left. The orphanage was getting crowded.'")
					
					print("Lawrance: 'Living in the orphanage got difficult...'")
					
					print(name + ": 'I see.'")
					
					print("-NOTES UPDATED: LAWRANCE-")
					notepadEntry.append("Lawrance")
				#fatherMerwin
				if(interviewA7a == "2"):
					print(name + ": 'So what is Father Cornealius doing?'")
					
					print("Lawrance: 'Meditation sir. It says it gives him inner peace.'")
					
					print(name + ": 'Inner peace huh. What about you?'")
					
					print("Lawrance: 'I just help out here. Religion isn't really a thing for me.'")
					
					print(name + ": 'Understandable. I'm not a religious person either.'")
					
					print(name + ": 'So is it just you and Father Cornealius here?'")
					
					print("Lawrance: 'Yes. The church is usually pretty empty except during weekends.'")
					
					print(name + ": 'So, is it just you and Father Cornealius here Monday to Friday?'")
					
					print("[Lawrance opens his mouth to speak but suddenly pauses]")
					
					print("Lawrance:'Um, no. It's usually me, Father Cornealius and Father Merwin.'")
					
					print(name + ": 'And where is Father Merwin right now?'")
					
					print("Lawrance: 'I don't know. Father Cornealius said that Father Merwin is sick.'")
					
					print(name + ": 'I see....'")
					
					print("-NOTES UPDATED: 'FATHER MERWIN'-")
					notepadEntry.append("Father Merwin")
					
				#lawranceTestimony
				if(interviewA7a == "3"):
					print(name + ": 'So Lawrance, have you heard or seen anything suspicious around here?'")
					
					print("Lawrance: 'This is about the murder down the alley right?'")
					
					print(name + ": 'Oh? So you know about it?'")
					
					print("Lawrance: 'There isn't many reasons groups of guards and mages would surround a random alleyway.'")
					
					print("Lawrance: 'Not to mention people talk especially around church.'")
					
					print(name + ": 'And have you heard anything that may help us?'")
					
					print("[Lawrance gives you a shrug]")
					
					print("Lawrance: 'No, I just heard there was a murder.'")
					
					print(name + ": 'I see.'")
					
					print("-NOTES UPDATED:LAWRANCES TESTIMONY-")
					notepadEntry.append("Lawrances Testimony")
				if(interviewA7a == "4"):
					print(name + ": 'Well thank you for your information. You've been a big help Lawrance.'")
					
					print("[He gives you a mild nod and walks off]")
					
					print("[Coleridge returns besides you]")
					
					print(name + ": 'You found anything?'")
					
					print("Coleridge: 'Pft, no. This is a church kid. Place is clean. You?'")
					
					print(name + ": 'Maybe. I'll need to interview Father Cornealius.'")
					
					print("Coleridge: 'Well looks like he's done.'")
					
					print("[The father stands up and utter a last prayer]")
					lawranceInterview = False
					

			if(eidarInterviewed == True):
				print("You may access inventory during interview")
				
				print("1. [Ask about the boy] \n2. [Ask about the church] \n3. [Ask about the case] \n4. [Ask about the priest robe] \n5. [Done]")
				interviewA7a = input("")
				inventoryAccess(interviewA7a)

				if(interviewA7a == "1"):
					print(name + ": 'What's your name?'")
					
					print("Boy: 'My name is Lawrance sir, you are a city guard yes?'")
					
					print(name + ": 'Are you an altar boy of some kind?'")
					
					print("Lawrance: 'I suppose I can be considered an altar boy.'")
					
					print(name + ": 'You sound unsure.'")
					
					print("Lawrance: 'Well, to be honest sir, I live here.'")
					
					print("Lawrance: 'I was an orphan but Father Cornealius took me in.'")
					
					print("Lawrance: 'Since then, I've lived here and helped out but I'm not religious or anything.'")
					
					print(name + ": 'I see, why didn't you goto an orphanage.'")
					
					print("Lawrance: 'Well, I used to live in one but I left. The orphanage was getting crowded.'")
					
					print("Lawrance: 'Living in the orphanage got difficult...'")
					
					print(name + ": 'I see.'")
					
					print("-NOTES UPDATED: LAWRANCE-")
					notepadEntry.append("Lawrance")
				#fatherMerwin
				if(interviewA7a == "2"):
					print(name + ": 'So what is Father Cornealius doing?'")
					
					print("Lawrance: 'Meditation sir. It says it gives him inner peace.'")
					
					print(name + ": 'Inner peace huh. What about you?'")
					
					print("Lawrance: 'I just help out here. Religion isn't really a thing for me.'")
					
					print(name + ": 'Understandable. I'm not a religious person either.'")
					
					print(name + ": 'So is it just you and Father Cornealius here?'")
					
					print("Lawrance: 'Yes. The church is usually pretty empty except during weekends.'")
					
					print(name + ": 'So, is it just you and Father Cornealius here Monday to Friday?'")
					
					print("[Lawrance opens his mouth to speak but suddenly pauses]")
					
					print("Lawrance:'Um, no. It's usually me, Father Cornealius and Father Merwin.'")
					
					print(name + ": 'And where is Father Merwin right now?'")
					
					print("Lawrance: 'I don't know. Father Cornealius said that Father Merwin is sick.'")
					
					print(name + ": 'I see....'")
					
					print("-NOTES UPDATED: 'FATHER MERWIN'-")
					notepadEntry.append("Father Merwin")
					fatherMerwin = True
					
				#lawranceTestimony
				if(interviewA7a == "3"):
					print(name + ": 'So Lawrance, have you heard or seen anything suspicious around here?'")
					
					print("Lawrance: 'This is about the murder down the alley right?'")
					
					print(name + ": 'Oh? So you know about it?'")
					
					print("Lawrance: 'There isn't many reasons groups of guards and mages would surround a random alleyway.'")
					
					print("Lawrance: 'Not to mention people talk especially around church.'")
					
					print(name + ": 'And have you heard anything that may help us?'")
					
					print("[Lawrance gives you a shrug]")
					
					print("Lawrance: 'No, I just heard there was a murder.'")
					
					print(name + ": 'I see.'")
					
					print("-NOTES UPDATED:LAWRANCES TESTIMONY-")
					notepadEntry.append("Lawrances Testimony")
					lawranceTestimony = True
				#lawranceRobes
				if(interviewA7a == "4"):
					print(name + ": 'I take it that the robe you're wearing is church uniform of some kind?'")
					
					print("Lawrance: 'Yeah, the robes are worn by everyone who works or help around in the church.'")
					
					print(name + ": 'Have you lost any robes lately?'")
					
					print("Lawrance: 'I don't really keep track of the robes around here, I just clean.'")
					
					print(name + ": 'Well can you identify something for us?'")
					
					print("Lawrance: 'Uhm...sure.'")
					
					print("[You hand Lawrance the black robes]")
					
					print("Lawrance: 'This definately belongs to the church, um how did you get it?'")
					
					print(name + ": 'Sorry, I can't tell you.'")
					
					print("[Lawrance gives a subtle nod and hands the robe back to you]")
					lawranceRobes = True
				if(interviewA7a == "5"):
					print(name + ": 'Well thank you for your information. You've been a big help Lawrance.'")
					
					print("[He gives you a mild nod and walks off]")
					
					print("[Coleridge returns besides you]")
					
					print(name + ": 'You found anything?'")
					
					print("Coleridge: 'Pft, no. This is a church kid. Place is clean. You?'")
					
					print(name + ": 'Maybe. I'll need to interview Father Cornealius.'")
					
					print("Coleridge: 'Well looks like he's done.'")
					
					print("[The father stands up and utter a last prayer]")
					lawranceInterview = False
					

		print("[You give a slight bow to the Father as he approaches]")
		
		print("[Father Cornealius smiles and nods towards you]")
		
		print("[You stare slowly towards Coleridge]")
		
		print("[Coleridge gives the father an awkward smile]")
		
		print("[Cornealius nods to Coleridge and you raise your head]")
		
		print("Father Cornealius: 'So, how may I help the gentlemen in red?'")
		
		print(name + ": 'Father Cornealius, someone have been recently murdered nearby. We like to ask some questions.'")
		
		print("Father Cornealius: 'Oh...of course. Anything I can do to help.'")
		
		print("-NOTES UPDATED: FATHER CORNEALIUS-")
		notepadEntry.append("Father Cornealius")
		cornealiusInterivew = True
		while(cornealiusInterivew == True):
			if(eidarInterviewed == False):
				print("You may access inventory during interview")
				
				print("1. [Ask about Lawrance] \n2. [Ask about Father Merwin] \n3. [Ask about the case] \n4. [Done]")
				interviewA7b = input("")
				inventoryAccess(interviewA7b)

				if(interviewA7b == "1"):
					print(name + ": 'Father Cornealius, may I ask you about Lawrance?'")
					
					print("Father Coreanlius: 'Of course.'")
					
					print(name + ": 'I talked to Lawrance earlier and he told me he ran away from an orphange and you took him in right?'")
					
					print("Father Cornealius: 'Yes that's right.'")
					
					print(name + ": 'You do realize you can't just take in an orphanage runaway yes?'")
					
					print("Father Cornealius: 'Of course but Lawrance appeared at my door begging to stay here.'")
					
					print("Father Coreanlius: 'I simply can't just ignore him now can I?'")
					
					print(name + ": 'I suppose not. How long have Lawrance lived here?'")
					
					print("Father Cornealius: 'About a month now.'")
					
					print(name + ": 'I see.'")
					
				if(interviewA7b == "2"):
					print(name + ": 'Lawrance told me that there's a third person who is usually here.'")
					
					print("Father Cornealius: 'Yes that's right. Father Merwin.'")
					
					print(name + ": 'Where is he today?'")
					
					print("Father Cornealius: 'I'm not quite sure. Usually he's always here.'")
					
					print("Father Cornealius: 'Only time he doesn't show up is when he's quite sick.")
					
					print("Father Cornealius: 'Although he seems pretty healthy yesterday.'")
					
					print(name + ": 'I see.'")
					
				if(interviewA7b == "3"):
					print(name + ": 'Father Cornealius, have you seen or heard anything suspicious recently?'")
					
					print("[Father Cornealius strokes his chin lightly]")
					
					print("Father Coreanlius: 'No, not that I'm aware of.'")
					
					if(gendelRockDialogue == True):
						print(name + ": 'Were there any recent robbery?'")
						
						print("Father Cornealius: 'In the church? Hah, who would steal from a church?'")
						
						print("Coleridge: 'Well a lot of scumbags in this city.'")
						
						print("Father Cornealius: 'Hahah, honestly if someone want to steal from the church they might as well just ask.'")
						
						print("Father Cornealius: 'If its money they're after I wouldn't mind offering.'")
						
						print("Coleridge: 'Real generous of you father, care to offer some?'")
						
						print(name + ": 'Coleridge...'")
						
						print("Coleridge: 'I'm kidding, I'm kidding.'")
						
				if(interviewA7b == "4"):
					print(name + ": 'Well thank you Father Cornealius, I think we got everything we need.'")
					
					print("Father Cornealius: 'Mhm. Do take care now and find the man justice yes?'")
					
					print(name + ": 'Will do father, excuse us.'")
					
					print("[You and Coleridge departed from the church]")
					cornealiusInterview = False
					

			if(eidarInterviewed == True):
				print("You may access inventory during interview")
				
				print("1. [Ask about Lawrance] \n2. [Ask about Father Merwin] \n3. [Ask about the case] \n4. [Ask about the robe] \n5. [Done]")
				interviewA7b = input("")
				inventoryAccess(interviewA7b)

				if(interviewA7b == "1"):
					print(name + ": 'Father Cornealius, may I ask you about Lawrance?'")
					
					print("Father Coreanlius: 'Of course.'")
					
					print(name + ": 'I talked to Lawrance earlier and he told me he ran away from an orphange and you took him in right?'")
					
					print("Father Cornealius: 'Yes that's right.'")
					
					print(name + ": 'You do realize you can't just take in an orphanage runaway yes?'")
					
					print("Father Cornealius: 'Of course but Lawrance appeared at my door begging to stay here.'")
					
					print("Father Coreanlius: 'I simply can't just ignore him now can I?'")
					
					print(name + ": 'I suppose not. How long have Lawrance lived here?'")
					
					print("Father Cornealius: 'About a month now.'")
					
					print(name + ": 'I see.'")
					
				if(interviewA7b == "2"):
					print(name + ": 'Lawrance told me that there's a third person who is usually here.'")
					
					print("Father Cornealius: 'Yes that's right. Father Merwin.'")
					
					print(name + ": 'Where is he today?'")
					
					print("Father Cornealius: 'I'm not quite sure. Usually he's always here.'")
					
					print("Father Cornealius: 'Only time he doesn't show up is when he's quite sick.")
					
					print("Father Cornealius: 'Although he seems pretty healthy yesterday.'")
					
					print(name + ": 'I see.'")
					
				if(interviewA7b == "3"):
					print(name + ": 'Father Cornealius, have you seen or heard anything suspicious recently?'")
					
					print("[Father Cornealius strokes his chin lightly]")
					
					print("Father Coreanlius: 'No, not that I'm aware of.'")
					
					if(gendelRockDialogue == True):
						print(name + ": 'Were there any recent robbery?'")
						
						print("Father Cornealius: 'In the church? Hah, who would steal from a church?'")
						
						print("Coleridge: 'Well a lot of scumbags in this city.'")
						
						print("Father Cornealius: 'Hahah, honestly if someone want to steal from the church they might as well just ask.'")
						
						print("Father Cornealius: 'If its money they're after I wouldn't mind offering.'")
						
						print("Coleridge: 'Real generous of you father, care to offer some?'")
						
						print(name + ": 'Coleridge...'")
						
						print("Coleridge: 'I'm kidding, I'm kidding.'")
						
						print("-NOTES UPDATED: FATHER CORNEALIUSS TESTIMONY-")
					notepadEntry.append("Father Cornealiuss Testimony")
				#cornealiusRobe
				if(interviewA7b == "4"):
					print(name + ": 'Father Cornealius, would you care to identify this robe we have?'")
					
					print("[Father Cornealius takes the robe in hand]")
					
					print("[He looks stunt]")
					
					print("Coleridge: 'I think we're getting somewhere.'")
					
					print("Father Cornealius: 'Pardon me but...where did you get this?'")
					
					print(name + ": 'We found it near the scene of the crime. Do you know who it belongs to?'")
					
					print("Father Cornealius: 'Yes...i-it belongs to Father Merwin...'")
					
					print("Father Cornealius: 'Than....'")
					
					print("Coleridge: 'We're uh..sorry for your lost Father Cornealius.'")
					
					print(name + ": 'We aren't even certain if it is Father Merwin's yet Father Cornealius.'")
					
					print("Father Cornealius: 'This is his robe..what other ..who would...'")
					
					print(name + ": 'Father Cornealius, we're not even certain if the body is Father Merwin...'")
					
					print("Father Cornealius: 'It explains so much...there's no way Father Merwin would not be here..'")
					
					print(name + ": 'Father Cornealius, would you help us identify the body later?'")
					
					print("Father Cornealius: 'O-Of course...'")
					
					print(name + ": 'Thank you father.'")
					cornealiusRobe = True
					
				if(interviewA7b == "5"):
					print(name + ": 'Well thank you Father Cornealius, I think we got everything we need.'")
					
					print("Father Cornealius: 'Mhm. Do take care now and find justice for Me- ..the man yes?'")
					
					print(name + ": 'Will do father, excuse us.'")
					
					print("[You and Coleridge departed from the church]")
					cornealiusInterview = False
					
		print("Coleridge: 'Lets get outta here, this place gives me the creeps.'")
		
		print(name + ": 'Yeah I know what you mean.'")
		
		print("Coleridge: 'You do?'")
		
		print(name + ": 'For once, yeah.'")
		area = "100.1"
#-----------AREA 6 INTERVIEW: MIRA THE GENERAL SHOPKEEPER--------------
#---------------------AREA 8: INTERROGATION---------------------------
	if(area == "8"):
		print("____________________________________________")
		print("Welcome to Interrogation. This is the final stretch of the investigation. Here you may re-interview all of the characters you come across and eventually accuse one of them of the crime. Presenting evidence from your notes and inventory may cause the accused to be stressed leading to a more convincing conviction and a more solid answer. Keep in mind you may open your inventory when prompt to give an input.")
		time.sleep(15)
		while(True):
			print("Captain Faust: 'So who should I bring in?'")
			
			print("1. Captain Faust \n2. Coleridge \n3. Messenger Boy \n4. Scholar William \n5. Gendel the Blacksmith \n6. Mira the General Shopkeeper \n7. Eidar the Homeless \n8. Father Cornealius \n9. Lawrance")
			witnessInt = input("")
			inventoryAccess(witnessInt)

			#faustInterview
			if(witnessInt == "1"):
				faustInterview = True
				print(name + ": 'Captain Faust. I like to interview you...'")
				
				print("Captain Faust: 'Wha-? What do I have to do with the crime.'")
				
				print(name + ": 'Please sit, Captain Faust.'")
				
				print("[With an irritated look, Faust sat in front of you...]")
				
				print("Captain Faust: 'This better not be some stupid prank by you or Coleridge.'")
				
				while(True):
					print("1. [Ask for an alibi] \n2. [Review Witness Information] \n3. [Accuse] \n4. [Dismiss]")
					intPrompt = input("")
					inventoryAccess(intPrompt)

					if(intPrompt == "1"):
						print(name + ": 'What were you doing at the day of the murder.'")
						
						print("Captain Faust: 'Briefing you, you idiot.'")
						
						print(name + ": 'And do you have anyone who can corroborate with that?'")
						
						print("[Captain Faust gives you a blank stare....]")
						
						print(name + ": 'Right....'")
					if(intPrompt == "2"):
						print(name + ": 'So can you repeat what you told me during my investigation?'")
						
						print("Captain Faust: 'I didn't tell you shit because I am not a part of your investigation!'")
						
						print(name + ": '..Mhm ..right...'")
					if(intPrompt == "3"):
						print("Are you sure you wish to accuse Captain Faust of the murder?")
						print("1. Yes \n2. No")
						accusedResponse = input("")
						inventoryAccess(accusedResponse)

						if(accusedResponse == "1"):
							print(name + ": 'Captain Faust...YOU ARE THE MURDERER!'")
							
							print("Coleridge: 'Whoo, the rookie is high on something...'")
							
							print("Captain Faust: 'You're kidding me...what evidence do you have to support that?!'")
							
							print(notepadEntry)
							print(invArray)
							print("TYPE IN THE EVIDENCE NAME")
							Evidence = input("")
							inventoryAccess(Evidence)
							print(name + ": 'This evidence shows that! Um...well.. I...I don't know...")
							
							print("Captain Faust: 'GOD DAMMIT THIS IS A WASTE OF TIME. YOU GOT TO BE KIDDING ME!'")
							
							print("Captain Faust: 'DAMMIT I KNEW BETTER THAN TO TRUST YOU COLERIDGE.'")
							
							print("Coleridge: 'Wha..what did I do?'")
							
							print("Captain Faust: 'Forget it! I'm taking both of you off this case and sends it over to someone else!'")
							
							print(name + ": 'Uh....'")
							ending = "1"
							area = "ENDING"
					if(intPrompt == "4"):
						print(name + ": 'Uhm...nevermind Captain Faust... you're free to go...'")
						
						print("Captain Faust: 'Ugh..stop fooling around already! We have a case to solve!'")
						
						break
			if(witnessInt == "1" and faustInterview == True):
				print(name + ": 'Captain Faust I need you here again!'")
				
				print("Captain Faust: 'Stop wasting both of our time!'")
				
				print(name + ": 'Uhm..okay, sorry captain.'")
				
			#coleInterview
			if(witnessInt == "2"):
				coleInterview = True
				print(name + ": 'Coleridge I wish to interview you...'")
				
				print("Coleridge: 'Huh..?'")
				
				print("Coleridge: 'Aw cmon, what the hell are you playing at?'")
				
				print("[Coleridge moves from the chair besides you to the one across]")
				while(True):
					print("1. [Ask for an alibi] \n2. [Review Witness Information] \n3. [Accuse] \n4. [Dismiss]")
					intPrompt = input("")
					inventoryAccess(intPrompt)

					if(intPrompt == "1"):
						print(name + ": 'Where were you during the time of the murder?'")
						
						print("Coleridge: 'How about right next to you jackass.'")
						
						print("Coleridge: 'This shit ain't funny.'")
						
						print(name + ": 'And do you have a witness who can attest to that?'")
						
						print("Coleridge: 'Y-You're kidding me right? Did you hit your head too hard?'")
					if(intPrompt == "2"):
						print(name + ": 'So tell me what you told me previously'")
						
						print("Coleridge: 'I don't know, I was half drunk yesterday.'")
						
						print(name + ": 'Mhm...'")
						
						print("Coleridge: 'What?! Am I still drunk? What the hell is going on?!'")
					if(intPrompt == "3"):
						print("Are you sure you wish to accuse Coleridge of the murder?")
						print("1. Yes \n2. No")
						accusedResponse = input("")
						inventoryAccess(accusedResponse)

						if(accusedResponse == "1"):
							print(name + ": 'Coleridge...YOU ARE THE MURDERER!'")
							
							print("Coleridge: 'This is some sick twisted shit you're into boy. Fine I'll play along, how?'")
							print(notepadEntry)
							print(invArray)
							print("TYPE IN THE EVIDENCE NAME")
							Evidence = input("")
							inventoryAccess(Evidence)
							print(name + ": 'THIS EVIDENCE INDICATES THAT YOU....'")
							
							print("Coleridge: 'Are bloody drunk kid...Captain, I think the kid needs a break...a really long one.'")
							
							print("Captain Faust: 'Agreed...'")
							
							ending = "2"
							area = "ENDING"
					if(intPrompt == "4"):
						print(name + ": 'Uh ..nevermind Coleridge..you can go..'")
						
						print("Coleridge: '...Alright..damn rookie'")
						
						print("[Coleridge retakes his seat besides you...]")
						partnerRel = partnerRel - 5
						break
			if(wintessInt == "2" and coleInterview == True):
				print(name + ": 'Coleridge..'")
				
				print("Coleridge: 'No, just shut the hell up kid.'")
				
			if(witnessInt == "3"):
				print(name + ": 'I wish to interview the messenger boy.'")
				
				print("Captain Faust: Who?'")
				
				print(name + ": 'He's uh..the kid who wakes me up every morning...'")
				
				print("Coleridge: '...Wow...he must be screwing up his job pretty badly for you to want to accuse him of murder...'")
				
				print("Captain Faust: '...O-Okay...Guess I'll bring him in...'")
				while(True):
					print("1. [Ask for an alibi] \n2. [Review Witness Information] \n3. [Accuse] \n4. [Dismiss]")
					intPrompt = input("")
					inventoryAccess(intPrompt)

					if(intPrompt == "1"):
						print(name + ": 'Where were you during the time of the murder?'")
						
						print("Messenger: Mur-Murder? What murder?!'")
						
						print("Coleridge: '..Holy crap, what the hell is this.'")
						
						print(name + ": 'Where were you yesterday sir?'")
						
						print("Messenger: 'I-I was just w-waking up pe- I love me mum I didn't kill nobody!")
					if(intPrompt == "2"):
						print(name + ": 'So what was it you tell me during the interview?'")
						
						print("Messenger: 'Wh-What interview, w-what's going on?!")
						
						print("Coleridge: 'Captain, is this legal?'")
						
						print("[Captain Faust gives a shrug]")
					if(intPrompt == "3"):
						print("Are you sure you wish to accuse the Messenger Boy of the murder?")
						print("1. Yes \n2. No")
						accusedResponse = input("")

						if(accusedResponse == "1"):
							print(name + ": 'BOY!...YOU ARE THE MURDERER!'")
							
							print("[The Messenger Boy collasped on to the floor in shock]")
							
							print("Coleridge: 'Holy shit, I think you killed him...'")
							
							print("[The Messenger Boy groans]")
							
							print("Coleridge: 'Oh, okay...'")
							ending = "3"
							area = "ENDING"
					if(intPrompt == "4"):
						print(name + ": 'Hm..nevermind, you can go.'")
						
						print("Messenger: 'Oh thank goodnes...'")
						
						print("[The Messenger departed in heavy relief...]")
						break
			if(witnessInt == "4"):
				print(name + ": 'Please bring Scholar William in...'")
				
				print("Captain Faust: 'Uh...alright.'")
				
				print("[Several minutes later...]")
				
				print("Captain Faust: 'It seems Scholar William has departed the city...'")
				
				print(name + ": 'Oh...'")
				
				print("Captain Faust: 'If you need his information again just consult your notes.'")
				
			if(witnessInt == "5"):
				print(name + ": 'Please bring in Gendel the Blacksmith.'")
				
				print("Captain Faust: 'Very well.'")
				
				print("Gendel: 'Ah! Whaddaye want boy?! I'm busy dammit!'")
				
				print("[He looks at the chair too tall for him...]")
				
				print("[He forces his way up the chair anyway....]")
				
				while(True):
					print("1. [Ask for an alibi] \n2. [Review Witness Information] \n3. [Accuse] \n4. [Dismiss]")
					intPrompt = input("")
					inventoryAccess(intPrompt)

					if(intPrompt == "1"):
						print(name + ": 'What were you doing during the time of the murder?'")
						
						print("Gendel: 'This bloody thing again?! I told ye, I was working in me forge!'")
						
						print(name + ": 'Can anyone agreed with that?'")
						
						print("Gendel: 'Huh! Blooy no! I work alone...'")
						
						print(name + ": 'Hm...'")
						
						print("Gendel: 'Don't mean I kill nobody!'")
					if(intPrompt == "2"):
						print(name + ": 'So do you mind telling me what you know again?'")
						
						print("Gendel: 'I told ye, I didn't know nothing I was working. My family heirloom got stolen and that's all I know.'")
						
						print(name + ": 'Okay, thank you.'")
					if(intPrompt == "3"):
						print("Are you sure you wish to accuse Gendel the Blacksmith of the murder?")
						print("1. Yes \n2. No")
						accusedResponse = input("")

						if(accusedResponse == "1"):
							print(name + ": 'Gendel the Blacksmith...YOU ARE THE MURDERER!'")
							
							print("Coleridge: 'As funny as it would be to see the dwarf in the dungeon..I don't think that's a good idea...")
							
							print("Gendel the Blacksmith: 'How dare ya?! Well I like to see ya prove it ya bald face pinky.'")
							
							print(notepadEntry)
							print(invArray)
							print("TYPE IN THE EVIDENCE NAME")
							Evidence = input("")

							if(Evidence == "Gendels Rock"):
								print("Gendel: '..Me rock...what about it?'")
								
								print(name + ": 'Well ..you ..lost it right..?'")
								
								print("Gendel: '...Yeah so?'")
								
								print(name + ": 'Uh...well...'")
								
								print("Coleridge: 'Oh ..this is bad.'")
								
								print(name + ": 'Uh...hm...'")
								
							elif(Evience == "Handprint in Gendels"):
								print(name + ": 'There was a strange handprint we found in your shop.'")
								
								print("Gendel: 'Well maybe..it's the thief's ...SO WHAT DOES THIS HAVE TO DO WITH ME?!.'")
								
								print(name + ": '....Uh...'")
								
							elif(Evidence == "Gendel the Blacksmith"):
								print(name + ": 'This is some notes I've written about you...'")
								
								print("Gendel: '...And?'")
								
								print(name + ": '....'")
								
							print("Coleridge: 'Alright kid..I think it's about time for a break.'")
							ending = "4"
							area = "ENDING"
					if(intPrompt == "4"):
						print(name + ": 'Uh..thank you Gendel, you can leave now.'")
						
						print("Gendel: 'Bloody finally, ya better find where my heirloom is!'")
						
						print("[Gendel swats Faust's hand away as he attempt to assist him off the chair and waddles off grumbling...]")
						break
			if(witnessInt == "6"):
				print(name + ": 'Captain, please bring in Mira the General Shopkeeper'")
				
				print("Captain Faust: 'Alright.'")
				
				print("[Mira walks in and sits across from you]")
				
				print("Mira: 'I didn't think I'd see you boys again so quickly.'")
				
				print(name + ": 'Yes, well we just like to be throughout.'")
				
				print("Mira: 'Yes of course, go right ahead.'")
				while(True):
					print("1. [Ask for an alibi] \n2. [Review Witness Information] \n3. [Accuse] \n4. [Dismiss]")
					intPrompt = input("")
					inventoryAccess(intPrompt)

					if(intPrompt == "1"):
						print(name + ": 'Where were you during the murder??'")
						
						print("Coleridge: 'Tread lightly there rookie...'")
						
						print("Mira: 'Um..when did the murder happen?'")
						
						print(name + ": 'Most likely the day before..'")
						
						print("Mira: 'Probably at my shop of course.'")
						
						print(name + ": 'Mmkay.'")
						
					if(intPrompt == "2"):
						print(name + ": 'Would you care to repeat your testimony?'")
						
						print("Mira: 'Of course, but I didn't see or hear anything suspicious.")
						
						print("Mira: 'And I certainly didn't realize when a homeless man was living in my basement.'")
						
						print("Mira: 'Besides that, there was the things I mention about the church yesterday...'")
						
						print("Mira: 'Do you need me to repeat that?'")
						
						print(name + ": 'No, that's quite alright ma'am.'")
					if(intPrompt == "3"):
						print("Are you sure you wish to accuse Mira the General Shopkeeper of the murder?")
						print("1. Yes \n2. No")
						accusedResponse = input("")

						if(accusedResponse == "1"):
							print(name + ": 'Mira the General Shopkeeper...YOU ARE THE MURDERER!'")
							
							print("Coleridge: 'Alright this is bullshit kid.'")
							
							print("Mira: 'Oh dear...'")
							
							print("Coleridge: 'Why don't you go ahead and prove how this sweet lil'old lady killed a man twice her size.'")
							print(notepadEntry)
							print(invArray)
							print("TYPE IN THE EVIDENCE NAME")
							Evidence = input("")
							print(name + ": 'Uh....P-Perhaps I made a mistake...'")
							
							print("Coleridge: 'Damn right ya did. Let me take you home Mira...a waste of time.'")
							ending = "5"
							area = "ENDING"
					if(intPrompt == "4"):
						print(name + ": 'Thank you Mira, you're free to go.")
						
						print("Mira: 'Mhm, good luck to you boys.'")
						
						print("Coleridge: 'Captain Faust, let's get a couple more guards to send her home.'")
						
						print("Captain Faust: 'Agreed.'")
						break
			if(witnessInt == "7"):
				print(name + ": 'I would like to see Eidar the Homeless.'")
				
				print("Captain Faust: 'Very well, I'll have the men bring him in.'")
				
				print("[Eidar walks in cleaned up and well dressed]")
				
				print("Coleridge: 'Holy crap, did you dig up gold or something?.'")
				
				print("Eidar: 'Yes indeed I did, Mira took very well care of me and in exchange I help her with the store.'")
				
				print(name + ": 'Good to see you have a second chance Eidar.'")
				
				print("Coleridge: 'You better take good care of that ol'lady ya hear?'")
				
				print("Eidar: 'Certainly, and I have you two to thank as well but you must've called me here for something else.'")
				
				print(name + ": 'Yes Eidar, please sit.'")
				
				print("[Eidar takes a seat across from you...]")
				
				while(True):
					print("1. [Ask for an alibi] \n2. [Review Witness Information] \n3. [Accuse] \n4. [Dismiss]")
					intPrompt = input("")
					inventoryAccess(intPrompt)

					if(intPrompt == "1"):
						print(name + ": 'Eidar, would you care to tell us where you were during the murder?'")
						
						print("Eidar: 'As I've said previously, I was out in the street..looking for a place to sleep.'")
						
						print("Eidar: 'I have nothing to do with any murder that happened.'")
						
						print(name + ": 'Anyone can agree with you on that?'")
						
						print("Eidar: What?! No! Of course not!")
						
					if(intPrompt == "2"):
						print(name + ": 'Can you tell me again what you told me previously?'")
						
						print("Eidar: 'I went to the general store looking for a place to sleep...'")
						
						print("Eidar: 'I found the basement unlock and slept in it and found somethings in the basement.'")
						
						print(name + ": 'Such as the black robe yes?'")
						
						print("Eidar: 'Yes. That's right.'")
						
					if(intPrompt == "3"):
						print("Are you sure you wish to accuse Eidar the Homeless of the murder?")
						print("1. Yes \n2. No")
						accusedResponse = input("")

						if(accusedResponse == "1"):
							print(name + ": 'Eidar the Homeless...YOU ARE THE MURDERER!'")
							
							print("Eidar: 'Whoa! Hey! I agree I was trespassing by Mira was okay with it! I am not a murderer!'")
							
							print(name + ": 'You are the murderer and I can prove it!'")
							
							print(notepadEntry)
							print(invArray)
							print("TYPE IN THE EVIDENCE NAME")
							Evidence = input("")

							if(Evidence == "Priest Robe" or Evidence == "priest robe"):
								print(name + ": 'Eidar, are you aware who the robes belong to?'")
								
								print("Eidar: 'Of course not! I told you that!'")
								
								print(name + ": 'Let me tell you then...it belongs to a father of a church, Father Merwin!'")
								
								print("Eidar: 'So what?! You're saying I killed some clergyman?!'")
								
								print(name + ": 'Yes! And this is precisely why!'")
								print(notepadEntry)
								print(invArray)
								print("TYPE IN THE EVIDENCE NAME")
								Evidence2 = input("")

								if(Evidence2 == "Miras Testimony on Merwin" or Evidence2 == "miras testimony on merwin"):
									print(name + ": 'Shall I tell you what I believe happened Eidar?'")
									
									print("Eidar: 'Go ahead and try!'")
									
									print(name + ": 'Father Merwin, a very strict and overzealous man must've saw you breaking in Mira's basement..'")
									
									print(name + ": 'Being the man he is, he was most likely against even the smallest of crime.'")
									
									print(name + ": 'Afterward, he confronted you and in a panic you killed him and took his robes!'")
									
									print("Eidar: 'You're crazy! Do you think I am stupid enough to keep the robe muchless give it to you?!'")
									
									print(name + ": 'Enough! Captain, arrest this man!'")
									
									print("Eidar: 'Y-You bastard! I won't forget this!'")
									
									print("Captain Faust: 'Arrest him!'")
									
									print("[Several men walks in and drags Eidar away as he screams and shouts]")
									ending = "6"
									area = "ENDING"
								else:
									print(name + ": 'This evidence is the reason why you killed Father Merwin!'")
									
									print("Eidar: 'Care to explain?'")
									
									print(name + ": 'Well..you see....um....uh..'")
									
									print("Coleridge: 'Rookie, I think you need a break..come on.'")
									
									print("Eidar: 'No, this is a waste of time. You cannot keep me here. I'm leaving.'")
									
									ending = "7"
									area = "ENDING"
							else:
								print(name + ": 'This is the evidence that will prove your guilt!'")
								
								print("Coleridge: '...'")
								
								print("Captain Faust: '...'")
								
								print("Eidar: ...Just what the hell does that prove?!?")
								
								print(name + ": '....Uh well...'")
								
								print("Eidar: 'Dammit this is a waste of time!'")
								
								print("Coleridge: 'Alright, let's take a second here...'")
								ending = "7"
								area = "ENDING"
					if(intPrompt == "4"):
						print(name + ": 'Thank you Eidar, that's all we need from you for now.'")
						
						print("Eidar: 'Very well. Glad to be of help.'")
						
						print("[Eidar stands and exits...]")
			if(witnessInt == "8"):
				print(name + ": 'Captain, please bring in Father Cornealius.'")
				
				print("Captain Faust: 'Very well, I'll have the men on it right away.'")
				
				print("[Father Cornealius enters and sits in the chair across from you]")
				
				print("Father Cornealius: 'It is...good to see you again'")
				
				print(name + ": 'Yes..sorry for your lost..but..'")
				
				print("Father Cornealius: Yes, I am aware...very well. Please begin.'")
				
				while(True):
					print("1. [Ask for an alibi] \n2. [Review Witness Information] \n3. [Accuse] \n4. [Dismiss]")
					intPrompt = input("")
					inventoryAccess(intPrompt)

					if(intPrompt == "1"):
						print(name + ": 'Father Cornealius, where were you when Father Merwin was murderer?'")
						
						print("Father Cornealius: 'In church, meditating as I always do.'")
						
						print(name + ": 'And can anyone else verify that?'")
						
						print("Father Cornealius: 'Just...Lawrance I'm afraid.'")
						
						print(name + ": 'Very well.'")
					if(intPrompt == "2"):
						print(name + ": 'So can you tell me again what you told me at the church?'")
						
						print("Father Cornealius: 'Most certainly, but I just didn't see anything or have any information about the murder...'")
						
						print(name + ": 'Right.'")
						
					if(intPrompt == "3"):
						print("Are you sure you wish to accuse Father Cornealius of the murder?")
						print("1. Yes \n2. No")
						accusedResponse = input("")

						if(accusedResponse == "1"):
							print(name + ": 'Father Cornealius...YOU ARE THE MURDERER!'")
							
							print("Father Cornealius: 'Pardon me...but I-...Father Merwin is a dear friend of mine..'")
							
							print("Father Cornealius: 'I'm sorry but...I can't be the one who hurt Merwin...'")
							
							print(name + ": 'Very well..I will prove to you that you did it..that you killed Father Merwin...'")
							
							print(notepadEntry)
							print(invArray)
							print("TYPE IN THE EVIDENCE NAME")
							Evidence = input("")

							if(Evidence == "Miras Testimony on Lawrance"):
								print(name + ": 'First, let's address some of the lies you told us yes?")
								
								print(name + ": 'First, Lawrance.'")
								
								print("Father Cornealius: 'What about him?'")
								
								print(name + ": 'You told me he ran away from an orphanage yes?'")
								
								print("Father Cornealius: 'He is. So?'")
								
								print(name + ": 'Funny. I've heard rumors that the orphanage kicked him out.'")
								
								print("Father Cornealius: 'You should know better than to listen to rumors as evidence.'")
								
								print(name + ": 'You're right but what will we find if we check the orpahange ourselves?'")
								
								print("Father Cornealius: '.....'")
								
								print(name + ": 'Why did you lie to us about that Father Cornealius?'")
								
								print("Father Cornealius: 'I care for Lawrance I great deal..'")
								
								print("Father Cornealius: 'I didn't want him to carry the burden of those past stigma.'")
								
								print("Father Cornealius: 'He isn't a troubled child. He just needs someone to care for him.'")
								
								print("Father Cornealius: 'What does this have to do with Merwin's death?'")
								print(notepadEntry)
								print(invArray)
								print("TYPE IN THE EVIDENCE NAME")
								Evidence2 = input("")
								if(Evidence2 == "Miras Testimony on Merwin"):
									print(name + ": 'I take it that Merwin didn't like the idea of a troubled non-believing boy living in his church yes?.'")
									
									print("Father Cornealius: 'No ...he didn't ...so you're saying I killed Merwin because he didn't like Lawrance?'")
									
									print(name + ": 'Perhaps. Let's get you and Lawrance together in the same room then.'")
									
									print(name + ": 'Captain Faust.'")
									
									print("Captain Faust: 'Alright.'")
									
									print(name + ": 'I'll let you think through this here.'")
									print("[You and Coleridge walks out of the room and closes the door...]")
									area = "9"
								else:
									print("[Father Cornealius let out a chuckle]")
									
									print("Father Cornealius: 'A shame...I'm afraid you've made a mistake.'")
									
									print("Father Cornealius: 'Now..please excuse me..I need to prepare for my friend's funeral..")
									ending = "8"
									area = "ENDING"
							elif(Evidence == "Miras Testimony on Merwin" or Evidence == "miras testimony on merwin"):
								print("Father Cornealius: 'He was a very religious man..I don't see how I would be his murderer.'")
								
								print(name + ": 'Yes indeed, I bet he was pretty strict about the church wasn't he?'")
								
								print("Father Cornealius: 'As expected. He was a devout man.'")
								
								print(name + ": 'Indeed...'")
								
								print("Father Cornealius: 'How does this proof I murdered him?'")
								
								print(name + ": 'Before that..how did he feel about Lawrance?'")
								
								print("Father Cornealius: '....'")
								
								print("Cornealius: 'He...didn't like Lawrance very much...so what?'")
								print(notepadEntry)
								print(invArray)
								print("TYPE IN THE EVIDENCE NAME")
								Evidence2 = input("")
								if(Evidence2 == "Miras Testimony on Lawrance"):
									print(name + ": 'And you lied to us about Lawrance, Father Cornealius.'")
									
									print("Father Cornealius: 'How so?'")
									
									print(name + ": 'It appears that Lawrance didn't run away from the orpahange...'")
									
									print(name + ": 'Care to explain why you lied to us?'")
									
									print("Father Cornealius: 'Lawrance is young..I didn't want him to carry around the stigma of being a troubled youth.'")
									
									print(name + ": 'Did Father Merwin know about this troubled non-religious youth living in his church?'")
									
									print("Father Cornealius: '...He did...'")
									
									print("Father Cornealius: 'So are you suggesting I killed Merwin ..because of Lawrance?'")
									
									print(name + ": 'Maybe..let's get Lawrance in here as well shall we.'")
									
									print(name + ": 'Captain Faust, will you please?'")
									
									print("Faust: 'Got it.'")
									
									print(name + ": 'Father, we'll just leave you here to think on this for a little bit...'")
									area = "9"
								else:
									print("Father Cornealius: 'A shame...I'm afraid you've made a mistake.'")
									
									print("Father Cornealius: 'Now..please excuse me..I need to prepare for my friend's funeral..")
									ending = "8"
									area = "ENDING"
							elif(Evidence == "Mira's Testimony on Father Cornealius" or Evidence == "mira's testimony on father cornealius"):
								print("Father Cornealius: 'I don't see how this leads to the conclusion that I murdere father Merwin.'")
								
								print("Father Cornealius: 'The girl was simple taken by my sermon and she was a very devout girl...'")
								
								print(name + ": 'Well yes but.....uhm...'")
								
								print("Father Cornealius: 'I'm sorry..but I grief for my friend and you accuse me of his murder?")
								
								print("Father Cornealius: '...Excuse me please..I-I need to tend to Father Merwin for his funeral...'")
								ending = "8"
								area = "ENDING"
							else:
								print("Father Cornealius: 'Care to elaborate?'")
								
								print(name + ": 'Well...its just that..uhm...'")
								
								print("Coleridge: 'Sigh..I'm sorry about this we're just gonna take a break okay?'")
								
								print("Father Cornealius: 'I'm sorry but I'm quite busy..and if you don't have anything on me, I'm afraid I must take my leave...")
								
								print("Coleridge: 'Uh..right...'")
								
								print("[Father Cornealius bows and leaves]")
								ending = "8"
								area = "ENDING"
					if(intPrompt == "4"):
						print(name + ": 'Well Father Cornealius, thank you for coming down.'")
						
						print("Father Cornealius: 'It's quite alright. Anything to find justice for my dear friend...'")
						
						print(name + ": 'Mhm.'")
						
						break
			if(witnessInt == "9"):
				print(name + ": 'Please bring in the church boy, Lawrance'")
				
				print("Captain Faust: 'Alright, I'll send men over to the church.'")
				
				print("[Lawrance walks in looking around and slowly found his seat]")
				
				print("Lawrance: 'Um..why am I here?'")
				
				print(name + ": 'We just want to go over somethings and ask you a few extra questions is all.'")
				
				print("Lawrance: '..Okay...'")
				while(True):
					print("1. [Ask for an alibi] \n2. [Review Witness Information] \n3. [Accuse] \n4. [Dismiss]")
					intPrompt = input("")
					inventoryAccess(intPrompt)

					if(intPrompt == "1"):
						print(name + ": 'What were you doing the day Father Merwin was murdered?'")
						
						print("Lawrance: 'Uhm...I was cleaning the church.'")
						
						print(name + ": 'Anyone at that church with you?'")
						
						print("Lawrance: 'Yes...Father Cornealius.'")
						
						print(name + ": 'Okay.'")
					if(intPrompt == "2"):
						print(name + ": 'Can you tell me what you told me yesterday again?'")
						
						print("Lawrance: 'Um...sure...I didn't see or hear anything...'")
						
						print("Lawrance: 'I just knew..there was a murder because people talked about it...'")
						
					if(intPrompt == "3"):
						print("Are you sure you wish to accuse Lawrance of the murder?")
						print("1. Yes \n2. No")
						accusedResponse = input("")

						if(accusedResponse == "1"):
							print(name + ": 'Lawrance...YOU ARE THE MURDERER!'")
							
							print("Lawrance: 'E-Excuse me?'")
							
							print(name + ": 'That's right Lawrance, as I've just said.'")
							
							print(name + ": 'I believe you are the one responsible for Father Merwin's murder'")
							
							print("Lawrance: 'That..I ..no...that's impossible.'")
							
							print(name + ": 'Then allow me to explain it to you...'")
							print(notepadEntry)
							print(invArray)
							print("TYPE IN THE EVIDENCE NAME")
							Evidence = input("")

							if(Evidence == "Mira's Testimony on Lawrance"):
								print(name + ": 'You and Father Cornealius both said you've ran away from your previous orphanage?'")
								
								print("Lawrance: 'Y-Yes..'")
								
								print(name + ": 'And yet...we both know this isn't true.'")
								
								print("Lawrance: 'Wh-What do you mean?'")
								
								print(name + ": 'There's been talk that you caused some trouble. You didn't run from the old orphanage you were kicked out.'")
								
								print("Lawrance: '...'")
								
								print(name + ": 'What did you do Lawrance?'")
								
								print("Lawrance: '...I-I didn't do anything...i-it wasn't me ...I didn't do anything...'")
								
								print("[Lawrance looks down holding his head and shaking it...]")
								
								print("Coleridge: 'Rookie, ease up on the kid.'")
								
								print(name + ": 'Okay..lets talk about Father Merwin...did you get along with him?'")
								
								print("Lawrance: 'Y-Yes...'")
								
								print(name + ": 'You're lying to me again Lawrance...")
								
								print("Lawrance: 'I-I...'")
								print(notepadEntry)
								print(invArray)
								print("TYPE IN THE EVIDENCE NAME")
								Evidence2 = input("")

								if(Evidence2 == "Mira's Testimony on Merwin"):
									print(name + ": 'Father Merwin, didn't like you did he?'")
									
									print("Lawrance: 'N-No he did. He..like...Father Cornealius..'")
									
									print(name + ": 'But he's nothing like Father Cornealius is he?")
									
									print(name + ": 'A rigid man, fill with religious ambition and belief...'")
									
									print(name + ": 'Having someone like you living in his church..he didn't like that one bit..did he?'")
									
									print("Lawrance: 'E-Enough! I-I want Father Cornealius!'")
									
									print(name + ": 'Very well...we'll bring Father Cornealius in...think on it.'")
									
									print("[You and Coleridge walks out closing the door behind you...]")
									area = "9"
								else:
									print(name + ": 'This ..is your lie...'")
									
									print("[Lawrance lets out a sudden chuckle]")
									
									print("[Coleridge raises an eyebrow..]")
									
									print("Lawrance: 'I-I'm afraid I don't understand..could you explain it to me?'")
									
									print(name + ": ''Well ...this ...uh...'")
									
									print("Lawrance: 'Yes?'")
									
									print(name + ": 'This....basically..'")
									
									print("Lawrance: 'It seems..you are not well prepared...perhaps another time ...sir.'")
									
									print("[Lawrance stands and slowly walks out of the room...]")
									ending = "9"
									area = "ENDING"
							elif(Evidence == "Mira's Testimony on Merwin"):
								print(name + ": 'Father Merwin..what is your opinion about him?'")
								
								print("Lawrance: 'He ...is a good person..like Father Cornealius...'")
								
								print(name + ": 'You two get along well?'")
								
								print("Lawrance: 'Yes sir...'")
								
								print(name + ": 'I don't think so Lawrance...he was an overzealous man..'")
								
								print(name + ": 'He condemned the nonbelievers...so much so that his hometown dispies him...'")
								
								print(name + ": 'And you...you're a nonbeliever ain't that right? Living in the place of his worship...'")
								
								print("Lawrance: 'N-No ..you're wrong..I ...")
								print(notepadEntry)
								print(invArray)
								print("TYPE IN THE EVIDENCE NAME")
								Evidence = input("")
								if(Evidence2 == "Mira's Testimony on Lawrance"):
									print(name + ": 'Not to mention...there's this..'")
									
									print("Lawrance: '...'")
									
									print("Lawrance: 'I...what do you mean?'")
									
									print(name + ": 'Not only are you a nonbeliever...you were kicked out of your orphanage..you didn't run.'")
									
									print(name + ": 'Father Merwin ..didn't like you at all did he? He never did..and neither did you.'")
									
									print("Lawrance: 'I've...heard enough...I want Father Cornealius...'")
									
									print(name + ": 'Very well...we'll bring Father Cornealius in...think on it.'")
									
									print("[You and Coleridge walks out closing the door behind you...]")
									area = "9"
									print("")
								else:
									print(name + ": 'Not to mention..there's this...'")
									
									print("[Lawrance lets out a sudden chuckle]")
									
									print("[Coleridge raises an eyebrow..]")
									
									print("Lawrance: 'I-I'm afraid I don't understand..could you explain it to me?'")
									
									print(name + ": ''Well ...this ...uh...'")
									
									print("Lawrance: 'Yes?'")
									
									print(name + ": 'This....basically..'")
									
									print("Lawrance: 'It seems..you are not well prepared...perhaps another time ...sir.'")
									
									print("[Lawrance stands and slowly walks out of the room...]")
									ending = "9"
									area = "ENDING"
							else:
								print(name + ": 'This is the explaination that you are guilty...'")
								
								print("[Lawrance lets out a sudden chuckle]")
								
								print("[Coleridge raises an eyebrow..]")
								
								print("Lawrance: 'I-I'm afraid I don't understand..could you explain it to me?'")
								
								print(name + ": ''Well ...this ...uh...'")
								
								print("Lawrance: 'Yes?'")
								
								print(name + ": 'This....basically..'")
								
								print("Lawrance: 'It seems..you are not well prepared...perhaps another time ...sir.'")
								
								print("[Lawrance stands and slowly walks out of the room...]")
								ending = "9"
								area = "ENDING"
					if(intPrompt == "4"):
						print(name + ": 'Thank you Lawrance...that's all I needed from you.'")
						
						print("Lawrance: 'Okay, can I leave now?'")
						
						print(name + ": 'Yeah go ahead.'")
						
						print("Lawrance: 'Thank you.'")
						
						print("[Lawrance gets up and takes off]")
						break
#---------------------AREA 9: FINAL CONFRONTATION-----------------------
	if(area == "9"):
		print("Coleridge: 'For sure...it's either baldy or the kid.'")
		
		print("Captain Faust: 'There's still so much unanswered questions...'")
		
		print(name + ": 'Aye..and it's about time we tie it all up.'")
		
		print("Guard: 'Captain, they're ready.'")
		
		if(partnerRel >= 20):
			print("Coleridge: 'Let's end this partner.'")
			
		else:
			print("Coleridge: 'Let's get this over with.'")
			
		print(name + ": 'Yeah.'")
		
		print("[Both you and Coleridge enters sitting opposite of Father Cornealius and Lawrance...]")
		
		print("[Captain Faust awaits at the door...]")
		
		print(name + ": 'Father Cornealius, Lawrance, we all know that one of you is guilty.'")
		
		print(name + ": 'And that both of you have lied a great deal to us.'")
		
		print(name + ": 'Here..if not one then both of you will walk out in cuff.'")
		
		print(name + ": 'Let's end this and bring Father Merwin the justice he deserves...'")
		
		print("Father Cornealius: 'I couldn't agree more.'")
		
		print("[Lawrance gives a subtle nod...]")
		
		print(name + ": 'Let's start with what we know...'")
		
		print(name + ": 'Lawrance didn't run from the orphanage he was kicked out. He was a troubled youth supposedly.'")
		
		print(name + ": 'Father Cornealius, you took him in. Father Merwin didn't like it.'")
		
		print(name + ": 'But because of his respect for Father Cornealius, he abide by Lawrance living with him ..that is until..'")
		
		print(notepadEntry)
		print(invArray)
		print("TYPE IN THE EVIDENCE NAME")
		Evidence1 = input("")

		if(Evidence1 == "Miras Testimony(Theft)"):
			print(name + ": 'You stole something and Father Merwin caught you.'")
			
			print("Lawrance: 'I didn't steal anything!'")
			
			print("Father Cornealius: 'You accuse us of murder and now accuse Lawrance of thievery?!'")
			
			print(name + ": 'I'm not just accusing him. I'm saying he did do it. You stole Gendel the Blacksmith's heirloom didn't you?'")
			
			print("Father Cornealius: 'Am I to expect solid proof or do you based it on more rumors?'")
			
			print(name + ": 'Why don't you let him answer father. Would we find Gendel's Rock in your possession in the church Lawrance?'")
			
			print("Lawrance: 'I...I-'")
			
			print(name + ": 'Don't take what I said the wrong way, I have yet to claim Lawrance was the killer but a thief for certain.'")
			
			print("Lawrance: 'I...I was never there...'")
			
			print(name + ": 'Really? What do you think when I tell you I have proof that you were?'")
			
			print(notepadEntry)
			print(invArray)
			print("TYPE IN THE EVIDENCE NAME")
			Evidence2 = input("")

			if(Evidence2 == "Handprint in Gendels"):
				print(name + ": 'Gendel's place is covered in dust. Especially his storage closet.'")
				
				print(name + ": 'On his closet window, I found what appears to be a handprint. Too tall to be Gendel's and far too big.'")
				
				print(name + ": 'If we are to go down to Gendel's now and press your hand against that window, would we see something similar?'")
				
				print("Father Lawrance: 'Fine, I-I admit it...I stole the heirloom ..but that's all I did!'")
				
				print(name + ": 'And did Father Merwin caught you?'")
				
				print("Lawrance: 'No! Father Merwin never saw anything!'")
				
				print("[Coleridge leans over in a whisper]")
				
				print("Coleridge: 'I hate to tell ya kid but you have no evidence of when the father die.'")
				
				print("Coleridge: 'You can prove the kid took the rock but no indication that he was caught.'")
				
				print(name + ": 'That's true...'")
				
				print("Coleridge: 'From here on out, this is more or less a leap of faith.'")
				
				print(name + ": 'Perhaps all we need to do is make them confess a motivation.'")
				
				print("Coleridge: 'So we're just gonna make random jab at their motivation till one cracks?'")
				
				print(name + ": 'You have another idea?'")
				
				print("Coleridge: 'Nah...'")
				
				print("Coleridge: 'Either the kid witness the father killing another father or the kid did it himself.'")
				
				print("Coleridge: 'We don't know the time between Merwin's death and when the stone was taken...'")
				
				print(name + ": 'I'm impressed..you actually pay attention to the investigation.'")
				
				print("Coleridge: 'Hey kid..I still have my job for a reason.'")
				
				print(name + ": 'Father Cornealius, I've been wondering...why is it that Lawrance specifically you took under you.'")
				
				print("Father Cornealius: 'Excuse me?'")
				
				print(name + ": 'I'm asking you..of all the troubled youth in this city..why Lawrance?'")
				
				print(name + ": 'What would make you sacrifice so much for him? Even ...murder.'")
				
				print(name + ": 'Pardon me, if you killed Father Merwin that is...'")
				
				print("Father Cornealius: 'I...Lawrance came to me..and I would not turn him away...'")
				
				print(name + ": 'But why just Lawrance..certainly a man generous enough to give Coleridge money would take on more troubled youth...'")
				
				print("Father Cornealius: 'Are you questioning my generousity?'")
				
				print(name + ": 'No ..just your motivation..I think there's a reason you took Lawrance specifically...'")
				
				print(notepadEntry)
				print(invArray)
				print("TYPE IN THE EVIDENCE NAME")
				Evidence3 = input("")

				if(Evidence3 == "Miras Testimony on Father Cornealius"):
					print(name + ": 'He's your son.'")
					
					print("Father Cornealius: '...'")
					
					print(name + ": 'You constantly defend him...speak for him...took him under your wing...'")
					
					print(name + ": 'I think of no other but a parent who would sacrifice so much...'")
					
					print("Father Cornealius: 'How ridiculous..I am a priest..can a man not simply be generous?! And none of this is truth!'")
					
					print("Father Cornealius: 'Nothing but rumors and theories!'")
					
					print("Father Cornealius: 'NOTHING!'")
					
					print(name + ": 'You just told us why you killed Father Merwin, Father Cornealius.'")
					
					print(name + ": 'Did Father Merwin come to the same conclusion? You fathered a bastard..and more important a troubled one.'")
					
					print(name + ": 'I bet, when Father Merwin question you why you defend Lawrance and took him in..he found out.'")
					
					print(name + ": 'You had a child and you know it.'")
					
					print("Lawrance: 'I am sorry father..but I must confess...I saw him ...I saw him hit Father Merwin...in that alley..'")
					
					print("[Lawrance begin to sob....]")
					
					print("Lawrance: 'I'm sorry...h-he said ...my father..he asked me to...to lie...I'm sorry!'")
					
					print("[Father Cornealius looks at Lawrance with wide eyes...he slowly sits and lower his head...]")
					
					print("Father Cornealius: '...Yes..I confess ..to all of it...I killed Father Merwin...I'm sorry I made you lie Lawrance..'")
					
					print("Father Cornealius: 'I...I killed him ..Father Merwin ..confronted me and...he was about to tell everyone..'")
					
					print("Father Cornealius: 'I..I could not allow him..so I took the brick and I smashed his head in...'")
					
					print("Father Cornealius: 'And then..I tried to hide the body..so I broke the basement lock to the general store..'")
					
					print("Father Cornealius: 'I only managed to hide his cloak...but his body..it was too heavy..there was..too much people...'")
					
					print("Father Cornealius: 'So I left him there...'")
					
					print("Captain Faust: 'Father Cornealius! You are under arrest for the murder of Father Merwin!'")
					
					print("[Captain Faust and several guards walks over to the priest and lift him off his chair as Lawrance cries...]")
					
					print("Coleridge: '....'")
					
					print("1. 'Coleridge..wanna get a drink?' \n2. 'Hold it!'")
					final = input("")

					if(final == "1"):
						print("Coleridge: ''Hm? Yes course!")
						
						print(name + ": 'Yeah..your treat right?'")
						
						print("Coleridge: 'Ha! Of course this one's on me rookie..next one though'")
						
						print(name + ": 'We'll talk about that when it comes.'")
						
						print("Coleridge: 'Right!'")
						
						ending = "11"
						area = "ENDING"
					if(final == "2"):
						print(name + ": 'HOLD IT!'")
						
						print("[Coleridge let out a smile...]")
						
						print("[The guards pauses]")
						
						print("[Lawrance's crying stops and he grinds his teeth....]")
						
						print(name + ": 'FATHER CORNEALIUS IS INNOCENT! LAWRANCE IS THE GUILTY ONE!'")
						
						print("Father Cornealius: 'No! I already confessed it was me!'")
						
						print(name + ": 'Father Cornealius..did you see Merwin's body?'")
						
						print("Father Cornealius: 'Of course! I was the one who identified him!'")
						
						print(name + ": 'My partner..did he tell you how he died?'")
						
						print("Father Cornealius: 'Yes! Struck in the head multiple times!'")
						
						print("Father Cornealius: 'What does this prove?!'")
						
						print(name + ": 'THAT YOUR CONFESSION CONTRADICT WHAT REALLY HAPPENED!'")
						
						print(name + ": 'THE REAL MURDER WEAPON IS NOT A BRICK...IT'S....'")
						
						print("")
						print(notepadEntry)
						print(invArray)
						print("The murder weapon itself is not in your inventory but there is something that links to the murder weapon...")
						print("TYPE IN THE EVIDENCE NAME")
						Evidence4 = input("")

						if(Evidence4 == "White Solid Substance"):
							print(name + ": 'THE CANDLE IN THE CHURCH!'")
							
							print(name + ": 'FATHER MERWIN DID DIE OF BLUNT FORCE TRAUMA!'")
							
							print(name + ": 'BUT HIS FACE WAS BURNT BY SOMETHING HEATED!'")
							
							print(name + ": 'SUCH AS AN OBJECT LIKE A CANDLE AND THE WAX THAT HAS FALLEN ON TO FATHER MERWIN!'")
							
							print(name + ": 'UNLESS FATHER CORNEALIUS TRULY COMITTED THE CRIME, THE ONLY POSSIBLE PERSON WAS...LAWRANCE!!'")
							
							print("[Lawrance began to laugh...]")
							
							print("Lawrance: 'Damn..you can't just leave it alone? ....You can't even lie properly...you useless old fart...'")
							
							print("Lawrance: 'DAMN DAMN DAMN DAMN DAMN DAMN DAMN DaMn dAmN DAmn dAmn DaMn daMN WHY WON'T YOU LEAVE ME ALONE.?!'")
							
							print("Lawrance: 'YEAH I KILLED THAT IGNORANT SHIT, ALWAYS TELLING ME TO REPENT AND BOW BEFORE SOME ROCK'")
							
							print("Lawrance: 'THE ASS WAS SO IRRITATING...ALWAYS YELLING AND SHOUTING AND WHEN I CAME BACK FROM THAT MIDGET...'")
							
							print("Lawrance: 'HE STOOD THERE WITH THOSE BLOODY EYES JUST STARING..JUST STARING...I HATE IT!'")
							
							print("Lawrane: 'SO YEAH I DID THE SAME TO HIM WHAT I DID TO THOSE ANNOYING KIDS IN THE ORPHANAGE.'")
							
							print("Lawrance: 'HE ....THEY ...WON'T SHUT UP SO I DID IT FOR THEM!'")
							
							print("Lawrance: 'I SQUEEZE THOSE PUTRID NECK OF THEIR AND SQUEEZE AND SQUEEZE'")
							
							print("Lawrance: 'BUT THIS ASS..HE WASN'T A KID NO..SO I GRABBED THE CANDLE AND I HIT HIM!'")
							
							print("Lawrance: 'OVER AND OVER AGAIN TILL HIS FACE WAS BURNING!'")
							
							print("Lawrance: 'EACH TIME I HIT HIM HE GROWS MORE AND MORE SILENCE, HIS FACE BURNT FROM MY MIND!'")
							
							print("Lawrance: 'I KILLED HIM AND I'D DO IT OVER AND OVER AND OVER AGAIN IF I CAN!'")
							
							print("Lawrance: 'SCREW MERWIN, SCREW YOU, SCREW CORNEALIUS, ALL OF YOU CAN BURN!'")
							
							print("Captain Faust: 'ARREST HIM!'")
							
							print("Father Cornealius: '....How...how can it ....'")
							
							print("Lawrance: 'YOU OLD FART I'LL FINISH THE JOB...I'LL KILL YOU!'")
							
							print("Lawrance: 'YOU ABANDONED ME IN THAT ORPHANAGE! YOU THINK I DIDN'T KNOW?! I'LL KILL YOU!'")
							
							print("[Father Cornealius collaspes on his knee sobbing...]")
							
							print("[Captain Faust and a handful of guards restrain Lawrance and drags him away...]")
							
							print("Coleridge: 'Father Cornealius..you are under arrest for accessory to murder...'")
							
							print("[Another guard enters and drag Cornealius away...]")
							
							print(name + ": 'You knew didn't you?'")
							
							print("Coleridge: 'What? Ya think the captain kept me around for my charming personality?'")
							
							print(name + ": 'Hah...let's go ..I'm beat.'")
							
							print("Coleridge: 'Damn right. Dinner then my treat!'")
							
							print(name + ": 'Ha! You're generous ..we should invite Mira..and Eidar and probably Gendel too.'")
							
							print("Coleridge: 'The more the merrier! This is only a once in a lifetime thing kid. Ya know..you're not bad.'")
							
							print(name + ": 'Thanks Coleridge...now lets go..I'm gonna empty your coin pouch.'")
							
							print("Coleridge: 'Hell I was just gonna goto one of those cheap street store.'")
							
							print("Coleridge: 'But fine..since we're celebrating your first case close...as you wish.'")
							
							print(name + ": 'This will probably never happen again will it?'")
							
							print("Coleridge: 'Not in your lifetime rookie. Savior it.'")
							
							print(name + ": 'I will partner.'")
							
							print("Coleridge: 'Aye.'")
							
							ending = "12"
							area = "ENDING"
					else:
						print("Lawrance: 'Heh...that's ridiculous...'")
						
						print(name + ": 'Wha...'")
						
						print("Father Cornealius: 'It seems...I am guilty after all..'")
						
						print(name + ": 'W-Wait I know what the murder weapon is!'")
						
						print("Captain Faust: 'It doesn't seem like you do...we have a confession and nothing else that says otherwise...'")
						
						print("Captain Faust: 'Father Cornealius...you are under arrest.'")
						
						ending = "11"
						area = "ENDING"
				else:
					ending = "10"
					area = "ENDING"
			else:
				ending = "10"
				area = "ENDING"
		else:
			ending = "10"
			area = "ENDING"
#-----------------------ISOLATED AREAS----------------------------------
	if(area == "100"):
		print("____________________________________________")
		print("Coleridge: 'Well since its your bright ass idea to investigate this...You can take lead.'")
		
		print("1. 'Maybe you should take responsibility...(Confront) \n2. 'Fine...'(Accept) \n3. 'What? No!'(Resist) \n4. 'Fine..but..'(Compromise)")
		dialogueAVa = input("")

		if(dialogueAVa == "1"):
			print(name + ": 'Maybe you should take responsibility as well.'")
			
			print(name + ": 'This is your case as well as mine and even if we didn't find that body, in the end it will still become our case.'")
			
			print("Coleridge: 'And you know this how?'")
			
			print(name + ": 'Because it's our job Coleridge'")
			
			print("Coleridge: 'And I was expecting an answer like, I'm psyhic..'")
			
			print("1. 'Is this a game to you?!'(Push) \n2. 'Nevermind..'(Back Off)")
			dialogueAVa1 = input("")

			if(dialogueAVa1 == "1"):
				print(name + ": 'Is this a game to you?!'")
				
				print(name + ": 'Why would you become a city guard if this is all a joke for you?!'")
				
				print("Coleridge: 'It pays well..now do we have a murderer to catch or you want to keep interrogating me?'")
				
				print(name + ": 'Ugh...'")
				
				partnerRel = partnerRel - 1

			if(dialogueAVa1 == "2"):
				print(name + ": 'Nevermind. There doesn't seem to be any point in talking.'")
				
				print("Coleridge: 'Smartest thing you've said all day kid.")
				
				partnerRel = partnerRel + 2

		if(dialogueAVa == "2"):
			print(name + ": 'Fine..I'll take lead in this case.'")
			
			print("Coleridge: 'Good, because I sure as hell won't.'")
			
			partnerRel = partnerRel + 2

		if(dialogueAVa == "3"):
			print(name + ": 'What? No! I'm only a rookie!'")
			
			print("Coleridge: 'And yet we're in this case because of you...")
			
			print(name + ": 'We were patrolling the area. It would've been our case even if we didn't find the body.'")
			
			print("Coleridge: 'Like you said, you're the rookie. So I say, you're incharge of this case.")
			
			print(name + ": 'But...'")
			
			print("Coleridge: 'And think of it this way kid. This'll be good experience for you.'")
			
			print("Coleridge: 'Now get going.'")
			
			print(name + ": ''Okay..fine.")
			
			partnerRel = partnerRel + 3

		if(dialogueAVa == "4"):
			print(name + ": 'Fine..but you really should take this seriously.'")
			
			print("Coleridge: 'I am taking it seriously. That's why I'm putting you incharge.'")
			
			print("Coleridge: 'A four years old wouldn't trust me with his candies.'")
			
			print(name + ": 'Worst part is, I think I actually believe you.'")
			
			print("[Coleridge gives a big smile]")
			
			partnerRel = partnerRel + 5

		print("Coleridge: 'So, where to first rookie?'")
		
		print(name + ": 'Lets return to the scene of the crime first.'")
		
		print("Coleridge: 'Off we go then.'")
		
		area = "4.2"
	if(area == "100.1"):
		print("____________________________________________")
		print("Coleridge: 'So where to next?'")

		if(blacksmith == False and genStore == False and church == False):
			while(True):
				print("1. Talk to Coleridge \n2. Goto the Blacksmith \n3. Goto the General Store \n4. Goto the Church")
				dialogueAVb = input("")

				if(dialogueAVb == "1"):
					print(name + ": 'What do you think so far?'")
					
					print("Coleridge: 'Whats to think? We've only just started.'")
					
					print("Coleridge: 'The guard said there's three place round here right? Let's look in those places then.'")
					
					dialogueColeridge = True
				if(dialogueAVb == "1" and dialogueColeridge == True):
					print("Coleridge: 'I already told you what I think. Get going already!'")
					
					partnerRel = partnerRel - 2
				if(dialogueAVb == "2"):
					print(name + ": 'Lets head to the blacksmith.'")
					
					area = "5"
					break
				if(dialogueAVb == "3"):
					print(name + ": 'Lets take a look at the general store.'")
					
					area = "6"
					break
				if(dialogueAVb == "4"):
					print(name + ": 'We'll see if the church has anything.")
					
					print("Coleridge: 'Well don't mind me. Do go ahead.'")
					area = "7"
					break
		while(True):
			for x in range(0, 3):
				print(countArray[x] + locationArray[x])

			nextLocation = input("")
			if(nextLocation == "1"):
				if(blacksmith == False):
					print(name + ": 'Lets head to the blacksmith next.'")
					
					print("Coleridge: 'Lead the way.'")
					
					area = "5"
					break
				if(blacksmith == True):
					print(name + ": 'I want to head to the blacksmith again...'")
					
					print("Coleridge: 'What for? It's just gonna be a waste of time.'")
					
					print(name + ": 'Yeah perhaps...'")
			if(nextLocation == "2"):
				if(genStore == False):
					print(name + ": 'Let's head to the general store now.'")
					
					print("Coleridge: 'Yes!'")
					
					print(name + ": 'You seem very happy about that.'")
					
					print("Coleridge: 'Damn right I am. That place is a pawn shop.'")
					
					print("Coleridge: 'You won't believe the stuff people throw away.'")
					
					print("[Coleridge walks quickly towards the general store]")
					
					print("Coleridge: 'Cmon rookie keep up!'")
					
					area = "6"
					break
				if(genStore == True):
					print(name + ": 'I want to revisit the general store again...'")
					
					print("Coleridge: 'Look kid, as much as I like like to visit the lady again..'")
					
					print("Coleridge: 'Its just gonna be a waste of time.'")
					
					print(name + ": 'Didn't think you would pass on a trip back to the store.'")
					
					print("Coleridge: 'Well I still very much prefer to end this case'")
					
					print(name + ": 'Hm..I guess I can agree to that.'")
			if(nextLocation == "3"):
				if(church == False):
					print(name + ": 'Let's head to the church.'")
					
					print("Coleridge: 'Ah great I'll bring the dononation.'")
					
				if(church == True):
					print(name + ": 'Perhaps we should return to the church.'")
					
					print("Coleridge: 'No ho freaking way. That was too much for me man.'")
					
					print(name + ": 'Too much? Too much of what?'")
					
					print("Coleridge: 'Too much silence..it creeps the living hell outta me.'")
					
					print(name + ": 'Fine, we can go back another time.'")

		if(blacksmith == True and genStore == True and church == True):
			print("____________________________________________")
			print(name + ": 'Well that's it. That's all the places.'")
			
			print("Coleridge: 'Yeah, I think the scholar should be all waiting for us now.'")
			
			print(name + ": 'Yeah, let's return to the barrack.'")
			investigateEnd = True
			area = "3"
#-------------------------------------------------------------
	if(area == "ENDING"):
		if(ending == "1"):
			print("You screwed up man...after accusing the captain of the murder, he assigned someone else on the case and unfortunately unable to close it either but at least they didn't accuse their captain of a murder. The captain however, was in a generous mood and instead of firing you, you are now demoted to cleaning toilet alongside Coleridge who just really really hates you...")
			time.sleep(30)
			break
		if(ending == "2"):
			print("Well ...you tried to accuse your partner of a murder that takes place when he was standing next to you. Only possible explaination is you're either high or drunk or both. Eventually you were demoted to a desk job but ..hey at least Coleridge always welcomes you as a drinking buddy now despite the fact you tired to accuse him of murder....")
			time.sleep(30)
			break
		if(ending == "3"):
			print("After shocking the messenger boy quite terribly, he went home still somewhat dazed. You got demoted as expected and the case was passed along to someone else. You lost Coleridge as partner and instead become confined in some desk job for the rest of your life never to put on an actual uniform again but hey the good news is, you lost your job the day after because nobody woke you up till the afternoon.")
			time.sleep(30)
			break
		if(ending == "4"):
			print("After accusing Gendel with unsufficent evidnece, he was released as expected..and frankly so were you from the case for misconduct after the blacksmith rant and complain to everyone about harresment. Let's just say, afterward, the Coronian guards aren't expecting any friendly business from Gendel and his heirloom was forever lost to him....")
			time.sleep(30)
			break
		if(ending == "5"):
			print("Well..you accused a little old lady of murder. Unfortunately, afterward Coleridge refuses to work with you but under Faust order, he continues to but accusing the old lady certainly didn't help the guard's reputation. After doing an unsatisfactory job, you were demoted to minial guards alongside Coleridge who looks at you like you're shit every day since...")
			time.sleep(30)
			break
		if(ending == "6"):
			print("You manage to close the case and arrest Eidar the homeless. Despite constant protest from Eidar he was nevertheless thrown into the dungeon and given a death sentence. You were promoted by Captain Faust but continue to work besides Coleridge to solve homicide. Several months following the case, shortly before Eidar's execution, he makes one last claim to deny his accused crime....")
			time.sleep(30)
			break
		if(ending == "7"):
			print("Unable to prove Eidar's guilt you were not able to make an arrest. The captain wasn't so generous as to provide you with a second chance and the case was given to someone else. The case remained unsolved and life continues as you continue your job as another regular guard...")
			time.sleep(30)
			break
		if(ending == "8"):
			print("Unable to gather the proper evidence to convict Father Cornealius he walked free and the case was never solved. However, given that this is your first case and second day, the captain pardon you and you continue your life as a regular guard besides Coleridge...")
			time.sleep(30)
			break
		if(ending == "9"):
			print("Unable to find evidence against Lawrance, the case remain very much closed. Even if the evidence have present itself, it is already too late for Lawrance have long departed from Corona the day after his interview. No consequences were given providing that this is your first case and second day on the job, life goes on and you continue as a small guard in this big city alongside Coleridge....")
			time.sleep(30)
			break
		if(ending == "10"):
			print("Father Cornealius: 'You sadden me...you've accuse a member of the clergy..of killng another...'")
			
			print("Father Cornealius: 'Or worst, you accuse a child bearing a stigma for his past mistakes...'")
			
			print(name + ": 'Hold it father, I can explain.'")
			
			print("Father Cornealius: 'No ..you cannot. I grief for my friend and you dare hold this harresment..this farst in our face...'")
			
			print("Father Cornealius: 'I can tell you don't know what you're doing.'")
			
			print(name + ": 'Hold it one moment!'")
			
			print("Father Cornealius: 'What do you intent to hold me and Lawrance with hm? Theory and rumors?'")
			
			print("Father Cornealius: 'If you do not intent to arrest us..then goodbye.'")
			
			print("[Father Cornealius and Lawrance walks out...]")
			
			print("Coleridge: 'Can they just do that?'")
			
			print("Captain Faust: 'He's right...I-I don't see any worthy evidence...'")
			
			print(name + ": '..Shit.'")
			
			print("Coleridge: 'It's alright kid..no one can win them all.'")
			
			print("Unable to break Father Cornealius or Lawrance, the two walk free. Even after trying to pursuit the case, the two have left the city the day afterward. The case remains close and justice was never found but as Coleridge says, you can't win them all. Life continues....")
			time.sleep(30)
			break
		if(ending == "11"):
			print("Alas...justice have been claimed for Father Merwin...Father Cornealius sits in the dungeon awaiting the execution block...you were promoted as your first case on your first day was an immediate success. Coleridge however...refuse to continue as your partner. Unable to convince Coleridge other wise...you alone rise in rank as homicide investigators...justice was served...or..was it?")
			time.sleep(30)
			break
		if(ending == "12"):
			print("With justice found for Father Merwin, you were immediate promoted for a job well done on your first case, and second day. With Coleridge as your mentor, the two of you quickly rise as homicide investigators. What was an insiginifcant tale soon become a story of grandeur as you alongside your partner become one of the most famous pair in homicide investigation....")
			time.sleep(30)
			break
