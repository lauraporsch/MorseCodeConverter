from MORSE_CODE import MORSE_CODE


def convert_to_morse(message):
    code = ""
    for letter in message:
        if letter not in MORSE_CODE:
            print("Sorry, you used a character that is not used in Morse Code, please try again.")
            return True
        else:
            code += MORSE_CODE[letter] + "  "
    print(f"Whitespace separates single characters, // equals whitespace and separates words\n "
          f"This is your encrypted message:\n"
          f"{code}")
    restart = input("Would you like to convert more messages? Type Yes or No  ").lower()
    if restart == "yes":
        return True
    else:
        print("Thank you for using the Morse Code Converter!")
        return False

print("███    ███  ██████  ██████  ███████ ███████      ██████  ██████  ██████  ███████\n"
      "████  ████ ██    ██ ██   ██ ██      ██          ██      ██    ██ ██   ██ ██\n"
      "██ ████ ██ ██    ██ ██████  ███████ █████       ██      ██    ██ ██   ██ █████\n"
      "██  ██  ██ ██    ██ ██   ██      ██ ██          ██      ██    ██ ██   ██ ██\n"
      "██      ██  ██████  ██   ██ ███████ ███████      ██████  ██████  ██████  ███████")

print("Hello, welcome to the Morse Code Converter.\n"
      "This program will turn your written message into Morse Code.\n"
      "You can use letters, numbers, commas, periods and question marks.\n")
more_messages = True

while more_messages:
    user_text = input("Please enter the text you would like to encode to Morse Code.\n").upper()
    more_messages = convert_to_morse(message=user_text)


