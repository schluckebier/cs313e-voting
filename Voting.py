import sys
TotalCases = 0
LineCounter = 1
VoteNumber = 0
Candidates = []
AllVotes = []

Flag = True



class Ballot:
	def __init__(self, baln, balid):
		self.baln = baln
		self.balid = balid
			
	
			
			
	

class Candidate:
	def __init__(self, cann, canid):
		self.cann = cann
		self.canid = canid
		self.ballist = []
		
	def totalvotes(self):
		return len(self.ballist)
		

		

	
	
	


def voting_read(s):
	global LineCounter
	global Candidates
	global VoteNumber
	global TotalCases
	#global FirstVote
	global AllVotes
	#global Flag
	prev = " "
	CurrentLine = s.readline()
	if LineCounter == 1:
		TotalCases = int(CurrentLine)
	elif LineCounter == 3:
		VoteNumber = int(CurrentLine)
	elif LineCounter >= 4 and LineCounter < 4 + VoteNumber:
		Candidates.append(CurrentLine.rstrip("\n"))
	elif (LineCounter >= 4 + VoteNumber) and CurrentLine !='\n':
		CurrentVotes = []
		for i in CurrentLine:
			if i != "\n":
				if prev == " ":
					CurrentVotes.append(int(i))
				elif i != " " and prev != " ":
					CurrentVotes[-1] = int(prev + i)
			prev = i
		AllVotes += [CurrentVotes]
	elif LineCounter >4 and CurrentLine == '\n':
		voting_eval()
		
	LineCounter += 1

def voting_eval():

	WinMark = len(AllVotes)/2
	baldic = {}
	b = iter(AllVotes)
	for k in range (1, len(AllVotes)+1):
		baldic[k] = next(b)
		
	Realbaldic = {}
	for k in range (1, len(AllVotes)+1):
		Realbaldic[k] = Ballot(baldic[k], k)
	
	
	candic = {}
	a = iter(Candidates)
	for i in range (1, VoteNumber+1):
		candic[i] = next(a)
		
	Realcandic = {}
	for i in range (1, VoteNumber+1):
		Realcandic[i] = Candidate(candic[i], i)
		
	for Balid in range (1, len(AllVotes)+1):
		for Canid in range (1, VoteNumber+1):
			if Realbaldic[Balid].baln[0] == Realcandic[Canid].canid:
				Realcandic[Canid].ballist.append( Realbaldic[Balid])
				
	for i in range (1, len(Candidates)+1):
		if Realcandic[i].totalvotes() > WinMark:
			
			print( Realcandic[i].cann)
			
			 
		
			
	
	
	
	
		
	
		
	
	
	
		
	
	
	
		
	
	
def voting_print(ans, w):
	#w.write(ans)
	x=1

def voting_solve(r, w):
	for i in range(64):
		a = voting_read(r)
		#voting_print(a, w)
	






voting_solve(sys.stdin, sys.stdout)
#print(str(AllVotes) +" "+ str(TotalCases) +" "+ str(VoteNumber) + " " + str(Candidates))