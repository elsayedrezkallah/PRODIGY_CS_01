# Define a function to perform the Caesar cipher encryption/decryption
def caesar_cipher(message, shift):
    # Initialize an empty string to store the encrypted/decrypted message
    encrypted_message = ""
    
    # Iterate over each character in the input message
    for char in message:
        # Check if the character is a letter (either uppercase or lowercase)
        if char.isalpha():  
            # Calculate the ASCII offset for uppercase or lowercase letters
            ascii_offset = 65 if char.isupper() else 97  
            
            # Perform the Caesar cipher encryption/decryption by shifting the character
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            
            # Add the encrypted character to the encrypted message
            encrypted_message += encrypted_char
        else:
            # If the character is not a letter, add it to the encrypted message as is
            encrypted_message += char
    
    # Return the encrypted/decrypted message
    return encrypted_message

# Define the main function to interact with the user
def main():
    # Print a welcome message
    print("--------------------------------- Caesar Cipher ---------------------------------")
    print("Welcome to the Encryption or Decryption program :)")
    
    # Loop indefinitely until the user chooses to quit
    while True:
        try:
            # Ask the user to choose an option: encrypt, decrypt, or quit
            choice = input("If you like to 'encrypt' Type e or 'decrypt' Type d or to 'quit' type q: ")
            
            # Check if the user's input is valid
            if choice not in ["e", "d", "q"]:
                print("That's not a valid choice! \nPlease choose from the letters that appear in front of you :)")
                continue
            
            # If the user chooses to quit, print a farewell message and break out of the loop
            if choice == "q":
                print("Thanks For Your Patience :)")
                break
            
            # Ask the user to input the text to be encrypted/decrypted
            text = input("Enter text: ")
            
            # Ask the user to input the shift value
            shift = int(input("Enter shift: "))
            
            # Check if the shift value is within the valid range (0-25)
            if shift < 0 or shift > 25:
                print("Shift value must be between 0 and 25.")
                continue
            
            # Perform the encryption or decryption based on the user's choice
            if choice == "e":
                encrypted_text = caesar_cipher(text, shift)
                print("Encrypted text:", encrypted_text)
            elif choice == "d":
                decrypted_text = caesar_cipher(text, -shift)
                print("Decrypted text:", decrypted_text)
        
        # Catch any ValueError exceptions that may occur during input validation
        except ValueError:
            print("Invalid input. Please enter a valid shift value.")

# Call the main function when the script is run
if __name__ == "__main__":
    main()