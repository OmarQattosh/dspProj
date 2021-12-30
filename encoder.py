
import numpy as py
import csv

import scipy.io.wavfile as wavf

import matplotlib.pyplot as plot
file=open('data.csv')
type(file)
csvreader = csv.reader(file)
rows= []
for row in csvreader:
    rows.append(row)
#print(rows)
file.close()
Samplefreq= 8000
SampleRate=320
n = py.linspace(0,320,320)
toencode=input("Please Enter the String to Encode: ")
siglist = []
for c in toencode:
    for i in range(0,len(rows)):
        if c.lower() == rows[i][0]:
            if c.islower():
            
                tmp=py.cos(2*py.pi*int(rows[i][1])*n/Samplefreq)+py.cos(2*py.pi*int(rows[i][2])*n/Samplefreq)+py.cos(2*py.pi*int(rows[i][3])*n/Samplefreq)+py.cos(2*py.pi*100*n/Samplefreq)
                siglist.append(tmp)
            else:
                tmp=py.cos(2*py.pi*int(rows[i][1])*n/Samplefreq)+py.cos(2*py.pi*int(rows[i][2])*n/Samplefreq)+py.cos(2*py.pi*int(rows[i][3])*n/Samplefreq)+py.cos(2*py.pi*200*n/Samplefreq)
                siglist.append(tmp)

out_f = 'out.wav'
for j in range(1,len(siglist)):
     siglist[0]=py.append(siglist[0],siglist[j])
print(siglist[0])
wavf.write(out_f, SampleRate, siglist[0])
plot.plot(siglist[0])
plot.show()

    





