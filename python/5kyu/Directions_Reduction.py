#https://www.codewars.com/kata/directions-reduction/train/python

#Once upon a time, on a way through the old wild west,…

#… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too. Going to one direction and coming back the opposite direction is a needless effort. Since this is the wild west, with dreadfull weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!
#How I crossed the desert the smart way.

#The directions given to the man are, for example, the following (depending on the language):

#["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].

#or

#{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };

#or

#[North, South, South, East, West, North, West]

#You can immediatly see that going "NORTH" and then "SOUTH" is not reasonable, better stay to the same place! So the task is to give to the man a simplified version of the plan. A better plan in this case is simply:

#["WEST"]

#or

#{ "WEST" }

#or

#[West]

#Other examples:

#In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going north and coming back right away. What a waste of time! Better to do nothing.

#The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other, therefore, the final result is [] (nil in Clojure).

#In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH" are not directly opposite but they become directly opposite after the reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].
#Task

#Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

#Notes

#    Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible. "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other and can't become such. Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].

#    if you want to translate, please ask before translating.





def dirReduc(arr):
	pred = ""
	new_a = []
	found = True
	a = arr

	while found:
		found = False
		for d in a:
			if (d == "NORTH" and pred == "SOUTH") or (d=="SOUTH" and pred == "NORTH") or (d == "EAST" and pred == "WEST") or (d == "WEST" and pred == "EAST"):
				new_a = new_a[:-1]
				found = True
			else:
				new_a.append(d)
			pred = d 
			
			if not found:
				pred = d 
			else:
				pred = ""

		a = new_a
		new_a = []
	return a
    