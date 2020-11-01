places = [
	'Gangtok',		# 0, -10
	'Bolivia',		# 1, -9
	'Agra',			# 2, -8
	'Munnar',		# 3, -7
	'Mysore',		# 4, -6
	'California',	# 5, -5
	'New York',		# 6, -4
	'Lake Ladakh',	# 7, -3
	'Manali',		# 8, -2
	'Jammu Kashmir'	# 9, -1
]

slice_1 = places[2:5]
print(slice_1)

slice_2 = places[2:]
print(slice_2)

slice_3 = places[:5]
print(slice_3)

slice_4 = places[:]
print(slice_4)

slice_5 = places[0:-5]
print(slice_5)