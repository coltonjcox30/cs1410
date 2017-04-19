def main():
	filenameT = raw_input('Target strand filename: ')
	finT=open(filenameT,'r')
	filenameC = raw_input('Candidate strands filename: ')
	finC=open(filenameC, 'r')
	cand = []
	for line in finC:
		cand.append(line.strip())
	target= finT.readline().strip()
	for c in cand:
		comparestrands(target,c)

def comparestrands(T,C):
    for i in range(len(C)):
	if T[i:]== C[:len(C)-i]:
		print T+C[len(C)-i:]


main()

            
                     
    
