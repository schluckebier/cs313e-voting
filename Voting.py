#David Schluckebier

TotalCases = 0
LineCounter = 1
VoteNumber = 0
Candidates = []
AllVotes = []
CaseCount = 1
candic = {}
Flag = True



class Ballot:
	'''
	adds atributes ballot number and ballot id
	'''
	def __init__(self, baln, balid):
		self.baln = baln
		self.balid = balid
			
	
			
			
	

class Candidate:
	'''
	add atributes candidate number, candidate id, a list of their ballots, and if they are a loser
	'''
	def __init__(self, cann, canid):
		self.cann = cann
		self.canid = canid
		self.ballist = []
		self.loser = False
		
	def totalvotes(self):
		return len(self.ballist)
		
def firstnum(s):
	'''
	identifies how many cases will be run
	'''
	global LineCounter
	global TotalCases
	
	CurrentLine = s.readline()
	if LineCounter == 1:
		TotalCases = int(CurrentLine)
	LineCounter+=1	

	


def voting_read(s):
	'''
	reads all the lines that aren't the first line and puts them into the correct data store
	'''
	global LineCounter
	global Candidates
	global VoteNumber
	global TotalCases
	global FirstVote
	global AllVotes

	global CaseCount

	prev = " "
	CurrentLine = s.readline()
	if CurrentLine == "":
		a = voting_eval()
		
		if type(a) == str:
			return(a)
		else:
			b = []
			for i in a:
				b.append(candic[i])
			return(b)
		
	if LineCounter == 3:
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
	elif (LineCounter >4 and CurrentLine == '\n'):
		a = voting_eval()
		
		if type(a) == str:
			return(a)
		else:
			b = []
			for i in a:
				b.append(candic[i])
			return(b)
		
	LineCounter += 1




def checkEqual(i):
	'''
	checks if two values are equal
	'''
	try:
		i = iter(i)
		first = next(i)
		return all(first == rest for rest in i)
	except StopIteration:
		return True


def voting_eval():
	'''
	runs the Australian voting algorithm
	uses global variables so I can't run it in unittests so I have bad coverage
	'''
	global LineCounter
	global Candidates
	global VoteNumber
	global TotalCases
	global FirstVote
	global AllVotes
	global Flag
	global candic
	global CaseCount
	
	
	baldic = {}
	b = iter(AllVotes)
	for k in range (1, len(AllVotes)+1):
		baldic[k] = next(b)
		
	Realbaldic = {}
	for k in range (1, len(AllVotes)+1):
		Realbaldic[k] = Ballot(baldic[k], k)
	
	
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
		
	WinCount = 0.0
	for i in range (1, len(AllVotes)+1):
		WinCount += 1.0
		WinMark = WinCount/2
	
	def MakeCanCount():
		CanCount = {}
		for i in range (1, VoteNumber+1):
			if Realcandic[i].loser == False:
				CanCount[i]=((len(Realcandic[i].ballist)))
		return CanCount
		
	winner = False
	Tie = False
	
		
	while winner == False and Tie == False:
		
		CanCount = MakeCanCount()
		for i in range (1, VoteNumber+1):
			if len(Realcandic[i].ballist) > WinMark:
				winner = True
				LineCounter = 3
				VoteNumber = 0
				Candidates = []
				AllVotes = []
				return Realcandic[i].cann
			if len(Realcandic[i].ballist) == 0:
				Realcandic[i].loser = True
		if checkEqual(CanCount.values()):
				LineCounter = 3
				VoteNumber = 0
				Candidates = []
				AllVotes = []
				tie = True
				return CanCount.keys()
					
				
		for i in range (1, VoteNumber+1):
			if min(CanCount.values()) == len(Realcandic[i].ballist):
				for k in range (len(Realcandic[i].ballist)):
					for p in range (1, VoteNumber):
						if Realcandic[Realcandic[i].ballist[k].baln[p]].loser == False:
							Realcandic[Realcandic[i].ballist[k].baln[p]].ballist.append(Realcandic[i].ballist[k])
							Realcandic[i].loser = True
						break
		
				
			

def voting_print(ans, w):
	'''
	prints either a elements of a list on a newline or prints a string
	'''
	global TotalCases
	global CaseCount
	if ans == None:
		x=1
	elif type(ans)== list:
		for i in ans:
			w.write(i + "\n")
		w.write("\n")
		CaseCount+=1
	else:
		w.write(ans + "\n" + "\n")
		CaseCount+=1

def voting_solve(r, w):
	'''
	the caller to the rest of the program
	has a read and a writer 
	'''
	global TotalCases
	global CaseCount
	firstnum(r)
	while CaseCount <= TotalCases:
		
		u = voting_read(r)
		
		voting_print(u, w)
		
		



