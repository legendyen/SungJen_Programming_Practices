alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if direction == 'decode':
    shift_amount = shift_amount * -1
  for i in start_text:
    position = alphabet.index(i)
    new_position = position + shift_amount
    if new_position > 25:
      new_position = new_position - 26 
    elif new_position < 0:
      new_position = new_postion + 26
 
    end_text = end_text + alphabet[new_position]
  print(f"The {direction} text is {end_text}")

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
