from scipy import signal
import numpy as py
import csv
from scipy import signal as sg
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
toencode=input()
siglist = []

for c in toencode:
    for i in range(0,len(rows)):
        
        if c.lower() == rows[i][0]:
            if c.islower():
                print("hi") 
                tmp=py.cos(2*py.pi*int(rows[i][1])*n/Samplefreq)+py.cos(2*py.pi*int(rows[i][2])*n/Samplefreq)+py.cos(2*py.pi*int(rows[i][3])*n/Samplefreq)+py.cos(2*py.pi*100*n/Samplefreq)
                siglist.append(tmp)
            else:
                tmp=py.cos(2*py.pi*int(rows[i][1])*n/Samplefreq)+py.cos(2*py.pi*int(rows[i][2])*n/Samplefreq)+py.cos(2*py.pi*int(rows[i][3])*n/Samplefreq)+py.cos(2*py.pi*200*n/Samplefreq)
                siglist.append(tmp)
            
plot.plot(tmp)
plot.show()

    





