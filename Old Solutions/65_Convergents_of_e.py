#Project Euler # 65: Convergents of e

#Need to create two lists. One list has the infinite continued 1st terms, the other the numerators

import os


numeratorlist = [2,3,8]

for b in range(2,35):

	numeratorlist += [numeratorlist[-2]+numeratorlist[-1]]

	numeratorlist += [numeratorlist[-2]+numeratorlist[-1]]

	numeratorlist += [numeratorlist[-1]*2*b+numeratorlist[-2]]

digsum = 0

for c in range(0,len(str(numeratorlist[99]))):

	digsum += int(str(numeratorlist[99])[c])



print(digsum)
os.system('pause')
