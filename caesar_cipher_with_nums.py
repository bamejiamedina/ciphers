class Caesar_Cipher_with_nums():
  
  def encrypt(self):
    all_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    all_nums = "0123456789"
    print("Enter the message you would like encrypted:")
    message = str(input())
    message = message.upper()
    print("Enter the encryption key (any number between 0 and 25):")
    key = int(input())
    while (key < 0):   #if the key is below 0, it is increased by 26 until it is within 0 and 26
      key += 26
    while (key > 26):     #if the key is over 26, it is reduced by 26 until it is within 0 and 26
      key -= 26
    encrypted = ""
    for char in message:
      if char in all_letters:
        temp = all_letters.find(char)
        temp += key
        if(temp >= len(all_letters)):
          temp -= len(all_letters)
        elif(temp < 0):
          temp += len(all_letters)
        encrypted += all_letters[temp]
      else:
          if char in all_nums:
            temp = all_nums.find(char)
            temp += key
            if(temp >= len(all_nums)):
              temp -= len(all_nums)
            elif(temp < 0):
              temp -= len(all_nums)
            encrypted += all_nums[temp]   #Index out of bound error here when key > 25 and numbers are included in the input; currently looking for solution
          else:
            encrypted += char      
    print(encrypted)
    
  def decrypt(self):
    all_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    all_nums = "0123456789"
    print("Enter the message you would like decrypted:")
    message = str(input())
    message = message.upper()
    print("Enter the message you would like decrypted:")
    key = int(input())
    while (key < 0):   #if the key is below 0, it is increased by 26 until it is within 0 and 26
      key += 26
    while (key > 26):     #if the key is over 26, it is reduced by 26 until it is within 0 and 26
      key -= 26
    decrypted = ""
    for char in message:
      if char in all_letters:
        temp = all_letters.find(char)
        temp -= key
        if(temp >= len(all_letters)):
          temp -= len(all_letters)
        elif(temp < 0):
          temp += len(all_letters)
        decrypted += all_letters[temp]
      else:
          if char in all_nums:
            temp = all_nums.find(char)
            temp -= key
            if(temp >= len(all_nums)):
              temp -= len(all_nums)
            elif(temp < 0):
              temp -= len(all_nums)
            decrypted += all_nums[temp]
          else:
            decrypted += char      
    print(decrypted)
secret_message = Caesar_Cipher_with_nums()
secret_message.encrypt()
secret_message.decrypt()
        
        
