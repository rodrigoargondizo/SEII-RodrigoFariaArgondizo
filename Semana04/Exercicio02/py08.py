def hello_func():
    # pass
    # print('Hello function!')
    return 'Hello function.'

print(hello_func())
print(hello_func().upper())
print(hello_func)

def hey_func(greeting, name='You'):
    return '{} Function.'.format(greeting)

print(hey_func('Hey'))
print(hey_func('Hey', name='Gabriel'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name='Gabriel', age=22)

courses = ['Math', 'Art']
info = {'name': 'Gabriel', 'age': 22}
student_info(courses, info)
student_info(*courses, **info)

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Returns True for leap years and False for everything else"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Returns the number of days in a month"""
    if not 1 <= month <= 12:
        return 'Invalid month'

    if(month == 2) and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2017, 2))
print(days_in_month(2020, 2))
print(days_in_month(2018, 3))