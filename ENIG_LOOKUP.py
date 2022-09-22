import ENIG_MAPPINGS    # ENIGMA mappings. Based on Pringles device
'''
« ENIGMA table generator »
Generates a lookup table of all possible letter to letter substitutions based on 
all possible rotor starting configurations.
The function does not return anything, but prints to standard output a 
nested dictionary of all possible letter to letter substitutions.
Format:
{<Rotor Starting Configuration> : {letter to encrypt/decrypt : result of
encryption/decryption}}
'''
def table_gen():
    # reversed Rotor letter mappings and alphabet-number mappings
    ROTOR_REV_MAP = {v:k for k, v in ENIG_MAPPINGS.ROTOR_FW_MAP.items()}
    ALPHA_MAP_REV_MAP = {v:k for k, v in ENIG_MAPPINGS.ALPHA_MAP.items()}

    print("LOOKUP = {")
    # Iterate through each starting configuration of rotor
    for i in ENIG_MAPPINGS.ROTOR_FW_MAP.keys():
        print("\t'" + i + "': {")
        # as the rotor shifts by one notch, this variable ensures that the
        # letter gets matched properly to the corresponding reflector connection
        # point.
        refl_shift_i = ord(i) - 97

        # Per configuration, find the final letter mappings
        for j in ENIG_MAPPINGS.ROTOR_FW_MAP.keys():
            # get the „initial" rotor letter mapping 
            # (first substitution)
            first_sub_letter = ENIG_MAPPINGS.ROTOR_FW_MAP.get(j)

            # next, obtain the appropriate letter–reflector connection point
            # matching
            first_sub_letter_numeric = ENIG_MAPPINGS.ALPHA_MAP.get(first_sub_letter)
            refl_contact_point = (first_sub_letter_numeric - refl_shift_i) % 26

            # „reflect" the letter, then get the resulting encrypted/decrypted
            # letter (second + final substitution)
            refl_result = ENIG_MAPPINGS.REFL_MAP.get(refl_contact_point)
            refl_result_alphabetic = ALPHA_MAP_REV_MAP.get((refl_result + refl_shift_i) % 26)
            final_sub_letter = ROTOR_REV_MAP.get(refl_result_alphabetic)

            if (j != 'z'):
                print("\t\t'" + j + "':'" + final_sub_letter + "',")
            else:
                print("\t\t'" + j + "':'" + final_sub_letter + "'")
        if (i != 'z'):
            print("\t},")
        else:
            print("\t}")
    print("}")

if __name__ == "__main__":
    table_gen()