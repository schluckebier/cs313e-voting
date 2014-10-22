import sys


# ------------
# voting_read
# ------------

def voting_read (r) :
    """
    
    """
    s = r.readline()
    return s
    
    

# ------------
# voting_eval
# ------------

"""
def voting_eval (i, j) :
    
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    ________________________
    A function is given a value.
    If the value is new to the fuction it calculates its cycle length and stores it.
    it it has seen the value it looks up the value (Cache)
    This cycle length is compared to the current max cycle length to find the overall max.
    


    if i > j:#switch values if j is smaller
        i,j = j,i
    assert i <= j
    assert i>=0
    assert j>=0
    if j//2+1 > i:#use optimization which removes values less than half the larger value
        i = j//2+1
    MaxCycleLength=1
    def CycleCounter(num):#fuction which finds cycle length and if its a new value adds the value and its cycle lenght to a dictionary. if its a value already stored in the dictionary, then cycle length is looked up rather than re calculated. 
        TempNum=num
        CycleLength = 1
        while num > 1:
            if num in CacheDic:
                CycleLength += CacheDic[num]-1
                num = 1
            elif num % 2 == 0:
                num =  num//2
                CycleLength+= 1
            else:
                num = ((num*3)+1)//2
                CycleLength+=2
        CacheDic[TempNum]= CycleLength
        return CycleLength

 
                      
    
    for x in range (i, j+1):#tests the cycle length against the max. if the value is bigger then it is the new max
        tempcount = CycleCounter(x)
        if tempcount>MaxCycleLength:
            MaxCycleLength=tempcount

    return MaxCycleLength#return max
    assert MaxCycleLength >= 1

"""
# -------------
# voting_print
# -------------

def voting_print (v, w) :
    """
    """
    w.write(str(v) + "\n")

# -------------
# voting_solve
# -------------

def voting_solve (r, w) :
    """
    """
    a = voting_read(r)
    voting_print(a, w)
	
voting_solve(sys.stdin, sys.stdout)
