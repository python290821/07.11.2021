
# id, fname, lname, address, mobile_no

class Person:
    pass

def create_person(id, fname, lname, address, mobile_no):
    new_person = Person()
    new_person.__dict__['id'] = id # or: new_person.id = id
    new_person.fname = fname
    new_person.lname = lname
    new_person.address = address
    new_person.mobile_no = mobile_no
    return new_person

danny = create_person(200, 'danny', 'cohen', 'tel aviv levontin 30', '05026353265')
'''
danny = Person()
danny.id = 200 # danny.__dict__['id'] = 200
danny.__dict__['fname'] = 'danny'
danny.__dict__['lname'] = 'cohen'
danny.__dict__['address'] = 'tel aviv levontin 30'
danny.__dict__['mobile_no'] = '05026353265'
'''

