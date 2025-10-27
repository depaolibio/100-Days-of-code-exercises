logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Welcome to Caesar Cipher\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt():
    text_list = list(text)
    current_shift = shift
    for letter in text_list:
        if letter in alphabet:
            pos_alphabet = alphabet.index(letter)
            new_pos = pos_alphabet + current_shift
            new_pos_lim = new_pos % len(alphabet)
            retrieve_letter = alphabet[new_pos_lim]
            print(retrieve_letter, end='')
            current_shift += 2 ** 3
        else:
            print(letter, end='')

def decrypt(text_list_d, shift_amount):
    text_list_d = list(text)
    current_shift = shift
    for letter in text_list_d:
        if letter in alphabet:
            pos_alphabet_d = alphabet.index(letter)
            ori_pos_alphabet = pos_alphabet_d - current_shift
            ori_pos_alphabet_lim = ori_pos_alphabet % len(alphabet)
            retrieve_letter_d = alphabet[ori_pos_alphabet_lim]
            print(retrieve_letter_d, end='')
            current_shift += 2 ** 3
        else:
            print(letter, end='')

def caesar():
    if direction == "encode":
        encrypt()
        print("\n==================================\nThis is the end of your encoding.")
    elif direction == "decode":
        decrypt(text_list_d=text, shift_amount=shift)
        print("\n==================================\nThis is the end of your decoding.")
caesar()
