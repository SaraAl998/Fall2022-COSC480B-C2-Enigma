import argparse
import numpy as np
import json
import math

#exp_freqs = {'a': 0.10514299164410969, 'b': 0.027350829704601624, 'c': 0.03638931387548547, 'd': 0.032929269153818996, 'e': 0.10015299517476757, 'f': 0.015558432387901612, 'g': 0.025938566552901023, 'h': 0.031140402494998234, 'i': 0.06075085324232082, 'j': 0.0038366482287866305, 'k': 0.020760268329998822, 'l': 0.055737319053783686, 'm': 0.030622572672708015, 'n': 0.05211251029775215, 'o': 0.06592915146522302, 'p': 0.030434270919147934, 'q': 0.0019771684123808405, 'r': 0.07162527951041545, 's': 0.05609038484170884, 't': 0.056043309403318815, 'u': 0.04427444980581382, 'v': 0.010968577144874661, 'w': 0.016123337648581853, 'x': 0.004448628927856891, 'y': 0.037778039307991056, 'z': 0.005884429798752501}
#exp_freqs = {'a': 4467, 'b': 1162, 'c': 1546, 'd': 1399, 'e': 4255, 'f': 661, 'g': 1102, 'h': 1323, 'i': 2581, 'j': 163, 'k': 882, 'l': 2368, 'm': 1301, 'n': 2214, 'o': 2801, 'p': 1293, 'q': 84, 'r': 3043, 's': 2383, 't': 2381, 'u': 1881, 'v': 466, 'w': 685, 'x': 189, 'y': 1605, 'z': 250}


lfreq = {"a": {"tot": 279420, "a": 255, "h": 1449, "l": 40559, "m": 11453, "n": 40043, "r": 31754, "s": 16637, "b": 13238, "c": 18022, "y": 2611, "t": 42056, "x": 1286, "d": 9605, "f": 2147, "i": 6588, "k": 3053, "p": 10562, "g": 8545, "u": 5457, "v": 3495, "z": 1474, "e": 6131, "o": 389, "q": 341, "j": 318, "w": 1952}, "h": {"tot": 86299, "e": 18798, "i": 14800, "s": 836, "h": 112, "r": 4080, "l": 1785, "m": 904, "y": 8172, "o": 14847, "u": 2801, "a": 14065, "t": 2480, "k": 62, "n": 992, "c": 116, "w": 409, "b": 307, "p": 181, "z": 18, "g": 77, "f": 259, "d": 138, "j": 15, "v": 33, "q": 12}, "e": {"tot": 319497, "d": 30879, "s": 46930, "l": 19586, "h": 1461, "r": 66714, "j": 396, "n": 38436, "e": 7312, "t": 18125, "m": 12725, "y": 1743, "a": 15041, "v": 3385, "c": 13180, "g": 4208, "i": 4366, "p": 8610, "k": 695, "o": 5476, "z": 450, "u": 4490, "w": 2367, "b": 3042, "f": 3774, "q": 931, "x": 5175}, "i": {"tot": 309636, "n": 60888, "i": 579, "s": 36502, "c": 35999, "t": 24854, "o": 22038, "a": 20666, "e": 13427, "z": 8384, "r": 7287, "l": 15968, "d": 14417, "u": 2242, "p": 7030, "v": 8371, "g": 7040, "b": 4670, "m": 8343, "f": 6241, "k": 2633, "x": 767, "y": 91, "w": 147, "h": 420, "q": 500, "j": 132}, "n": {"tot": 225799, "g": 29714, "i": 22288, "a": 18634, "c": 13467, "e": 32263, "d": 15070, "m": 1606, "t": 29533, "s": 14511, "n": 3949, "o": 20424, "u": 3301, "r": 2084, "y": 1749, "z": 527, "l": 1794, "v": 1838, "k": 2202, "p": 2539, "b": 1423, "w": 940, "f": 3417, "h": 1407, "j": 522, "q": 489, "x": 108}, "l": {"tot": 176592, "i": 32897, "s": 2966, "f": 946, "v": 1090, "l": 18756, "y": 20196, "u": 6727, "a": 25052, "o": 18943, "e": 34576, "m": 1399, "t": 3549, "c": 1288, "n": 1085, "d": 2320, "b": 743, "g": 853, "h": 259, "p": 1458, "r": 184, "k": 901, "w": 304, "z": 51, "j": 20, "q": 19, "x": 10}, "r": {"tot": 225375, "d": 5668, "k": 1927, "g": 3256, "o": 31100, "r": 5752, "u": 6071, "i": 35622, "e": 40023, "s": 11857, "a": 35216, "t": 8440, "y": 7583, "n": 4308, "v": 1730, "m": 6706, "b": 3087, "p": 3507, "l": 2822, "h": 2076, "c": 5741, "f": 1520, "w": 902, "x": 12, "q": 147, "j": 183, "z": 119}, "d": {"tot": 82298, "v": 375, "w": 494, "e": 22148, "a": 8639, "d": 1822, "o": 8317, "i": 19349, "l": 3017, "u": 3435, "n": 1424, "g": 1029, "s": 2717, "y": 1780, "r": 5029, "h": 479, "p": 184, "c": 201, "f": 343, "j": 294, "m": 619, "t": 145, "z": 40, "b": 358, "k": 46, "q": 12, "x": 2}, "v": {"tot": 32934, "a": 5020, "e": 17745, "o": 2556, "i": 6761, "u": 459, "t": 8, "y": 134, "r": 105, "d": 9, "g": 8, "n": 13, "s": 26, "v": 44, "l": 19, "c": 7, "w": 2, "k": 6, "z": 4, "h": 1, "p": 3, "m": 3, "b": 1}, "k": {"tot": 23279, "s": 1770, "a": 2349, "h": 465, "e": 7885, "i": 4525, "r": 392, "z": 3, "m": 242, "n": 769, "t": 258, "b": 258, "o": 1039, "l": 1194, "u": 485, "c": 58, "k": 132, "p": 140, "v": 30, "w": 299, "y": 670, "d": 62, "f": 191, "g": 36, "j": 25, "q": 1, "x": 1}, "w": {"tot": 21454, "o": 3246, "h": 1459, "a": 4851, "e": 3495, "i": 3643, "l": 615, "n": 959, "s": 719, "r": 739, "t": 166, "m": 145, "u": 112, "y": 160, "b": 243, "p": 103, "w": 82, "g": 50, "d": 250, "f": 137, "k": 180, "c": 71, "j": 5, "z": 20, "q": 2, "v": 2}, "o": {"tot": 248019, "l": 18296, "n": 47067, "g": 10671, "t": 12894, "r": 28809, "s": 15626, "u": 19518, "i": 5816, "m": 17030, "c": 10905, "z": 761, "a": 3667, "h": 1028, "p": 14881, "v": 6396, "b": 4784, "o": 7475, "w": 4375, "d": 7714, "f": 2145, "x": 1995, "k": 1782, "y": 1060, "e": 2840, "q": 329, "j": 155}, "g": {"tot": 63134, "h": 2864, "e": 11916, "o": 4842, "a": 7713, "i": 8527, "g": 2113, "l": 5660, "n": 2781, "y": 2064, "s": 1682, "r": 7272, "m": 845, "u": 3820, "b": 198, "c": 34, "d": 124, "k": 35, "p": 69, "t": 213, "w": 211, "f": 121, "v": 5, "j": 12, "q": 1, "z": 12}, "c": {"tot": 139291, "a": 23273, "i": 11481, "u": 7752, "k": 6525, "l": 5088, "o": 24157, "t": 10302, "e": 14903, "y": 3559, "c": 2385, "h": 19822, "s": 1031, "r": 8336, "m": 52, "n": 228, "p": 42, "q": 178, "x": 1, "d": 53, "b": 23, "f": 19, "w": 20, "g": 14, "v": 2, "z": 45}, "t": {"tot": 210116, "e": 44229, "i": 49645, "o": 21357, "s": 5670, "u": 7301, "h": 16523, "a": 21117, "r": 20370, "j": 67, "t": 5826, "c": 1778, "n": 717, "l": 3471, "m": 882, "y": 7364, "b": 538, "p": 395, "g": 271, "f": 748, "w": 1133, "k": 69, "z": 340, "d": 196, "v": 82, "q": 20, "x": 7}, "s": {"tot": 174618, "v": 130, "c": 9519, "t": 34122, "e": 20839, "a": 9273, "s": 20859, "i": 18106, "g": 267, "h": 11197, "l": 3754, "k": 1825, "o": 8826, "m": 7285, "u": 10456, "y": 3007, "r": 281, "f": 485, "q": 1021, "n": 2573, "p": 8551, "b": 483, "w": 1412, "d": 256, "j": 71, "z": 20}, "b": {"tot": 63303, "a": 8685, "d": 452, "u": 4645, "l": 12412, "o": 6967, "b": 1711, "e": 8859, "y": 596, "i": 8912, "r": 6095, "c": 390, "f": 144, "h": 187, "j": 256, "k": 36, "m": 237, "n": 166, "p": 206, "s": 1525, "t": 492, "v": 141, "w": 78, "g": 87, "x": 4, "z": 10, "q": 10}, "u": {"tot": 130684, "a": 4130, "s": 19837, "l": 14100, "m": 8779, "r": 14229, "e": 3452, "c": 4527, "v": 450, "n": 27616, "d": 3659, "g": 2365, "t": 9310, "x": 403, "p": 5085, "b": 5296, "i": 4152, "z": 280, "o": 1042, "k": 531, "y": 147, "f": 968, "j": 80, "w": 30, "u": 70, "q": 41, "h": 105}, "x": {"tot": 9466, "i": 2140, "a": 1050, "e": 1115, "y": 758, "t": 1180, "o": 759, "m": 33, "u": 285, "p": 972, "l": 60, "c": 613, "b": 41, "f": 41, "h": 190, "s": 101, "w": 37, "r": 13, "d": 18, "k": 2, "n": 13, "g": 13, "q": 13, "x": 10, "z": 1, "v": 8}, "j": {"tot": 5426, "o": 1028, "e": 1055, "u": 1463, "a": 1378, "i": 413, "t": 3, "h": 8, "j": 6, "r": 11, "y": 7, "p": 3, "w": 2, "v": 1, "n": 16, "d": 9, "l": 3, "m": 4, "b": 2, "c": 5, "g": 2, "s": 3, "k": 4}, "f": {"tot": 38066, "f": 3062, "t": 1219, "a": 3561, "u": 3908, "o": 5545, "i": 7027, "e": 5162, "y": 943, "l": 4104, "r": 2832, "b": 49, "d": 40, "g": 24, "s": 318, "w": 42, "z": 6, "n": 44, "v": 2, "k": 12, "c": 39, "h": 42, "m": 45, "p": 29, "j": 8, "x": 3}, "y": {"tot": 33803, "a": 2094, "e": 1694, "s": 3655, "m": 2399, "i": 1441, "r": 2038, "c": 2270, "p": 3739, "g": 911, "l": 3861, "n": 2325, "d": 1489, "t": 2194, "x": 200, "o": 1689, "z": 222, "u": 215, "y": 9, "b": 475, "w": 311, "f": 226, "h": 210, "v": 38, "k": 83, "j": 10, "q": 5}, "m": {"tot": 94809, "a": 19645, "p": 6919, "e": 18877, "b": 4332, "i": 18112, "y": 2804, "o": 12427, "u": 4008, "s": 1851, "h": 80, "m": 3427, "r": 123, "t": 102, "l": 381, "n": 1012, "k": 36, "f": 231, "w": 92, "c": 101, "d": 92, "g": 37, "v": 79, "z": 15, "j": 19, "q": 6, "x": 1}, "p": {"tot": 110926, "e": 17219, "s": 3871, "i": 10292, "t": 4583, "o": 12574, "y": 1788, "h": 16764, "r": 14814, "a": 12543, "n": 540, "p": 3577, "u": 3814, "l": 7341, "m": 224, "j": 20, "d": 94, "x": 1, "b": 205, "c": 142, "f": 176, "w": 187, "k": 71, "g": 73, "v": 8, "z": 1, "q": 4}, "z": {"tot": 14505, "e": 6290, "z": 567, "o": 1848, "i": 2309, "a": 2438, "u": 131, "l": 265, "g": 9, "h": 15, "y": 442, "r": 11, "t": 14, "n": 12, "b": 21, "d": 21, "p": 16, "c": 16, "k": 14, "s": 15, "w": 18, "m": 15, "v": 9, "q": 4, "j": 2, "f": 3}, "q": {"tot": 5853, "u": 5763, "w": 2, "s": 5, "p": 2, "i": 18, "h": 2, "r": 6, "n": 2, "o": 4, "a": 21, "t": 8, "g": 1, "e": 6, "y": 1, "l": 2, "m": 1, "q": 4, "v": 2, "d": 2, "f": 1}}

# dictionary storing the rotor mappings:
# rotor_map = {"A": "B", "C":"D"}
# reflector_map = {1: -2}
# thresh = 7.179214737492013e-06 # Diego said keep this low
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

# # # returns a dict or dict that stores the relative frequency of letter2 appearing after letter1
# f = open("training_all_words.txt", 'r')
# s = f.read()
# lfreq = {}

# for i in range(len(s)-1):
#     l1 = s[i].lower()
#     l2 = s[i+1].lower()

#     if (l1.isalpha() and l2.isalpha()):
#         if l1 not in lfreq:
#             lfreq[l1] = {}
#             lfreq[l1]["tot"] = 0
#         if l2 not in lfreq[l1]:
#             lfreq[l1][l2] = 0
#         lfreq[l1][l2] += 1
#         lfreq[l1]['tot'] += 1

# out = open("trained.txt", "w")
# lfreq = json.dumps(lfreq)
# out.write(lfreq)
# f.close()

'''
REFL_MAP = {
    0:12,
    1:6,
    2:22,
    3:16,
    4:10,
    5:9,
    6:1,
    7:15,
    8:25,
    9:5,
    10:4,
    11:18,
    12:0,
    13:24,
    14:23,
    15:7,
    16:3,
    17:20,
    18:11,
    19:21,
    20:17,
    21:19,
    22:2,
    23:14,
    24:13,
    25:8
}

ALPHA_MAP = {
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7,
    'i':8,
    'j':9,
    'k':10,
    'l':11,
    'm':12,
    'n':13,
    'o':14,
    'p':15,
    'q':16,
    'r':17,
    's':18,
    't':19,
    'u':20,
    'v':21,
    'w':22,
    'x':23,
    'y':24,
    'z':25
}

ROTOR_FW_MAP = {
    'a':'v',
    'b':'z',
    'c':'b',
    'd':'r',
    'e':'g',
    'f':'i',
    'g':'t',
    'h':'y',
    'i':'u',
    'j':'p',
    'k':'s',
    'l':'d',
    'm':'n',
    'n':'h',
    'o':'l',
    'p':'x',
    'q':'a',
    'r':'w',
    's':'m',
    't':'j',
    'u':'q',
    'v':'o',
    'w':'f',
    'x':'e',
    'y':'c',
    'z':'k'
} '''

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
'''

# Resulting lookup map

lu = {
	'a': {
		'a':'g',
		'b':'f',
		'c':'e',
		'd':'i',
		'e':'c',
		'f':'b',
		'g':'a',
		'h':'m',
		'i':'d',
		'j':'n',
		'k':'o',
		'l':'u',
		'm':'h',
		'n':'j',
		'o':'k',
		'p':'v',
		'q':'s',
		'r':'y',
		's':'q',
		't':'w',
		'u':'l',
		'v':'p',
		'w':'t',
		'x':'z',
		'y':'r',
		'z':'x'
	},
	'b': {
		'a':'k',
		'b':'v',
		'c':'m',
		'd':'x',
		'e':'z',
		'f':'u',
		'g':'s',
		'h':'j',
		'i':'r',
		'j':'h',
		'k':'a',
		'l':'p',
		'm':'c',
		'n':'y',
		'o':'w',
		'p':'l',
		'q':'t',
		'r':'i',
		's':'g',
		't':'q',
		'u':'f',
		'v':'b',
		'w':'o',
		'x':'d',
		'y':'n',
		'z':'e'
	},
	'c': {
		'a':'p',
		'b':'u',
		'c':'z',
		'd':'t',
		'e':'s',
		'f':'l',
		'g':'r',
		'h':'x',
		'i':'m',
		'j':'q',
		'k':'w',
		'l':'f',
		'm':'i',
		'n':'o',
		'o':'n',
		'p':'a',
		'q':'j',
		'r':'g',
		's':'e',
		't':'d',
		'u':'b',
		'v':'y',
		'w':'k',
		'x':'h',
		'y':'v',
		'z':'c'
	},
	'd': {
		'a':'v',
		'b':'w',
		'c':'u',
		'd':'q',
		'e':'g',
		'f':'s',
		'g':'e',
		'h':'r',
		'i':'p',
		'j':'l',
		'k':'z',
		'l':'j',
		'm':'n',
		'n':'m',
		'o':'y',
		'p':'i',
		'q':'d',
		'r':'h',
		's':'f',
		't':'x',
		'u':'c',
		'v':'a',
		'w':'b',
		'x':'t',
		'y':'o',
		'z':'k'
	},
	'e': {
		'a':'h',
		'b':'p',
		'c':'k',
		'd':'y',
		'e':'q',
		'f':'v',
		'g':'o',
		'h':'a',
		'i':'n',
		'j':'r',
		'k':'c',
		'l':'s',
		'm':'t',
		'n':'i',
		'o':'g',
		'p':'b',
		'q':'e',
		'r':'j',
		's':'l',
		't':'m',
		'u':'x',
		'v':'f',
		'w':'z',
		'x':'u',
		'y':'d',
		'z':'w'
	},
	'f': {
		'a':'f',
		'b':'r',
		'c':'n',
		'd':'w',
		'e':'o',
		'f':'a',
		'g':'y',
		'h':'q',
		'i':'s',
		'j':'t',
		'k':'l',
		'l':'k',
		'm':'x',
		'n':'c',
		'o':'e',
		'p':'u',
		'q':'h',
		'r':'b',
		's':'i',
		't':'j',
		'u':'p',
		'v':'z',
		'w':'d',
		'x':'m',
		'y':'g',
		'z':'v'
	},
	'g': {
		'a':'m',
		'b':'c',
		'c':'b',
		'd':'h',
		'e':'k',
		'f':'y',
		'g':'x',
		'h':'d',
		'i':'l',
		'j':'o',
		'k':'e',
		'l':'i',
		'm':'a',
		'n':'s',
		'o':'j',
		'p':'q',
		'q':'p',
		'r':'t',
		's':'n',
		't':'r',
		'u':'z',
		'v':'w',
		'w':'v',
		'x':'g',
		'y':'f',
		'z':'u'
	},
	'h': {
		'a':'x',
		'b':'k',
		'c':'h',
		'd':'o',
		'e':'j',
		'f':'m',
		'g':'n',
		'h':'c',
		'i':'w',
		'j':'e',
		'k':'b',
		'l':'t',
		'm':'f',
		'n':'g',
		'o':'d',
		'p':'z',
		'q':'y',
		'r':'v',
		's':'u',
		't':'l',
		'u':'s',
		'v':'r',
		'w':'i',
		'x':'a',
		'y':'q',
		'z':'p'
	},
	'i': {
		'a':'e',
		'b':'y',
		'c':'l',
		'd':'m',
		'e':'a',
		'f':'i',
		'g':'q',
		'h':'o',
		'i':'f',
		'j':'p',
		'k':'s',
		'l':'c',
		'm':'d',
		'n':'u',
		'o':'h',
		'p':'j',
		'q':'g',
		'r':'w',
		's':'k',
		't':'v',
		'u':'n',
		'v':'t',
		'w':'r',
		'x':'z',
		'y':'b',
		'z':'x'
	},
	'j': {
		'a':'t',
		'b':'s',
		'c':'i',
		'd':'f',
		'e':'p',
		'f':'d',
		'g':'m',
		'h':'u',
		'i':'c',
		'j':'z',
		'k':'v',
		'l':'q',
		'm':'g',
		'n':'r',
		'o':'w',
		'p':'e',
		'q':'l',
		'r':'n',
		's':'b',
		't':'a',
		'u':'h',
		'v':'k',
		'w':'o',
		'x':'y',
		'y':'x',
		'z':'j'
	},
	'k': {
		'a':'y',
		'b':'d',
		'c':'x',
		'd':'b',
		'e':'s',
		'f':'p',
		'g':'j',
		'h':'n',
		'i':'v',
		'j':'g',
		'k':'t',
		'l':'w',
		'm':'q',
		'n':'h',
		'o':'u',
		'p':'f',
		'q':'m',
		'r':'z',
		's':'e',
		't':'k',
		'u':'o',
		'v':'i',
		'w':'l',
		'x':'c',
		'y':'a',
		'z':'r'
	},
	'l': {
		'a':'j',
		'b':'f',
		'c':'v',
		'd':'s',
		'e':'x',
		'f':'b',
		'g':'z',
		'h':'t',
		'i':'u',
		'j':'a',
		'k':'q',
		'l':'r',
		'm':'n',
		'n':'m',
		'o':'p',
		'p':'o',
		'q':'k',
		'r':'l',
		's':'d',
		't':'h',
		'u':'i',
		'v':'c',
		'w':'y',
		'x':'e',
		'y':'w',
		'z':'g'
	},
	'm': {
		'a':'d',
		'b':'z',
		'c':'g',
		'd':'a',
		'e':'l',
		'f':'v',
		'g':'c',
		'h':'s',
		'i':'o',
		'j':'y',
		'k':'m',
		'l':'e',
		'm':'k',
		'n':'w',
		'o':'i',
		'p':'x',
		'q':'t',
		'r':'u',
		's':'h',
		't':'q',
		'u':'r',
		'v':'f',
		'w':'n',
		'x':'p',
		'y':'j',
		'z':'b'
	},
	'n': {
		'a':'s',
		'b':'m',
		'c':'z',
		'd':'p',
		'e':'f',
		'f':'e',
		'g':'v',
		'h':'w',
		'i':'y',
		'j':'t',
		'k':'r',
		'l':'u',
		'm':'b',
		'n':'x',
		'o':'q',
		'p':'d',
		'q':'o',
		'r':'k',
		's':'a',
		't':'j',
		'u':'l',
		'v':'g',
		'w':'h',
		'x':'n',
		'y':'i',
		'z':'c'
	},
	'o': {
		'a':'l',
		'b':'e',
		'c':'s',
		'd':'x',
		'e':'b',
		'f':'w',
		'g':'p',
		'h':'k',
		'i':'j',
		'j':'i',
		'k':'h',
		'l':'a',
		'm':'r',
		'n':'t',
		'o':'y',
		'p':'g',
		'q':'v',
		'r':'m',
		's':'c',
		't':'n',
		'u':'z',
		'v':'q',
		'w':'f',
		'x':'d',
		'y':'o',
		'z':'u'
	},
	'p': {
		'a':'u',
		'b':'g',
		'c':'j',
		'd':'o',
		'e':'t',
		'f':'z',
		'g':'b',
		'h':'i',
		'i':'h',
		'j':'c',
		'k':'w',
		'l':'s',
		'm':'y',
		'n':'q',
		'o':'d',
		'p':'v',
		'q':'n',
		'r':'x',
		's':'l',
		't':'e',
		'u':'a',
		'v':'p',
		'w':'k',
		'x':'r',
		'y':'m',
		'z':'f'
	},
	'q': {
		'a':'b',
		'b':'a',
		'c':'f',
		'd':'r',
		'e':'g',
		'f':'c',
		'g':'e',
		'h':'j',
		'i':'q',
		'j':'h',
		'k':'s',
		'l':'v',
		'm':'x',
		'n':'z',
		'o':'t',
		'p':'w',
		'q':'i',
		'r':'d',
		's':'k',
		't':'o',
		'u':'y',
		'v':'l',
		'w':'p',
		'x':'m',
		'y':'u',
		'z':'n'
	},
	'r': {
		'a':'c',
		'b':'u',
		'c':'a',
		'd':'l',
		'e':'h',
		'f':'o',
		'g':'m',
		'h':'e',
		'i':'n',
		'j':'x',
		'k':'p',
		'l':'d',
		'm':'g',
		'n':'i',
		'o':'f',
		'p':'k',
		'q':'r',
		'r':'q',
		's':'z',
		't':'y',
		'u':'b',
		'v':'w',
		'w':'v',
		'x':'j',
		'y':'t',
		'z':'s'
	},
	's': {
		'a':'f',
		'b':'n',
		'c':'p',
		'd':'q',
		'e':'j',
		'f':'a',
		'g':'h',
		'h':'g',
		'i':'v',
		'j':'e',
		'k':'x',
		'l':'z',
		'm':'o',
		'n':'b',
		'o':'m',
		'p':'c',
		'q':'d',
		'r':'y',
		's':'t',
		't':'s',
		'u':'w',
		'v':'i',
		'w':'u',
		'x':'k',
		'y':'r',
		'z':'l'
	},
	't': {
		'a':'j',
		'b':'i',
		'c':'k',
		'd':'e',
		'e':'d',
		'f':'q',
		'g':'w',
		'h':'y',
		'i':'b',
		'j':'a',
		'k':'c',
		'l':'p',
		'm':'z',
		'n':'u',
		'o':'x',
		'p':'l',
		'q':'f',
		'r':'t',
		's':'v',
		't':'r',
		'u':'n',
		'v':'s',
		'w':'g',
		'x':'o',
		'y':'h',
		'z':'m'
	},
	'u': {
		'a':'q',
		'b':'l',
		'c':'t',
		'd':'f',
		'e':'i',
		'f':'d',
		'g':'y',
		'h':'x',
		'i':'e',
		'j':'m',
		'k':'n',
		'l':'b',
		'm':'j',
		'n':'k',
		'o':'v',
		'p':'z',
		'q':'a',
		'r':'u',
		's':'w',
		't':'c',
		'u':'r',
		'v':'o',
		'w':'s',
		'x':'h',
		'y':'g',
		'z':'p'
	},
	'v': {
		'a':'n',
		'b':'w',
		'c':'r',
		'd':'p',
		'e':'m',
		'f':'g',
		'g':'f',
		'h':'o',
		'i':'l',
		'j':'s',
		'k':'t',
		'l':'i',
		'm':'e',
		'n':'a',
		'o':'h',
		'p':'d',
		'q':'x',
		'r':'c',
		's':'j',
		't':'k',
		'u':'v',
		'v':'u',
		'w':'b',
		'x':'q',
		'y':'z',
		'z':'y'
	},
	'w': {
		'a':'x',
		'b':'s',
		'c':'w',
		'd':'j',
		'e':'q',
		'f':'r',
		'g':'z',
		'h':'k',
		'i':'t',
		'j':'d',
		'k':'h',
		'l':'o',
		'm':'u',
		'n':'v',
		'o':'l',
		'p':'y',
		'q':'e',
		'r':'f',
		's':'b',
		't':'i',
		'u':'m',
		'v':'n',
		'w':'c',
		'x':'a',
		'y':'p',
		'z':'g'
	},
	'x': {
		'a':'z',
		'b':'g',
		'c':'n',
		'd':'v',
		'e':'y',
		'f':'j',
		'g':'b',
		'h':'l',
		'i':'o',
		'j':'f',
		'k':'u',
		'l':'h',
		'm':'q',
		'n':'c',
		'o':'i',
		'p':'t',
		'q':'m',
		'r':'w',
		's':'x',
		't':'p',
		'u':'k',
		'v':'d',
		'w':'r',
		'x':'s',
		'y':'e',
		'z':'a'
	},
	'y': {
		'a':'s',
		'b':'x',
		'c':'v',
		'd':'g',
		'e':'p',
		'f':'y',
		'g':'d',
		'h':'z',
		'i':'q',
		'j':'k',
		'k':'j',
		'l':'n',
		'm':'w',
		'n':'l',
		'o':'r',
		'p':'e',
		'q':'i',
		'r':'o',
		's':'a',
		't':'u',
		'u':'t',
		'v':'c',
		'w':'m',
		'x':'b',
		'y':'f',
		'z':'h'
	},
	'z': {
		'a':'c',
		'b':'o',
		'c':'a',
		'd':'z',
		'e':'v',
		'f':'x',
		'g':'u',
		'h':'n',
		'i':'k',
		'j':'y',
		'k':'i',
		'l':'t',
		'm':'r',
		'n':'h',
		'o':'b',
		'p':'s',
		'q':'w',
		'r':'m',
		's':'p',
		't':'l',
		'u':'g',
		'v':'e',
		'w':'q',
		'x':'f',
		'y':'j',
		'z':'d'
	}
}



'''
Encrypts a plain text with the Pringles-ENIGMA machine.
'''

def encrypt():
    initial_pos = 'a'    # Rotor Starting Position
    #message = "the fox jumps"
    message = "enter"
    encrypted = ''
    message2 = '' #to only keep valid characters in lower case

    # Index lookup table and encrypt.
    for ch in message:
        if not ch.isalpha():
            continue
        ch = ch.lower()
        message2 += ch
        encrypted += lu[initial_pos][ch]
        initial_pos = chr(ord(initial_pos) - 1)
        if initial_pos < "a":
            initial_pos = "z"
    '''
    # Testing if the decryption returns the exact result
    y = decrypt(encrypted, lfreq)
    if (y == message2):
        encrypted += " - " + "Success"
    else:
         encrypted += " - " + "Failed"
    encrypted = message2 + " -> " + encrypted
    '''
    return encrypted    # return encrypted text
    


def decrypt(enc_text, lfreq):
    g = [] # guesses for plaintext
    look_up_dict = lu
    # look_up_dict = read_look_up_dict_file()
    for key1 in look_up_dict: # enumerate through each possible initial position
        #print('rotor position: ' + key1)
        dec_text = ""
        initial_pos = key1
        curr_dict = look_up_dict[initial_pos]

        # 2-GRAM SLIDING WINDOW
        prev = ""
        next = ""

        for i in range(len(enc_text)):
            c = enc_text[i].lower()
            dec_text += curr_dict[c]

            next = curr_dict[c] # 2-GRAM SLIDING WINDOW
            
            #print(prev + next, end=' ')

            # « Rotor rotates by one notch »
            initial_pos = chr(ord(initial_pos) - 1)
            if initial_pos < "a":
                initial_pos = "z"

            curr_dict = look_up_dict[initial_pos]

            # # TRAINING CODE
            # # check with training text
            # if (prev!=""):
            #     # Case 1: No such bigram (2-gram) exists!
            #     if (next not in lfreq[prev].keys()):
            #         dec_text = ""
            #         print("NOPE", end=' ')
            #         break

            #     numer = lfreq[prev][next] # number of times letter c appears after letter prev
            #     denom = lfreq[prev]['tot'] # number of times letter prev appears

            #     # Case 2: Bigram exists, but does not exceed threshold for appropriateness
            #     if ((numer/denom) <= thresh):
            #         dec_text = ""
            #         break

            prev = next # 2-GRAM SLIDING WINDOW

        #print(dec_text)
        if (dec_text != ""):
            g.append(dec_text)
        
    # further reduce possibilities
    g_chi_sqrd = chi_sqrd(g)

    final_dec_text = g[0]
    min = g_chi_sqrd[0]
    for i in range(len(g)):
        chi_sqrd_val = g_chi_sqrd[i]
        if (chi_sqrd_val<min):
            final_dec_text = g[i]
            min = chi_sqrd_val
    return final_dec_text

def chi_sqrd(g):
    #array of floats, same length as g, each index corresponding to same index in g
    g_chi_sqrd =[]

    #get exp_freqs from training data
    exp_freqs = {}
    for ch in lfreq:
        num = lfreq[ch]['tot']
        exp_freqs[ch] = num

    #get observed frequencies for each possible dec_text g[i]
    #then computer chi_squared and store it in g_chi_sqrd[i]
    for i in range(len(g)):
        dec_text = g[i]
        dec_text_freqs = {}
        for ch in dec_text:
            if ch not in dec_text_freqs:
                dec_text_freqs[ch] = 0
            dec_text_freqs[ch] += 1
        val = compute_chi_sqrd(exp_freqs, dec_text_freqs)
        g_chi_sqrd.append(val)
    return g_chi_sqrd

def compute_chi_sqrd(exp_freqs, dec_text_freqs):
    sum = 0.0
    for ch in exp_freqs:
        exp_freq = exp_freqs[ch]
        obs_freq = 0
        if ch in dec_text_freqs:
            obs_freq = dec_text_freqs[ch]
        freq_diff = obs_freq - exp_freq
        sum += ((freq_diff)**2)/exp_freq
    return sum



def main():

    print(encrypt())
    '''
    f = open("enc_text.txt",'w')
    enc_text = encrypt()
    f.write(enc_text)
    f.close()


    parser = argparse.ArgumentParser(description='Get the encrypted text.')
    parser.add_argument('encrypted_text', help='an integer for the accumulator')
    args = parser.parse_args()

    #training
    # lfreq = training() # Created ahead of time, discuss this with the group - Diego
    # open text file and store it in a string
    enc_f = open(args.encrypted_text, 'r')
    enc_text = enc_f.read()
    enc_f.close()

    # ch-sqaured???
    final_dec_text = decrypt(enc_text, lfreq)
    print(final_dec_text)
    '''


if __name__=="__main__":
    main()