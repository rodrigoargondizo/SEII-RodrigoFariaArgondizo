if True:
    print('Condition was true')

language = 'Python'
# language = 'C'
# language = 'Java'

if language == 'Python':
    print('Language is Python')
elif language == 'C':
    print('Language is C')
else:
    print('No match')

user = 'Admin'
logged_in = True

# user = 'Gabriel'
# logged_in = False

if user == 'Admin' or logged_in:
    print('Admin page')
else:
    print('Bad creds')

if not logged_in:
    print('Please log in')
else:
    print('Welcome')

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b, a is b)
print(id(a), id(b))

b = a
print(a is b, id(a) == id(b))

if False or None or 0 or [] or '' or () or {}:
    print('Evaluated to true')
else:
    print('Evaluated to false')