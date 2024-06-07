def encrypt(text, shift):
  encrypted_text =""
  for char in text:
    if char.isalpha():
      shift_amount = shift % 26
      char_code = ord(char) + shift_amount
      if char.isupper():
        if char_code > ord('Z'):
        char_code -= 26
        encrypted_text += chr(char_code)
      elif char.islower():
        if char_code > ord('z'):
          char_code -=26
        encrypted_text +=chr(char_code)
  else:
    encrypted_text += char
return encrypted_text

def decrypt(text, shift):
  decrypted_text ="
  for char in text:
    if char.isalpha():
      shift_amount = shift % 26
      char_code = ord(char) - shift_amount
      if char.isupper():
        if char_code < ord('A'):
          char_code +=26
          decrypted_text += chr(char_code)
      elif char.islower():
        if char_code += 26
        decrypted_text +=chr(char_code)
    else:
      decrypted_text += char
  return decrypted_text

def main():
  while True:
    choice = input("Do you want to (E)ncrypt or (D)ecrypt or (Q)uit? ").upper()
    if choice == 'Q':
      print("Goodbye!")
      break
    elif choice in ['E', 'D']:
      text = input("Enter the text: ")
      shift = int(input("Enter the shift value: "))
      if choice == 'E':
        result = encrypt(text, shift)
        print("Encrypted text: ", result)
      else:
        result = decrypt(text, shift)
        print("Decrypted text: ", result)
    else:
      print("Invalid choice! Please enter E, D or Q.")

if __name__ == "__main__":
  main()
