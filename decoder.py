import numpy as py
import csv
import scipy.io.wavfile as wavf
import matplotlib.pyplot as plot
from scipy.fft import fft, ifft
from scipy.signal import find_peaks
samplerate,data=wavf.read('out.wav')
#print(data)
y=fft(data,128)
yf= abs(y[1:64])

peakkind , _=find_peaks(yf)

for p in range(0,len(peakkind)):
    peakkind[p] = peakkind[p] *64
    print(peakkind[p])
   

file=open('data.csv')
type(file)
csvreader = csv.reader(file)
rows= []
for row in csvreader:
    rows.append(row)
#print(rows)
file.close()

for i in range(0,len(rows)):
   
    if abs(int(rows[i][1])- peakkind[1])< 100:
        if (abs(int(rows[i][2])- peakkind[2]))<100:
             if (abs(int(rows[i][3])- peakkind[3])) < 100:
                 letter= rows[i][0]
print(letter)                 




