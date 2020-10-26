name = input('Enter your name: ')
age = int(input('Enter your age: '))

if age >= 18:
	print('You are allowed to vote.') # level 1

	if name == 'Arpya': # level 1
		print('Hi Arpya!') # level 2

	else: # level 1
		print('I don\'t know who you are.') # level 2
else:
	print('You are not allowed to vote.')

"""
# Alernatively, you can write the above program like this:

if age >= 18 and name == 'Arpya':
	print('You are allowed to vote.')
	print('Hi Arpya!')
elif age >= 18 and name != 'Arpya':
	print('You are allowed to vote.')
	print('I don\'t know who you are.')
else:
	print('You are not allowed to vote.')
"""