def likes(names):
	if len(names) == 0:
		return "no one likes this"
	elif len(names) == 1:
		return "{} likes this".format(names[0])
	elif len(names) == 2:
		return "{} and {} likes this".format(names[0], names[1])
	elif len(names) == 3:
		return "{}, {} and {} likes this".format(names[0], names[1], names[2])
	 else:
		other_people = len(names) - 2
		return "{}, {} and {} others like this".format(names[0], names[1], other_people)
