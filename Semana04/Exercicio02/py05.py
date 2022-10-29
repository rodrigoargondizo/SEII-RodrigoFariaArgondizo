student = {'name': 'Rodrigo', 'age': 22, 'courses': ['SEMB2', 'RICA1']}

print(student)
print(student['name'])
print(student.get('name'))
print(student.get('phone'))
print(student.get('phone', 'Not Found'))

student['phone'] = '12345'
student['name'] = 'Rod'
print(student)

student.update({'name': 'Rodrigo', 'phone': '1234'})
print(student)

del student['age']
print(student.pop('phone'))
print(student)

print(len(student), student.keys(), student.values(), student.items())

for key, value in student.items():
    print(key, value)