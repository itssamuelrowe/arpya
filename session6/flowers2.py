						#   <= -7 out of range
flowers = [
	'Lilly',			# 0, -6
	'Yellow Rose',		# 1, -5
	'Jasmine',			# 2, -4
	'Cauliflower',		# 3, -3
	'Lotus',			# 4, -2
	'Orchids'			# 5, -1
]						# >= 6 out of range

for i in range(-1, -len(flowers) - 1, -1):
	print(flowers[i])