# Katlyn Toro encode file

def encode_password(password):

    encoded_password = ""     # setting up encoded_password

    for digit in password:
        # Shift each digit up by 3 and handle wraparound with modulo 10
        encoded_digit = (int(digit) + 3) % 10       # Takes each inputted string digit, converts to int, adds 3, modulo 10 (example: to convert 11 to 1 etc)
        encoded_password += str(encoded_digit)      # Stores the encoded digits as a string in 'encoded_password'

    return encoded_password


def decode_password(password):

    decoded_password = ""   # setting up decoded_password

    for digit in password:
        # Shift each digit down by 3 and handle wraparound with modulo 10
        decoded_digit = (int(digit) - 3) % 10       # Takes each inputted string digit, converts to int, subtracts 3, module 10
        decoded_password += str(decoded_digit)      # Stores the decoded digits as a string in 'decoded password'

    return decoded_password


if __name__ == '__main__':

    password = ""  # Initial value for 'password'
    encoded = ""  # Initial value for 'encoded'

    while True:
        print('Menu\n'
          '-------------\n'
          '1. Encode\n'
          '2. Decode\n'
          '3. Quit\n')
        option = int(input("Please enter an option: "))



        if option == 1:
            password = input("Please enter your password to encode: ")    # User input password string
            encoded = encode_password(password)       # Calling encode_password function and assigning result to 'encoded'

            if encoded:
                print("Your password has been encoded and stored!\n")
                # If you want to see the encoded password remove comment from following statement:
                # print(encoded)
            continue

        if option == 2:
         # Should just be entire def encode_password(password) statement switched to decode and -3 instead of +
         # Replacing (password) with (encoded) undoes previous encoding :)
            decoded = decode_password(encoded)  # Calling decode_password function and assigning result to 'decoded'
            print(f"The encoded password is {encoded}, and the original password is {decoded}.\n")

        if option == 3:
            break

