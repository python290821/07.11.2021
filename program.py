
# example:
# print( {i:i for i in range(10) if i > 0} )

# 1
# create the following dictionary:
# { 1: 1, 2: 4, 3: 9, 4: 16 ... 10: 100}
print( { i:i**2 for i in range(1, 11) } )

# 2
# ['I', 'Love', 'Python', 'Today']
# create the following dictionary:
# { 'I': 1, 'Love': 4, 'Python': 5 ...}
_words = ['I', 'Love', 'Python', 'Today']
print( { w:len(w) for w in _words  })

# 2.1
# {'jack': 38, 'john': 33 'michael': 48, 'guido': 57 }
# create the following dictionary:
# { 'jack': 38 ... only for items which the value is even}
_d1 = {'jack': 38, 'john': 33, 'michael': 48, 'guido': 57 }
# print({ k: _d1[k] for k in _d1() if _d1[k] % 2 == 0}) # slower
print({ k: v for k,v in _d1.items() if v % 2 == 0})

# 2.2
# { 'jack': 'below_40', 'john':'below_40', 'michael':'above_eq_40' ...}
print({ k:('below_40' if v < 40 else 'above_eq_40') for k,v in _d1.items() })

