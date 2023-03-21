alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
  new_text = ''
  for i in plain_text:
    position = alphabet.index(i)
    new_position = position + shift_amount
    
    if new_position > 25:
      new_position = new_position -26 
    #Debug for list index put of range
    
    new_text = new_text + alphabet[new_position]
  print("The encoded text is", new_text)

#Call the encrypt function and pass in the user inputs.
encrypt(plain_text=text, shift_amount=shift)

#Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#e.g. 
#plain_text = "hello"
#shift = 5
#cipher_text = "mjqqt"
#print output: "The encoded text is mjqqt"
