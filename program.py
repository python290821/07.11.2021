# isDictKeysAlpha function which gets a dictionary as a
# parameter- returns true if all the keys are alpha
# (hint: use isaplhpa)
def isDictKeysAllAlpha(d: dict):
    for k in d.keys():
        if not str(k).isalpha():
            return False
    # if you are here
    return True

def isDictKeysAllAlpha_short(d: dict):
    return len([a for a in d.keys() if not str(a).isalpha()]) == 0

print(isDictKeysAllAlpha({ 'a':2, 'b':3}))
print(isDictKeysAllAlpha({ 1:2, 'b':3}))

# create popByValue function which gets a dictionary
# and a value as a parameter-
# pop all items with the value.
# *etgar: returns these poped items (k,v) in a list
def popByValue(_d, _v):
    result = []
    for k,v in list(_d.items()):
        if v == _v:
            _d.pop(k)
            result.append((k, v))
    return result

def popByValue_simple(_d, _v):
    for k in list(_d.keys()):
        if _d[ k ] == _v:
            _d.pop( k )

print(popByValue({ 'a':2, 'b':3, 'c':2}, 2))
_d = { 'a':2, 'b':1, 'c':2}
popByValue_simple(_d, 2)
print(_d)

# create newDict function which gets two lis1 and list2
# as parameter- returns a dictionary which consist of
# the two lists: list1 will be the keys and list2 will
# be the values. if the lists are not in the same length
# or list1 contains duplication returns None
def newDict(_l1_keys, _l2_values):
    if len(_l1_keys) != len(_l2_values):
        return None
    if len(_l1_keys) != len(set(_l1_keys)):
        return None
    _d = { }
    for i in range(len(_l1_keys)):
        _d[ _l1_keys[ i ] ] = _l2_values[ i ]
    return _d

def newDict_short(_l1_keys, _l2_values):
    if len(_l1_keys) != len(_l2_values) or len(_l1_keys) != len(set(_l1_keys)):
        return None
    return { _l1_keys[i] : _l2_values[i] for i in range(len(_l1_keys)) }


print(newDict(['aa', 'b', 'c'], [4,5,6]))
print(newDict_short(['aa', 'b', 'c'], [4,5,6]))