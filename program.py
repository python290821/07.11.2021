
# id, fname, lname, address, mobile_no

class Person:
    pass

danny = Person()
danny.id = 200 # danny.__dict__['id'] = 200
danny.__dict__['fname'] = 'danny'
danny.__dict__['lname'] = 'cohen'
danny.__dict__['address'] = 'tel aviv levontin 30'
danny.__dict__['mobile_no'] = '05026353265'
print(danny.id) # danny.__dict__['id']

ronni = Person()
ronni.id = 3
ronni.fname = 'ronni'
ronni.lname = 'levi'
ronni.address = 'jerusalem yefet 30'
ronni.mobile_no = '0598287362'
print(ronni.id)
