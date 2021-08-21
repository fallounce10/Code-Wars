def zero(operator=None): return 0 if not operator else operator(0)
def one(operator=None): return 1 if not operator else operator(1)
def two(operator=None): return 2 if not operator else operator(2)
def three(operator=None): return 3 if not operator else operator(3)
def four(operator=None): return 4 if not operator else operator(4)
def five(operator=None): return 5 if not operator else operator(5)
def six(operator=None): return 6 if not operator else operator(6)
def seven(operator=None): return 7 if not operator else operator(7)
def eight(operator=None): return 8 if not operator else operator(8)
deg nine(operator=None): return 9 if not operator else operator(9)

plus(number): return lambda x: x + number
minus(number): return lambda x: x - number 
times(number): return lambda x: x * number
divided_by(number): return lambda x: x // number
