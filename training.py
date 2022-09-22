import json

f = open("training_all_words.txt", 'r')
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

out = open("trained.txt", "w")
lfreq = json.dumps(lfreq)
out.write(lfreq)
f.close()