#This program prints the frequency of each letter or character in a block of text.
text = raw_input("Enter the block of text: ")

alphabet = "abcdefghijklmnopqrstuvwxyz.,!?"

text = text.lower()
filteredText = ""

for character in range(0, len(text)):
	for index in range(0, 30):
		if text[character] == alphabet[index]:
			filteredText = filteredText + text[character]

def count(value, tex):
	var = 0
	for num in range(0, len(tex)):
		if tex[num] == value:
			var += 1
	percent = round(var * 100.0 / len(tex), 2)
	if var > 1:
		print("\'" + value + "\' occurs " + str(var) + " times (" + str(percent) + "%)")
	elif var == 1:
		print("\'" + value + "\' occurs " + str(var) + " time (" + str(percent) + "%)")
		
for index in range (0, 29):
	count(alphabet[index], filteredText)
	
	
