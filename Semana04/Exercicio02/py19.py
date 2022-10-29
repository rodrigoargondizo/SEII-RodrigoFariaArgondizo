li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

s_li = sorted(li, reverse=True)
print(li)
print(s_li)

li.sort(reverse=True)
print(li)

tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup)
print(tup)
print(s_tup)

di = {'name': 'Gabriel', 'job': 'programming', 'age': None, 'os': 'Xubuntu'}
s_di = sorted(di)
print(di)
print(s_di)

li = [-6, -5, -4, 1, 2, 3]
print(sorted(li, key=abs))