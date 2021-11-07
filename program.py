
#koko = { 'name': 'koko', 'breed: 'pincher' }

class Dog:
    pass

#rexy = { 'name': 'Rexi', 'height': 1.2, 'breed': 'wolf' }
rexy = Dog()
rexy.__dict__['name'] = 'Rexi'
rexy.__dict__['height'] = 1.2
rexy.__dict__['breed'] = 'wolf'
print(rexy.__dict__)
humi = Dog()
humi.__dict__['android_version'] = 12.1
print(humi.__dict__)
