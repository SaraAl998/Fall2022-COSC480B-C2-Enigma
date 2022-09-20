import argparse
import numpy as np
import math

# dictionary storing the rotor mappings:
rotor_map = {"A": "B", "C":"D"}
reflector_map = {1: -2}
thresh = 0 # Diego said keep this low
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


def decrypt(enc_text, lfreq):
    g = [] #guesses for plaintext
    look_up_dict = {}
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
            initial_pos = initial_pos - 1
            if initial_pos < "a":
                initial_pos = "z"
            curr_dict = look_up_dict[initial_pos]

            # check with training text
            if (prev!=""):
                numer = lfreq[prev][c] # number of times letter c appears after letter pev
                denom = lfreq[prev]['tot'] # number of times letter prev appears
                if ((numer/denom) <= thresh):
                    dec_text = ""
                    break
        if (dec_text != ""):
            g.add(dec_text)
    return g

def main():
    parser = argparse.ArgumentParser(description='Get the encrypted text.')
    parser.add_argument('encrypted_text', help='an integer for the accumulator')
    args = parser.parse_args()

    #training
    lfreq = training()
    # open text file and store it in a string
    enc_f = open(args.encrypted_text, 'r')
    enc_text = enc_f.read()
    enc_f.close()

    # 1. frequency analysis
    # and use n-grams
    g = decrypt(enc_text, lfreq)
    # ch-sqaured???
    # IoC???
if __name__=="__main__":
    main()