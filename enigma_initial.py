import argparse
import numpy as np
import json
import math
import ENIG_LOOKUP_RESULTS as lu
import ENIG_MAPPINGS


lfreq = {"a": {"tot": 5373, "a": 43, "r": 688, "b": 145, "n": 741, "l": 667, "h": 24, "m": 248, "d": 247, "c": 344, "t": 793, "p": 185, "i": 229, "s": 335, "g": 160, "e": 19, "f": 45, "j": 9, "k": 65, "y": 106, "z": 23, "o": 12, "q": 10, "u": 88, "v": 91, "w": 39, "x": 17}, "r": {"tot": 4860, "o": 428, "d": 163, "i": 572, "t": 270, "a": 621, "p": 87, "y": 156, "e": 1020, "s": 377, "n": 115, "w": 40, "c": 150, "f": 62, "l": 76, "m": 146, "q": 3, "g": 88, "r": 151, "u": 104, "b": 65, "k": 63, "v": 64, "h": 31, "j": 6, "x": 1, "z": 1}, "o": {"tot": 4252, "n": 1072, "r": 620, "u": 277, "v": 102, "a": 70, "l": 286, "m": 297, "d": 122, "w": 133, "b": 67, "s": 185, "p": 161, "c": 139, "o": 161, "h": 16, "y": 36, "t": 199, "g": 94, "i": 46, "x": 20, "k": 59, "f": 47, "e": 26, "z": 10, "j": 7}, "n": {"tot": 4822, "a": 334, "d": 407, "e": 455, "c": 360, "t": 699, "g": 727, "s": 523, "i": 322, "y": 50, "o": 161, "m": 56, "u": 67, "n": 122, "x": 2, "b": 53, "k": 58, "j": 30, "z": 7, "v": 77, "l": 54, "w": 29, "f": 65, "h": 36, "q": 9, "r": 57, "p": 62}, "b": {"tot": 1141, "a": 162, "c": 13, "e": 171, "i": 128, "l": 154, "o": 129, "r": 119, "s": 54, "u": 103, "b": 21, "y": 15, "w": 5, "d": 6, "g": 3, "h": 6, "k": 2, "m": 13, "p": 6, "t": 11, "f": 1, "n": 4, "j": 10, "v": 4, "z": 1}, "d": {"tot": 2507, "o": 135, "a": 231, "e": 534, "i": 410, "b": 50, "s": 204, "g": 46, "d": 97, "r": 151, "j": 11, "m": 50, "u": 102, "v": 37, "w": 36, "y": 36, "l": 63, "t": 44, "f": 44, "c": 88, "n": 21, "h": 40, "k": 6, "p": 63, "x": 1, "q": 6, "z": 1}, "e": {"tot": 7601, "d": 768, "r": 1187, "e": 242, "n": 880, "s": 1068, "a": 485, "l": 425, "m": 301, "p": 229, "v": 148, "q": 42, "x": 175, "c": 459, "g": 135, "b": 102, "t": 341, "u": 47, "i": 104, "w": 108, "y": 48, "f": 143, "h": 46, "o": 64, "k": 24, "j": 23, "z": 7}, "c": {"tot": 3025, "a": 380, "e": 399, "t": 309, "s": 58, "c": 78, "i": 198, "o": 595, "r": 137, "u": 124, "y": 35, "d": 20, "h": 318, "k": 154, "m": 13, "n": 12, "q": 7, "l": 130, "b": 7, "f": 6, "g": 11, "j": 2, "p": 23, "v": 4, "w": 2, "z": 3}, "i": {"tot": 5461, "l": 271, "t": 462, "e": 282, "g": 160, "n": 1326, "o": 603, "c": 460, "b": 91, "d": 179, "s": 451, "r": 171, "v": 187, "p": 114, "a": 267, "m": 174, "k": 27, "u": 22, "f": 99, "q": 9, "x": 23, "z": 50, "i": 15, "j": 6, "y": 1, "h": 7, "w": 4}, "l": {"tot": 3231, "i": 496, "e": 593, "a": 397, "u": 104, "y": 217, "l": 313, "t": 119, "b": 35, "c": 65, "f": 47, "g": 24, "o": 305, "m": 50, "p": 61, "r": 28, "s": 146, "w": 11, "d": 107, "k": 22, "v": 37, "h": 18, "n": 26, "j": 7, "x": 3}, "t": {"tot": 4760, "i": 1026, "y": 140, "a": 445, "e": 850, "r": 390, "s": 361, "o": 319, "u": 172, "m": 57, "t": 161, "h": 280, "l": 88, "w": 43, "b": 50, "c": 122, "n": 28, "d": 47, "f": 41, "p": 73, "g": 23, "k": 9, "v": 17, "j": 9, "q": 5, "z": 3, "x": 1}, "s": {"tot": 5084, "a": 279, "e": 567, "o": 234, "t": 771, "s": 471, "i": 431, "h": 268, "c": 381, "l": 130, "p": 346, "k": 53, "w": 85, "b": 125, "n": 45, "m": 148, "u": 224, "y": 41, "r": 131, "d": 119, "f": 94, "g": 65, "j": 15, "v": 43, "q": 16, "z": 2}, "y": {"tot": 1027, "a": 68, "i": 44, "l": 44, "s": 122, "t": 53, "z": 2, "m": 57, "b": 55, "o": 31, "w": 19, "e": 89, "c": 79, "n": 37, "r": 46, "p": 77, "d": 45, "f": 29, "g": 27, "h": 35, "u": 16, "j": 17, "k": 11, "q": 7, "v": 14, "y": 3}, "g": {"tot": 1717, "i": 119, "a": 158, "l": 66, "e": 305, "h": 125, "g": 40, "r": 174, "o": 75, "n": 54, "y": 26, "s": 136, "u": 74, "t": 39, "b": 48, "k": 9, "c": 64, "d": 37, "f": 41, "m": 40, "p": 51, "z": 2, "j": 4, "q": 1, "v": 6, "w": 22, "x": 1}, "u": {"tot": 1939, "t": 188, "a": 103, "s": 220, "n": 233, "r": 318, "i": 86, "l": 145, "m": 115, "q": 2, "e": 89, "g": 67, "k": 10, "b": 73, "d": 59, "c": 95, "p": 71, "f": 19, "y": 10, "z": 9, "o": 8, "x": 5, "j": 2, "h": 4, "v": 3, "w": 3, "u": 2}, "v": {"tot": 849, "e": 416, "i": 206, "a": 117, "o": 59, "g": 3, "d": 6, "r": 3, "y": 4, "c": 6, "s": 5, "x": 1, "t": 3, "h": 3, "m": 2, "n": 3, "p": 3, "u": 4, "v": 1, "b": 2, "w": 2}, "h": {"tot": 1429, "a": 256, "e": 302, "i": 190, "o": 233, "m": 22, "r": 55, "u": 56, "l": 21, "d": 17, "b": 26, "s": 36, "y": 32, "n": 19, "t": 83, "c": 12, "q": 2, "f": 13, "z": 3, "g": 3, "h": 8, "w": 15, "k": 3, "p": 18, "j": 3, "v": 1}, "m": {"tot": 1912, "a": 355, "i": 260, "y": 21, "m": 83, "o": 197, "p": 199, "e": 435, "s": 88, "n": 12, "b": 74, "d": 13, "u": 50, "w": 10, "c": 25, "f": 14, "g": 8, "t": 18, "h": 8, "l": 8, "j": 6, "k": 4, "r": 15, "v": 5, "x": 1, "q": 1, "z": 2}, "p": {"tot": 2027, "t": 101, "a": 253, "l": 187, "e": 311, "o": 234, "h": 101, "i": 127, "n": 6, "p": 112, "r": 313, "s": 94, "b": 6, "c": 22, "u": 76, "y": 12, "d": 16, "m": 16, "f": 7, "g": 15, "k": 3, "j": 4, "v": 4, "z": 2, "w": 4, "x": 1}, "k": {"tot": 592, "n": 27, "a": 32, "e": 158, "i": 97, "s": 85, "l": 18, "b": 24, "g": 7, "u": 8, "o": 15, "r": 10, "j": 4, "m": 6, "d": 14, "f": 12, "k": 6, "c": 13, "t": 17, "y": 11, "h": 8, "w": 5, "p": 14, "q": 1}, "w": {"tot": 632, "l": 11, "a": 133, "e": 104, "i": 105, "s": 42, "h": 34, "o": 62, "f": 9, "b": 10, "j": 2, "n": 36, "c": 6, "d": 6, "g": 4, "t": 8, "k": 4, "y": 6, "r": 24, "m": 5, "p": 5, "u": 3, "v": 2, "w": 10, "x": 1}, "q": {"tot": 123, "u": 103, "c": 2, "e": 1, "f": 1, "s": 3, "h": 1, "i": 4, "l": 3, "n": 1, "q": 1, "a": 1, "t": 2}, "x": {"tot": 264, "a": 23, "i": 27, "b": 2, "e": 26, "c": 26, "t": 36, "d": 2, "h": 7, "o": 2, "p": 57, "f": 8, "y": 5, "j": 1, "l": 4, "m": 6, "u": 9, "r": 3, "s": 5, "v": 1, "w": 3, "x": 10, "n": 1}, "j": {"tot": 183, "a": 34, "u": 37, "i": 9, "o": 44, "c": 3, "d": 2, "e": 40, "j": 3, "m": 2, "p": 4, "r": 2, "s": 1, "v": 1, "n": 1}, "f": {"tot": 927, "a": 102, "f": 79, "e": 123, "i": 195, "o": 128, "g": 6, "r": 66, "t": 33, "u": 62, "b": 6, "s": 14, "l": 63, "c": 11, "d": 6, "m": 4, "p": 6, "w": 4, "x": 1, "y": 12, "h": 5, "j": 1}, "z": {"tot": 136, "i": 15, "o": 18, "e": 44, "a": 23, "b": 4, "r": 1, "z": 8, "y": 4, "c": 2, "f": 1, "g": 1, "j": 1, "l": 4, "d": 2, "m": 1, "q": 1, "u": 5, "s": 1}}

# dictionary storing the rotor mappings:
# rotor_map = {"A": "B", "C":"D"}
# reflector_map = {1: -2}
thresh = 0# Diego said keep this low
# Notes: 1) Three substitutions  2) Make map for each key i.e full mapping after 3 substitutions
# a map of maps: {26 letters (outmost key, current position on the line): map of 26 letters (full tracing)}
# Assumptions: 1) We have the rotor and reflector mappings 2) We DO NOT have the initial position


# Calculations based on ASCII values
# 1. First substitution determined by rotor mapping (fixed): x --> y
# 2. Second substition determined by position of rotor against reflector.
# 3. Reflector has 26 connection points.
# 4. Index the connection points 1-26.
# 5. Store the "displacement" at each connection point in a map.
#    This is determined by the reflector mapping (fixed).
# 6. Starting key will be reference point for the rotor setting.

# returns a dict or dict that stores the relative frequency of letter2 appearing after letter1
def training():
    f = open("training.txt", 'r')
    s = f.read()
    lfreq = {}
    for i in range(len(s)-1):
        l1 = s[i].lower()
        l2 = s[i+1].lower()
        if (l1.isalpha() and l2.isalpha()):
            if l1 not in lfreq:
                lfreq[l1] = {}
                lfreq[l1]["tot"] = 0
            if l2 not in lfreq[l1]:
                lfreq[l1][l2] = 0
            lfreq[l1][l2] += 1
            lfreq[l1]['tot'] += 1
    f.close()
    return lfreq

'''
Encrypts a plain text with the Pringles-ENIGMA machine.
'''
def encrypt():
    initial_pos = 'k'    # Rotor Starting Position
    message = "ItwasabrightcolddayinApril,andtheclockswerestrikingthirteen.WinstonSmith,hischinnuzzledintohisbreastinanefforttoescapethevilewind,slippedquicklythroughtheglassdoorsofVictoryMansions,thoughnotquicklyenoughtopreventaswirlofgrittydustfromenteringalongwithhim."
    encrypted = ''

    # Index lookup table and encrypt.
    for ch in message:
        if not ch.isalpha():
            continue
        ch = ch.lower()
        print(ch,end="")
        encrypted += lu.LOOKUP[initial_pos][ch]
        initial_pos = chr(ord(initial_pos) - 1)
        if initial_pos < "a":
            initial_pos = "z"
    
    return encrypted    # return encrypted text


def decrypt(enc_text, lfreq):
    g = [] #guesses for plaintext
    look_up_dict = lu.LOOKUP
    #look_up_dict = read_look_up_dict_file()
    for key1 in look_up_dict: # enumerate through each possible initial position
        dec_text = ""
        initial_pos = key1
        curr_dict = look_up_dict[initial_pos]
        prev = ""
        for i in range(len(enc_text)):
            c = enc_text[i].lower()
            dec_text += curr_dict[c]

            #rotate rotor
            initial_pos = chr(ord(initial_pos) - 1)
            if initial_pos < "a":
                initial_pos = "z"
            if initial_pos not in look_up_dict:
                break
            curr_dict = look_up_dict[initial_pos]
            '''
            # check with training text
            if (prev!=""):
                if (c not in lfreq[prev]):
                    dec_text = ""
                    break
                numer = lfreq[prev][c] # number of times letter c appears after letter pev
                denom = lfreq[prev]['tot'] # number of times letter prev appears
                if ((numer/denom) <= thresh):
                    dec_text = ""
                    break
            prev = curr_dict[c]
            '''
        if (dec_text != ""):
            g.append(dec_text)
    return g


def main():

    print(encrypt())
    '''
    parser = argparse.ArgumentParser(description='Get the encrypted text.')
    parser.add_argument('encrypted_text', help='an integer for the accumulator')
    args = parser.parse_args()

    #training
    # lfreq = training() # Created ahead of time, discuss this with the group - Diego
    # open text file and store it in a string
    enc_f = open(args.encrypted_text, 'r')
    enc_text = enc_f.read()
    enc_f.close()

    # 1. frequency analysis
    # and use n-grams
    g = decrypt(enc_text, lfreq)
    print(g)
    # ch-sqaured???
    # IoC???
    '''

if __name__=="__main__":
    main()