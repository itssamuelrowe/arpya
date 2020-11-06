contacts = {
	"arpya": "+91 8861872440",
	"samuel": "+91 8310843835",
}

number_of_pairs = len(contacts)
print(number_of_pairs)

print("(before) arpya -> " + contacts["arpya"])
print("(before) samuel -> " + contacts["samuel"])

contacts["arpya"] = "+91 9898980000"
contacts["samuel"] = "+91 8888888888"

print("(after) arpya -> " + contacts["arpya"])
print("(after) samuel -> " + contacts["samuel"])

contacts["harry potter"] = "+1 1111111111"

print(contacts["harry potter"])