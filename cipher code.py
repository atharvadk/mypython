alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text_in = input("Type your message:\n").lower()
shift_in = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encrypted_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = (position + shift)%26

        encrypted_text += alphabet[new_position]
        
    print(f"Your encrypted code is {encrypted_text}")

  
def decrypt(text,shift):
    decrypted_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = (position - shift + 26)%26

        decrypted_text += alphabet[new_position]
    print(f"Your decrypted code is{decrypted_text}")

  
if direction == "encode":
    encrypt(text=text_in, shift=shift_in)
elif direction == "decode":
    decrypt(text=text_in, shift=shift_in)
else:
    print("you entered wrong message")
input()