#Michael Ladderbush

#!/usr/bin/perl -1 
use v5.10;
use strict;
use warnings;

	#this is just a simple introduction for the player using print.

print ("\n-Cave Explorer, use directions or actions to traverse the cave.-\n");
print ("-By: Michael Ladderbush-\n");

	#these are the lists and variables that will hold information relating to the items the user possesses as well as how far they have traversed the cave.

our @items;
our $flashlightEvent = 0;
our $pocketknifeEvent = 0;
our $ropeEvent = 0;
our $ropeEventTwo = 0;
our $escapeEvent = 0;
our $escapeTime = 0;
our $treasure = 1;
our $attempts = 0;
our $direction = 0;

#this is a subroutine that runs through the escapeEvent, this is used once the end of the cave is reached and the player has to reach the end before the variable reaches 
#a certain point.

sub escapeEvent { 

	if ($escapeEvent == 1) {

		$escapeTime = $escapeTime + int(rand(5));

			if ($escapeTime >= 10) {
	
				goto DEATH;

			}
	}	
}

#this is a subroutine that is used to ask the user for input.

sub inputPrompt {
	
	print ("\n	>Type an available direction left/right/straight/back or pockets to look at what you have:");
	our $direction = <STDIN>;
	chomp($direction);

}

#this subroutine is just to display when the user has no items.

sub emptyPockets {

	$direction = 0;
	print ("\nYou find a few dust bunnies.\n");
	goto ESCAPE;

}

#this subroutine displays the users items and runs the escapeEvent subroutine and the emptyPockets subroutine if necessary.

sub pockets {

	$direction = 0;
	escapeEvent();
	if (@items >= 1){

		print("\n@items\n");
		$direction = 0;
	
	}else {

		emptyPockets();

	}
}

#this subroutine is used for when the user goes a direction with nothing left to interact with.

sub wrongWay {

	print("\nYou bump into a wall and take a few steps back.\n\n");
	$direction = 0;

}

START:

inputPrompt();

	#this is the first of many if, elsif, else statements that take the users directional input and give a story event based on their decision.

given ($direction){

	when('left'){
	
		$direction = 0;
		escapeEvent();

		if ($flashlightEvent == 1){

			print ("\nYou are in a tiny room with a light shining from above and a small tunnel behind you.\n");

			#this is a goto that directs the program back to the keyword where it will then continue to run.

			goto LEFT1;

		}else{

			#After the user passes through this if-else statement the variable $flashlightEvent is set to 1, so that if the user comes back to this section of the
			#game they will not recieve the same output.

			print("\nYou squeeze through the tunnel and make your way into a tiny room with a light shining from above. On the ground you find a worn flashlight.\n");
			$flashlightEvent = 1;
			push(@items, ("Worn Flashlight\n\n"));
			goto LEFT1;

		}
	}


	when('right'){	

		escapeEvent();
		print("\nYou walk through the tunnel to your right and enter a pitch black room. You can feel a breeze from straight ahead.\n\n");
		$direction = 0;
		goto RIGHT1;

	}

	when('straight'){

		escapeEvent();
		wrongWay();
		goto START;	
			
	}
		
	when('back'){

		#this is for the end of the game, it checks whether the player won or lost and then exits.

		if ($escapeEvent == 1) {

			if ($treasure == 1){

				print("You escaped the cave with the gems. Congratulations!!!");
				sleep 20;
				exit;

			}else {

				print("At least you survived...");
				sleep 20;
				exit;

			}

		}else{

			$direction = 0;
			print ("\nThe entrance to the cave.\n");
			goto START;

			#typing pockets outputs the list of items the player has collected

		}
	}

	when('pockets'){

		pockets();
		goto START;

	}

	default { 

		$direction = 0;
		goto START;

	}

}
	
#this is the next goto, it brings the user left and again prompts them for a direction.



LEFT1:

	inputPrompt();

	if ($direction eq 'left') {

		escapeEvent();
		wrongWay();
		goto LEFT1;

	}elsif ($direction eq 'right'){
	
		escapeEvent();
		wrongWay();
		goto LEFT1;

	}elsif ($direction eq 'straight'){

		escapeEvent();
		wrongWay();
		goto LEFT1;

	}elsif ($direction eq 'back'){

		escapeEvent();	
		print("\nYou crawl back through the tunnel into the first room.\n");
		$direction = 0;
		goto START;

	}elsif ($direction eq 'pockets') {

		pockets();
		goto LEFT1;

	}else {

		goto LEFT1;

	}

#the next goto that is used when the user goes right.

RIGHT1:

inputPrompt();

	if ($direction eq 'left') {

		escapeEvent();
	
		#this is an extra if statement that checks if the user has tried this route before and if they have they will lose the game.

		if ($attempts == 0){

			print("\nYou trip in the darkness and hit your head! Don't walk around in the dark!\n\n");
			$direction = 0;
			$attempts = 1;
			print("You are in a pitch black room, the entrance is behind you and there is a breeze coming from straight ahead.\n\n");
			goto RIGHT1;

		}else {
		
			print("\nYou fall into a chasm and perish. Try again!\n");
			$attempts = 0;
			sleep 10;
			exit;

		}
	
	}elsif ($direction eq 'right') {

		escapeEvent();
		wrongWay();
		print("You are in a pitch black room, the entrance is behind you and there is a breeze coming from straight ahead.\n\n");
		goto RIGHT1;

	}elsif ($direction eq 'straight'){

		escapeEvent();
		print("\nThe breeze grows in strength as you reach an opening in the wall.\n\n");
		$direction = 0;
		print("It's too dark to tell what could be in the opening. There must be another way.\n\n");
		print("You are in a pitch black room, the entrance is behind you and there is a breeze coming from straight ahead.\n\n");
		goto RIGHT1;

	}elsif ($direction eq 'back'){

		escapeEvent();
		print("\nYou walk back into the first room.\n");
		$direction = 0;
		goto START;

	}elsif ($direction eq 'pockets') {
	
	escapeEvent();

		if (@items >= 1){

			pockets();
			print("You use the flashlight to illuminate the room!\n");
			goto RIGHT2;

		}else {

			print("\nYou are in a pitch black room, the entrance is behind you and there is a breeze coming from straight ahead.\n\n");
			goto RIGHT1;

		}
	
	}else {

		$direction = 0;
		print("You are in a pitch black room, the entrance is behind you and there is a breeze coming from straight ahead.\n\n");
		goto RIGHT1;

	}

#The goto for when the player activates the flashlight by checking their pockets.
	
RIGHT2:

print ("\nYou can now see there is a large chasm to the left, a small opening in the wall straight ahead and ledge overhead to the right.\n");
inputPrompt();

if ($direction eq 'left') {	

	print("\nYou peer over the edge of the chasm, there is no bottom in sight....\n\n");
	$direction = 0;
	escapeEvent();
	if ($ropeEvent == 1){

		$direction = 0;
		print("\nYou wrap the rope around a stalagmite and begin traversing the chasm. You eventually reach the bottom and see a tunnel ahead.\n\n");
		goto CHASM1;

	}else{
		goto RIGHT2;
	}

}elsif ($direction eq 'right') {
	
	#the user is prompted to see if they want to climb up and then if they have climbed up before they are immediately put atop the ledge. 
	#if the user hasnt made it to the top of the ledge yet they are put at the next goto, which asks them for a solution of a simple math problem (placeholder for something 
	#more interesting). If the question is answered correctly the player is put on top of the ledge.

	print("\nYou approach the bottom of the ledge. Do you attempt to climb up?\n\n");
	$direction = 0;
	escapeEvent();
	print("Type 'yes' or 'no'\n");
	my $decision = <STDIN>;
	chomp($decision);

		if ($decision eq 'yes' && $ropeEventTwo == 1){

			$direction = 0;
			goto LEDGE;

		}elsif ($decision eq 'yes'){

			$direction = 0;
			goto CLIMBGAME;

		}else {

			$direction = 0;
			goto RIGHT2;
		}

}elsif ($direction eq 'straight'){

	$direction = 0;
	escapeEvent();
	
	#this is the pocketknife event which is essentially the same as the flashlight event.

	if ($pocketknifeEvent == 1){

		$direction = 0;
		print("\nThere's nothing else in the opening.\n\n");
		goto RIGHT2;

	}else {

		$direction = 0;
		print("\nUsing the flashlight you see something shining within the opening. You find a pocketknife and return to the entrance of the room!\n");
		$pocketknifeEvent = 1;
		push(@items, ("Pocketknife\n\n"));
		goto RIGHT2;

	}

}elsif ($direction eq 'back'){

	print("\nYou walk back into the first room and shut off your flashlight. \n");
	$direction = 0;

		if ($escapeEvent == 1) {

			$escapeTime = $escapeTime + int(rand(3));

				if ($escapeTime >= 10) {
	
					goto DEATH;

				}else{

					print("\nYou rush into the first room of the cave, you can see the entrance!!!\n");
					$direction = 0;
				}	
		}

	goto START;

}elsif ($direction eq 'pockets') {

	$direction = 0;
	escapeEvent();
	pockets();
	goto RIGHT2

}else {

	$direction = 0;
	goto RIGHT2;

}

CLIMBGAME:

#This prompts the user for a correct input in order to continue to the correct goto, otherwise they are sent back.

	our $climb1;
	print("Enter the answer of 1500/50 + 10 - 15 in time to make it up the ledge!!!\n\n");
	$climb1 = <STDIN>;
	chomp $climb1;

	if ($climb1 == 25) {

		print("You made it to the top!\n");
		$ropeEventTwo = 1;
		goto LEDGE;
	
	}else {

		print("You fell!\n");
		goto RIGHT2;

	}

#another goto for when the player reaches the top of the ledge.

LEDGE:

print ("\nStraight ahead you see a skeleton covered in tattered clothing. Below you is the breezy room.\n");
inputPrompt();

if ($direction eq 'left') {

	escapeEvent();
	wrongWay();
	goto LEDGE;

}elsif ($direction eq 'right'){

	escapeEvent();
	wrongWay();
	goto LEDGE;

}elsif ($direction eq 'straight'){

	$direction = 0;
	escapeEvent();
	if ($ropeEvent == 1){

		print("\nThere's nothing there but bones.\n");
		goto LEFT1;

	}else {

		print("\nYou rummage through the bones and find some rope!\n");
		$ropeEvent = 1;
		push(@items, ("Rope\n\n"));
		goto LEDGE;

	}

}elsif ($direction eq 'back'){

	print("\nKnowing the way back down you are able to make it to the floor unscathed.\n\n");
	$direction = 0;
	escapeEvent();	
	print("\n");
	goto RIGHT2;

}elsif ($direction eq 'pockets') {

	pockets();
	escapeEvent();
	$direction = 0;
	goto LEDGE;

}else {

	$direction = 0;
	goto LEDGE;

}

	#for when the player reaches the bottom of the chasm.

CHASM1:

$direction = 0;
inputPrompt();

if ($direction eq 'left') {

	$direction = 0;

		if ($escapeEvent == 1) {

			print("\nThe ceiling is falling behind you, hurry!");
			$escapeTime = $escapeTime + int(rand(5));

				if ($escapeTime >= 10) {

					goto DEATH;

				}else{

					wrongWay();
					print("You are in a small room with a tunnel straight ahead.\n");

				}	
		}	

}elsif ($direction eq 'right') {

	$direction = 0;

		if ($escapeEvent == 1) {

			print("\nThe ceiling is falling behind you, hurry!");
			$escapeTime = $escapeTime + int(rand(5));

				if ($escapeTime >= 10) {

					goto DEATH;

				}else{

					wrongWay();
					print("You are in a small room with a tunnel straight ahead.\n");

				}	
		}	

	goto CHASM1;

}elsif ($direction eq 'back'){

	$direction = 0;	

		if ($escapeEvent == 1) {

			$escapeTime = $escapeTime + int(rand(5));
			print("\nSuddenly theres a rock wall where the tunnel used to be!\n");
			
				if ($escapeTime >= 10) {
	
					goto DEATH;

				}else{


				}
		}

}elsif ($direction eq 'straight'){

	$direction = 0;

		if ($escapeEvent == 1) {

			$escapeTime = $escapeTime + int(rand(2));
			print("\nYou climb back up the rope but a falling rock has pinned you and your backpack! You can get your arms out but if you can't cut through you'll lose the treasure!\n");

				if ($pocketknifeEvent == 1){
			
					print("\nYou slice through the straps of the bag and grab the treasure! Good thing you found that pocketknife!\n");
					goto RIGHT2;

				}else{

					print("\nWhat a shame. You lost the treasure....\n\n");
					$treasure = 0;
					goto RIGHT2;

				}

		}

			if ($escapeTime >= 10) {
	
				goto DEATH;

			}else{	

				print("\nYou go through the tunnel, eventually reaching a dead end where you find a pile of gems!\n\n");
				goto ESCAPE;

		}
			
	print("\n");
	goto CHASM1;

}elsif ($direction eq 'pockets') {
	
	$direction = 0;
	pockets();
	escapeEvent();	
	$direction = 0;
	goto CHASM1;
	
}else {
	$direction = 0;
	print("\nYou are in a small room with a tunnel straight ahead.\n");
	goto CHASM1;
}

	#this is when the player is finally at the end of the cave, after this point the escapeEvent is changed to '1' and the player will be limited in the amount
	#of moves they can make. This is controlled by a random integer that adds to a variable every time a direction is input. The text of many points are changed 
	#once the event is changed.

ESCAPE:

$direction = 0;
$escapeEvent = 1;

print("\nSuddenly you feel the floor shaking beneath you, and small debris falling on your shoulders! It's a cave in!\n");
print("You'll only have a limited amount of time to get out the cave so choose your moves wisely\n\n");

inputPrompt();

if ($direction eq 'left') {

	escapeEvent();
	wrongWay();
	goto ESCAPE;

}elsif ($direction eq 'right'){

	escapeEvent();
	wrongWay();
	goto ESCAPE;

}elsif ($direction eq 'straight'){

	$escapeEvent = 1;
	$direction = 0;
	$escapeTime = $escapeTime + int(rand(3));

		if ($escapeTime >= 10) {
	
			goto DEATH;

		}

	print("\nYou race down the tunnel and reach the rope.\n\n");
	goto CHASM1;

}elsif ($direction eq 'back'){

	$direction = 0;
	$escapeTime = $escapeTime + int(rand(5));

		if ($escapeTime >= 10) {
	
			goto DEATH;

		}

	print("\nThe ceiling is collapsing! Run!!!\n\n");

}elsif ($direction eq 'pockets') {
	
	$direction = 0;
	if (@items >= 1){

		print("\n@items\n");
		$direction = 0;
		$escapeTime = $escapeTime + int(rand(5));

		if ($escapeTime >= 10) {
	
			goto DEATH;

		}

		goto ESCAPE;
	
	}else {

		print("\n");
		$escapeTime = $escapeTime + int(rand(5));
		if ($escapeTime >= 10) {

			goto DEATH;

		}

		$direction = 0;
		print ("You find a few dust bunnies.\n");
		goto ESCAPE;

	}

}else {

	$direction = 0;
	goto ESCAPE;

}

	#if the players $escapeTime reaches 10 they will lose the game and it will exit.

DEATH:

print("You took way too long and died :(  !!!");
print("Closing program in 20 seconds");
sleep 20;
exit;
