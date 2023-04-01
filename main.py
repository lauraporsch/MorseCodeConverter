MORSE_CODE = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
                   "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
                   "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
                   "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
                   "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", ", ": "--..--", ".": ".-.-.-",
                   "?": "..--..", " ": "//"}


def convert_to_morse(message):
    code = ""
    for letter in message:
        if letter not in MORSE_CODE:
            print("Sorry, you used a sign that is not used in Morse Code, please try again.")
            return
        else:
            code += MORSE_CODE[letter] + "  "
    print(f"Whitespace separates single characters, // equals whitespace and separates words\n "
          f"This is your encrypted message:\n"
          f"{code}")


print("███    ███  ██████  ██████  ███████ ███████      ██████  ██████  ██████  ███████\n"
      "████  ████ ██    ██ ██   ██ ██      ██          ██      ██    ██ ██   ██ ██\n"
      "██ ████ ██ ██    ██ ██████  ███████ █████       ██      ██    ██ ██   ██ █████\n"
      "██  ██  ██ ██    ██ ██   ██      ██ ██          ██      ██    ██ ██   ██ ██\n"
      "██      ██  ██████  ██   ██ ███████ ███████      ██████  ██████  ██████  ███████")
# User prompt
print("Hello, welcome to the Morse Code Converter.\n"
      "This program will turn your written message into Morse Code.\n"
      "You can use letters, numbers, commas, periods and question marks.\n")
continue_convert = True
while continue_convert:
    user_text = input("Please enter the text you would like to encode to Morse Code.\n").upper()
    convert_to_morse(message=user_text)
    more_messages = input("Would you like to convert more messages? Type Yes or No  ").lower()
    if more_messages == "yes":
        pass
    else:
        continue_convert = False
        print("Thank you for using the Morse Code Converter!")

