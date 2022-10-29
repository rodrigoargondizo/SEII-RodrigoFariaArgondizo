message = 'Hello World'

print(message)
print(len(message))
print(message[0:5])
print(message[:5])
print(message[6:])
print(message.lower())
print(message.upper())
print(message.count('Hello'))
print(message.find('World'))
print(message.find('Word'))
print(message.replace('World', 'Universe'))

greeting = 'Hello'
name = 'Rodrigo'

print(greeting + ', ' + name)
print('{}, {}. Welcome!'.format(greeting, name))
print(f'{greeting}. {name.upper()}. Welcome!')

print(dir(name))
print(help(str.lower))