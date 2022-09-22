LETTER_FREQUENCY_DIST = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
LETTER_COUNT = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

f = open("1984.txt", 'r')
s = f.read()

total = 0

for i in range(len(s)):
    if s[i].isalpha():
        total += 1
        LETTER_COUNT[ord(s[i].lower())-97] += 1

print(LETTER_COUNT)
for j in range(len(LETTER_COUNT)):
    LETTER_FREQUENCY_DIST[j] = LETTER_COUNT[j] / total
    print(LETTER_FREQUENCY_DIST[j], chr(j+97))
print(LETTER_FREQUENCY_DIST)
