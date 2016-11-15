class Caesar_Cipher():
  
  def encrypt(self):
    all_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print("Enter the message you would like encrypted:")
    message = str(input())
    message = message.upper()
    print("Enter the encryption key (any number between 0 and 25):")
    key = int(input())
    while (key < 0):   #if the key is below 0, it is increased by 26 until it is within 0 and 26
      key += 26
    while (key > 26):     #if the key is over 26, it is reduced by 26 until it is within 0 and 26
      key -= 26
    translated = ""
    for letter in message:
      if letter in all_letters:
        temp = all_letters.find(letter)
        temp += key
        if(temp >= len(all_letters)):
          temp -= len(all_letters)
        elif(temp < 0):
          temp += len(all_letters)
        translated += all_letters[temp]
      else:
        translated += letter
    print(translated)
    
  def decrypt(self):
    all_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print("Enter the message you would like decrypted:")
    message = str(input())
    message = message.upper()
    print("Enter the decryption key (same as encryption key):")
    key = int(input())
    while (key < 0):   #if the key is below 0, it is increased by 26 until it is within 0 and 26
      key += 26
    while (key > 26):     #if the key is over 26, it is reduced by 26 until it is within 0 and 26
      key -= 26
    translated = ""
    for letter in message:
      if letter in all_letters:
        temp = all_letters.find(letter)
        temp -= key
        if(temp >= len(all_letters)):
          temp -= len(all_letters)
        elif(temp < 0):
          temp += len(all_letters)
        translated += all_letters[temp]
      else:
        translated += letter
    print(translated)
    
secret_message = Caesar_Cipher()
secret_message.encrypt()
secret_message.decrypt()
        
