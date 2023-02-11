#Credit card encyption
# function to encrypt plaintext 
def encrypt(text,s): 
	result = "" 

	# traverse text 
	for i in range(len(text)): 
		char = text[i] 

		# Encrypt uppercase characters 
		if (char.isupper()): 
			result += chr((ord(char) + s-65) % 26 + 65) 

		# Encrypt lowercase characters 
		else: 
			result += chr((ord(char) + s - 97) % 26 + 97) 

	return result 

# function to decrypt ciphertext 
def decrypt(text,s): 
	result = "" 

	# traverse text 
	for i in range(len(text)): 
		char = text[i] 

		# Decrypt uppercase characters 
		if (char.isupper()): 
			result += chr((ord(char) - s-65) % 26 + 65) 

		# Decrypt lowercase characters 
		else: 
			result += chr((ord(char) - s - 97) % 26 + 97) 

	return result 

# driver code 
if __name__ == "__main__": 
	text = input("Please enter your credit card number :")
	s = 4
	print ("Credit Card Number :",text) 
	print ("Shift :",s) 
	
	# encrypt the given credit card number 
	encrypted_text = encrypt(text,s) 
	print ("Encrypted Credit Card Number :",encrypted_text) 
	
	# decrypt the encrypted credit card number 
	decrypted_text = decrypt(encrypted_text,s) 
	print ("Decrypted Credit Card Number :",decrypted_text)