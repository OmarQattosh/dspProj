import numpy as py
import csv
import scipy.io.wavfile as wavf
import matplotlib.pyplot as plot
from scipy.fft import fft, ifft
from scipy.signal import find_peaks
import wave
import wave, struct

samplerate,data=wavf.read('out.wav')
file=open('data.csv')
type(file)
csvreader = csv.reader(file)
rows= []
for row in csvreader:
    rows.append(row)
   
file.close()
test=py.array_split(data,len(data)/320)
bigstring=''
letter=''

for i in range(0,len(test)):
    
    y=fft(test[i],128)

    yf= abs(y)

    peakkind , _=find_peaks(yf)
    print(peakkind)
    if peakkind[1] == 13 and peakkind[2]== 16:
        if peakkind[3] ==26:
            letter ='s'
        elif peakkind[3] == 39:
            letter ='t'
        elif peakkind [3] == 64:
            letter ='u'
    if peakkind[2] ==26 and peakkind[3] ==32:
        if peakkind[1]== 6:
            letter ='g'
        elif peakkind[1] == 10:
            letter = 'p'
        elif peakkind[1]==16:
            letter = 'y'    
    for p in range(0,len(peakkind)):
        peakkind[p] = peakkind[p] *64
        
        #print(peakkind[p])
 
    for i in range(0,len(rows)):
        if abs(int(rows[i][1])- peakkind[1])<100:
            if (abs(int(rows[i][2])- peakkind[2]))<100:
                if (abs(int(rows[i][3])- peakkind[3])) < 100:
                    letter= rows[i][0]
    bigstring=bigstring + letter
    print(bigstring)



