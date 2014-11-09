#DNA sequence parser

#import needed modules
from re import findall
import csv

f = open("WMn_S173_L001_R1_001 - Copy.txt",'r')
reader = csv.reader(f)

rawData = []
for i in reader:
    rawData.append(i)
f.close()

index = 1
sequences = []
for i in range(len(rawData)):
    if index < len(rawData):
        sequences.append(rawData[index])
        index = index+4

f = open("sequences.txt",'w',newline='')
writer = csv.writer(f)
writer.writerows(sequences)
f.close()
