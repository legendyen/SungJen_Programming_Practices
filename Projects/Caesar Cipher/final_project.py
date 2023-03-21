alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
  new_text = ''
  for i in plain_text:
    position = alphabet.index(i)
    new_position = position + shift_amount
    if new_position > 25:
      new_position = new_position -26 
 
    new_text = new_text + alphabet[new_position]
  print("The encoded text is", new_text)
  

# Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount):
  original_text = ""
  for i in cipher_text:
    position = alphabet.index(i)
    original_position = position - shift_amount
    if original_position < 0:
      original_position = original_position + 26

    original_text = original_text + alphabet[original_position]
  print("The decoded text is", original_text)


# Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. 
# Then call the correct function based on that 'drection' variable.

if direction == 'encode':
  encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
  decrypt(cipher_text=text, shift_amount=shift)

  
  
