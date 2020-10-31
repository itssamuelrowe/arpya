#  			0				1             2              3
names = [
	"Arpya Roy",
	"Samuel Rowe",
	"Sreem Chowdhary",
	"Ayushmann Khurrana"
]

# We know that range function gives us a sequence of integers.
# range(0, 10) -> 0,1,2,3,4,5,6,7,8,9

for i in range(0, 4):
	name = names[i]
	print(str(i) + " => " + name)

# I cannot add integer and string.

# print("index 0 => " + names[0])
# print("index 1 => " + names[1])
# print("index 2 => " + names[2])
# print("index 3 => " + names[3])


# names[i]