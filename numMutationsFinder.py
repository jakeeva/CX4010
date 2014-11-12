#Number of mutations finder

f = open("Original Sequence.txt",'r')
original = f.read().strip()
f.close()

f = open("sequences.txt")
sequences = f.readlines()
f.close()
for i in range(len(sequences)):
    sequences[i] = sequences[i].strip()

mutated = []
for i in sequences:
    if i != original:
        mutated.append(i)

