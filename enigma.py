import argparse
import numpy as np

# dictionary storing the rotor mappings:
rotor_map = {"A": "B", "C":"D"}
reflector_map = {1: -2}
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
def training():
    f = open("training.txt", 'r')
    s = f.read()
    lfreq = {}
    for i in range(len(s)-1):
        if ch in lfreq:

    f.close()
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

    # so frequency analysis

    # use n-grams

    # ch-sqaured???

    # IoC???
if __name__=="__main__":
    main()