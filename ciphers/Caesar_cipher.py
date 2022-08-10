class CaesarMessageCipher:

	def __init__(self, message):
	
		self.message = message		
		self._symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!№@#$%^&?*()|".,;:' 
		self.encryption_message = ''
		self.decryption_message = ''

	def encryption_mode(self, key):
		for char in message: 
			if char in self._symbols:
				encrypt_key = key + self._symbols.find(char)
				while encrypt_key >= len(self._symbols):
					encrypt_key -= len(self._symbols)
				self.encryption_message += self._symbols[encrypt_key]
			else: 
				self.encryption_message += char
		return self.encryption_message 

	def decryption_mode(self, key):		
		for char in self.encryption_message: 
			if char in self._symbols:
				decryption_key = self._symbols.find(char) - key 
				while decryption_key >= len(self._symbols):
					decryption_key -= len(self._symbols)
				while decryption_key < 0:
					decryption_key += len(self._symbols)
				self.decryption_message += self._symbols[decryption_key]			
			else: 				
				self.decryption_message += char		
		return self.decryption_message

	def hack_mode(self):
		for hacked_key in range(len(self.message)):
			
			translated_mess = ''

			for char in self.message:
				if char in self._symbols:
					encrypt_char_index = self._symbols.find(char)
					translated_char_index = encrypt_char_index - hacked_key
					if translated_char_index < 0:
						translated_char_index += len(self._symbols)
					translated_mess += self._symbols[translated_char_index] 
				else:
					translated_mess += char
			print(translated_mess)

if __name__ == '__main__':

	message = input('Enter your message: ')

	key = int(input('Enter your key for encryption: '))

	encrypt_message = CaesarMessageCipher(message)

	print(encrypt_message.encryption_mode(key))
	print(encrypt_message.decryption_mode(key))
	
	print()
	print()
	
	will_hack_mess = CaesarMessageCipher(encrypt_message.encryption_mode(key))

	will_hack_mess.hack_mode()