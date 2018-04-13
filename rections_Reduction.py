"""
Once upon a time, on a way through the old wild west,…
… a man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too. Going to one direction and coming back the opposite direction is a needless effort. Since this is the wild west, with dreadfull weather and not much water, it's important to save yourself some energy, otherwise you might die of thirst!

How I crossed the desert the smart way.
The directions given to the man are, for example, the following:

		["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
		or

		{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
		or (haskell)

		[North, South, South, East, West, North, West]
"""

def dirReduc(arr):
	org=' '.join(arr)
	tmp=org
	while 1:
		tmp = tmp.replace('  ', ' ')
		tmp = tmp.replace('NORTH SOUTH', '')
		tmp = tmp.replace('SOUTH NORTH', '')
		tmp = tmp.replace('EAST WEST', '')
		tmp = tmp.replace('WEST EAST', '')
		if tmp == org:
			return [x for x in tmp.split()]
		else:
			org = tmp
