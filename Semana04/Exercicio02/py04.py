# LISTS:
courses = ['History', 'Math', 'Physics']

print(courses)
print(len(courses))
print(courses[0])
print(courses[-1])
print(courses[0:2])
print(courses[:2])
print(courses[1:])

courses.append('Portuguese')
courses.insert(0, 'Art')
print(courses)

courses_2 = ['Education']
courses.extend(courses_2)
print(courses)

courses.remove('Math')
print(courses.pop())
print(courses)

courses.reverse()
print(courses)

nums = [1, 3, 5, 2, 4]

courses.sort()
nums.sort(reverse=True)

print(courses, nums)
print(sorted(nums))

print(min(nums), max(nums))

print(courses.index('Physics'))
print('English' in courses)

for index, item in enumerate(courses, start=1):
    print(index, item)

print(', '.join(courses))
print(', '.join(courses).split(', '))

# TUPLES:
tuple_1 = ('History', 'Math', 'Physics')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'

# SETS:
cs_courses = {'History', 'Math', 'Physics', 'Math'}
print(cs_courses)
print('Math' in cs_courses)

art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))



