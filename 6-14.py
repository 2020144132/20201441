mystr = 'x-DSPAM-Confidence:0.8475'
atpos = mystr.find( ' : ')
host = mystr[atpos+1 :]
print(host)
print(float(host))