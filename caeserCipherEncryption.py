
text = raw_input("Enter the text you wish to encrypt: ")
encrypKey = raw_input("Enter the encryption key: ") #The encryption key is the character which corresponds to the number of spaces you wish to move each character in the text.

text = text.lower()
filteredText = ""
#The filtered text is the original text in lower-case and all of the characters that aren't in our alphabet are removed.

alphabet = "abcdefghijklmnopqrstuvwxyz.,!?"
#Our alphabet consists of the 26 letters, a period, a comma, exclamation mark, and question mark.

for character in range(0, len(text)):
	for index in range(0, 30):
		if text[character] == alphabet[index]:
			filteredText = filteredText + text[character]

numericKey = alphabet.index(encrypKey)

finalText = ""
for character in range(0, len(filteredText)):
	num = alphabet.index(filteredText[character])
	finalText = finalText + alphabet[(num + numericKey) % 30]
	
print finalText
#The final text is the encrypted code.
		
