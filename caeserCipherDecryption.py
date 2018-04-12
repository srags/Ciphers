text = raw_input("Enter the text you wish to decrypt: ") #This is the encrypted text
encrypKey = raw_input("Enter the encryption key: ") #The encryption key is the character which corresponds to the number of spaces each character in the text has been moved.

alphabet = "abcdefghijklmnopqrstuvwxyz.,!?"
#Our alphabet consists of the 26 letters, a period, a comma, exclamation mark, and question mark.

#The filtered text is the original text in lower-case and all of the characters that aren't in our alphabet are removed.
filteredText = ""
for character in range(0, len(text)):
	for index in range(0, 30):
		if text[character] == alphabet[index]:
			filteredText = filteredText + text[character]
			
text = filteredText.lower()

numericKey = alphabet.index(encrypKey)

decrypText = ""
for character in range(0, len(text)):
	num = alphabet.index(text[character])
	decrypText = decrypText + alphabet[(num - numericKey) % 30]
	
print(decrypText)
#The final text is the orginal, decrpted text.
