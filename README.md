# Caesar Cipher

You are given a text to encrypt, for instance a string, and another symbol in the alphabet A, for instance a letter c, that serves as the encryption key. By converting the key character to its assigned number, the caesar cipher works by adding the  key to each character.

Every letter in the alphabet is assigned a number, in order, starting at 0. This means that a is assigned 0, b is assigned 1, z is assigned 25, "." is assigned 26, "," is assigned 27, "!" is assigned 28, and "?" is assigned 29.

# Vignere Cipher

A key for this cipher is a short word or a phrase in which all characters are in our "alphabet". 

To encrypt a text, you need to do the following: Use the first character of the keyword to encrypt the first character of the filtered text (by adding the  key to the character’s position in the alphabet and taking the result modulo 30), the second character of the keyword to encrypt the second character of the filtered text, and so on. When you reach the end of the keyword, start from its beginning, and continue cycling over the keyword until the end of the filtered text.

# Frequency

We can measure frequencies of characters in encrypted text. The most frequent character in encrypted text is likely to decrypt to a,t, or e. Knowing this, as well as other frequencies, allows you to automatically determine the likely key without even trying any dictionary words. We can use these frequencies to discover the cipher key without repeatedly trying different keys.




