multiples_of_2 = [
	2,
	4,
	6,
	8,
	10,
	12,
	14,
	16,
	18,
	20
]
print(multiples_of_2)

# append method

multiples_of_3 = []
for i in range(1, 11):
	multiples_of_3.append(i * 3)
print(multiples_of_3)

multiples_of_4 = []
for i in range(1, 11):
	multiples_of_4.append(i * 4)
print(multiples_of_4)

# List comprehension

multiples_of_5 = [ i * 5 for i in range(1, 11) ]
print(multiples_of_5)