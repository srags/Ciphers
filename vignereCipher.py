
text = raw_input("Enter the text you wish to encrypt: ")
keyword = raw_input("Enter the encryption key: ")

text = text.lower()
filteredText = ""

alphabet = "abcdefghijklmnopqrstuvwxyz.,!?"

for character in range(0, len(text)):
	for index in range(0, 30):
		if text[character] == alphabet[index]:
			filteredText = filteredText + text[character]
			
encrypText = ""

for index in range (0, len(filteredText)):
	digit = alphabet.index(keyword[index % len(keyword)]) + alphabet.index(filteredText[index])
	encrypText = encrypText + alphabet[digit % 30]

print encrypText 
	