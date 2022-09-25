def main():
    lfreq = {}
    f = open('dict.txt','r')
    tot = 0
    for line in f:
        l = line.strip().split()
        freq = int(l[1])
        lfreq[l[0]] = freq
        tot += freq
    #for key in lfreq:
        #lfreq[key]=lfreq[key]/tot
    print(lfreq)
    f.close()

if __name__=="__main__":
    main()