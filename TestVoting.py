
# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Voting import firstnum, voting_eval, voting_print, voting_solve

# -----------
# TestVoting
# -----------

class TestVoting (TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r    = StringIO("1\n\n4\nMouse\nDog\nCat\nMoose\n1 2 3 4\n1 2 3 4\n1 2 3 4\n1 2 3 4\n1 2 3 4\n1 2 3 4\n1 2 3 4\n1 2 3 4\n")
        i = firstnum(r)
        self.assertEqual(i,  None)


    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        l = ['a', 'b', 'c']
        voting_print(l, w)
        self.assertEqual(w.getvalue(), 'a\nb\nc\n\n')
        
    def test_print_2 (self) :
        w = StringIO()
        l = ['one', 'two', 'three']
        voting_print(l, w)
        self.assertEqual(w.getvalue(), 'one\ntwo\nthree\n\n')
        
    def test_print_3 (self) :
        w = StringIO()
        l = ['Dallas Cowboys', 'Houston Texans', 'Buffalo Bills']
        voting_print(l, w)
        self.assertEqual(w.getvalue(), 'Dallas Cowboys\nHouston Texans\nBuffalo Bills\n\n')
        
    def test_print_4 (self) :
        w = StringIO()
        l = ['11', '12', '13']
        voting_print(l, w)
        self.assertEqual(w.getvalue(), '11\n12\n13\n\n')
        
    def test_print_5 (self) :
    	w = StringIO()
    	l = ['Dog', 'Cat', 'Moose']
    	voting_print(l, w)
    	self.assertEqual(w.getvalue(), 'Dog\nCat\nMoose\n\n')
    	
    def test_print_6 (self) :
    	w = StringIO()
    	l = 'Hello'
    	voting_print(l, w)
    	self.assertEqual(w.getvalue(), 'Hello\n\n')
    	
    def test_print_7 (self) :
    	w = StringIO()
    	l = 'Goodbye'
    	voting_print(l, w)
    	self.assertEqual(w.getvalue(), 'Goodbye\n\n')
    	
    def test_print_8 (self) :
    	w = StringIO()
    	l = ['Dog', 'Cat', 'Moose']
    	voting_print(l[1], w)
    	self.assertEqual(w.getvalue(), 'Cat\n\n')

    def test_print_9 (self) :
    	w = StringIO()
    	l = ['Dog', 'Cat', 'Moose']
    	voting_print(l[0], w)
    	self.assertEqual(w.getvalue(), 'Dog\n\n')

    def test_print_10 (self) :
    	w = StringIO()
    	l = ['Dog', 'Cat', 'Moose']
    	voting_print(l[2], w)
    	self.assertEqual(w.getvalue(), 'Moose\n\n')

    def test_print_11 (self) :
    	w = StringIO()
    	l = 'Testing'
    	voting_print(l, w)
    	self.assertEqual(w.getvalue(), 'Testing\n\n')

    def test_print_12 (self) :
    	w = StringIO()
    	l = 'Does this work?'
    	voting_print(l, w)
    	self.assertEqual(w.getvalue(), 'Does this work?\n\n')
    	

    

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1\n\n3\na\nb\nc\n1 2 3\n1 3 2\n3 1 2\n")
        w = StringIO()
        voting_solve(r, w)
        self.assertEqual(w.getvalue(), '')

    def test_solve_2 (self) :
        r = StringIO("1\n\n4\nMouse\nDog\nCat\nMoose\n1 2 3 4\n1 2 3 4\n1 2 3 4\n1 2 3")
        w = StringIO()
        voting_solve(r, w)
        self.assertEqual(w.getvalue(), '')
        
    

# ----
# main
# ----

main()
