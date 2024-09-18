import sys

#Mappings
CAPITAL_PREFIX = '.....O'
NUMBER_PREFIX = '.O.OOO'
DECIMAL_PREFIX = '.O..OO'

BRAILLE_TO_ENG = {
    'O.....': 'a', 'O.O...': 'b', 'OO....': 'c', 'OO.O..': 'd', 'O..O..': 'e',
    'OOO...': 'f', 'OOOO..': 'g', 'O.OO..': 'h', '.OO...': 'i', '.OOO..': 'j',
    'O...O.': 'k', 'O.O.O.': 'l', 'OO..O.': 'm', 'OO.OO.': 'n', 'O..OO.': 'o',
    'OOO.O.': 'p', 'OOOOO.': 'q', 'O.OOO.': 'r', '.OO.O.': 's', '.OOOO.': 't',
    'O...OO': 'u', 'O.O.OO': 'v', '.OOO.O': 'w', 'OO..OO': 'x', 'OO.OOO': 'y',
    'O..OOO': 'z', '......': ' '
}

NUMBER_TO_BRAILLE = {
    '0': 'OOOOO.', '1': 'O....O', '2': 'O.OOO.', '3': 'OOO...', '4': 'OOO.O.',
    '5': 'O..OO.', '6': 'OOOO..', '7': 'OOOO.O', '8': 'OO.O..', '9': '.OOO..'
}

ENG_TO_BRAILLE = {value: key for key, value in BRAILLE_TO_ENG.items()}
BRAILLE_TO_NUMBER = {value: key for key, value in NUMBER_TO_BRAILLE.items()}


# Functions
def is_braille(s: str) -> bool:
    valid_chars = {'O', ',', ' '}
    return all(letter in valid_chars for letter in s)

def english_to_braille(english_text: str)->str :
    braille_output =''
    is_number_mode = False

    for char in english_text:
        if char.isupper():
            braille_output += CAPITAL_PREFIX
            char = char.lower()
        
        if char.isdigit():
            if not is_number_mode:
                braille_output += NUMBER_PREFIX
                is_number_mode = True

            braille_output += NUMBER_TO_BRAILLE[char]
        else:
            if is_number_mode:
                is_number_mode = False
            if char == ' ':
                braille_output += ' '  
            else:
                braille_output  += ENG_TO_BRAILLE.get[char, '']
        
    return braille_output 


def braille_to_english(braille_text: str) -> str:
    english_output = ''
    i = 0
    length = len(braille_text)
    is_number_mode = False

    
    while i < length:
        # handle space
        if braille_text[i] == ' ':
            english_output += ' '
            i += 1
            continue

        braille_char = braille_text[i: i + 6]

        # handle capitals
        if braille_char == CAPITAL_PREFIX:
            i+= 6
            braille_char = braille_text[i: i + 6]
            english_char = braille_to_english.get(braille_char,'')
            english_output += english_char.upper()
        elif braille_char == NUMBER_PREFIX:
            is_number_mode = True
            i += 6
        else:
            if is_number_mode:
                char = BRAILLE_TO_ENG.get(braille_char,'')

                is_number_mode = False
            else:
                char = BRAILLE_TO_ENG.get(braille_char,'')
            english_output += char
        i += 6
    return english_output






if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: python translator.py <input-string>")
        sys.exit(1)

    input_string = sys.argv[1]

    if is_braille(input_string):
        result = braille_to_english(input_string)
    else:
        result = english_to_braille(input_string)
    
    print(result)




                
            







            
    
        





        






    







