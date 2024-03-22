alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art
print(art.logo)

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
def caeser(text, shift, direction):
    if direction == "decode": 
        shift *= -1
    
    new_text = ""
    
    for letter in text:
        new_text += alphabet[(alphabet.index(letter)+shift)%26]
    
    print(f"The {direction}d text is {new_text}")

continue_cipher = "yes"

while continue_cipher == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text, shift, direction)
    continue_cipher = input("Do you want to continue. Type Yes or No\n").lower()
    