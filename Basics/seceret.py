newstr = input("Enter a string :")
words = newstr.split(" ")
coding = input("1 for Coding or 0 for Decoding")
coding = True if (coding=="1") else False

if(coding):
    nwords=[]
    for word in words:
        if(len(word)>=3):
            r1 = "asd"
            r2 = "lka"
            stnew = r1 + word[1:] + word[0]  + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if(len(word)>=3):
            stnew = word[3:-3]
            stnew = stnew[-1] +stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))