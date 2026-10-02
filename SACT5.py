import time
import winsound

# Dictionary for every letter 
MORSE_LETTERS = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.','0':'-----', #NUMBERS
                    ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'}

def encrypt(message):
    morseCode = ''

    for letter in message:
        if letter != ' ':
            morseCode += MORSE_LETTERS[letter] + ' '
        else:
            morseCode += ' '

    return morseCode

def playSound (morseCode):
    for symbol in morseCode:
        if symbol == ".":
            winsound.Beep(800,100) #Aproximate of frecuency and duration in ms
            print("Dot")
        elif symbol == "-":
            winsound.Beep(800,350)
            print("OverScore")
        elif symbol == " ":
            time.sleep(0.2) #Pausing after every letter
            print("Space")
        time.sleep(1) #We need to wait after every loop since python can't reproduce the sound quickly enough

message = input("Enter the message\n")
result = encrypt(message.upper())
print (result)
playSound(result)