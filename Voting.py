import sys
TotalNumber = 0
LineCounter = 1
VoteNumber = 0
Candidates = []
AllVotes = []
Flag = True


class Ballot
	def __init__(self):
	
	
class Candidate
	def __init__(self):
	


def voting_read(s):
	global LineCounter
	global Candidates
	global VoteNumber
	global TotalNumber
	global FirstVote
	global AllVotes
	global Flag
	prev = " "
	CurrentLine = s.readline()
	if LineCounter == 1:
		TotalNumber = int(CurrentLine)
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
	x = 1
	
def voting_print(ans, w):
	#w.write(ans)
	x=1

def voting_solve(r, w):
	for i in range(64):
		a = voting_read(r)
		#voting_print(a, w)
	






voting_solve(sys.stdin, sys.stdout)
print(str(AllVotes) +" "+ str(TotalNumber) +" "+ str(VoteNumber) + " " + str(Candidates))