import builtins
print(dir(builtins))

x = 'global x'

def test(z):
    global x
    y = 'local y'
    print(y)
    # print(x)
    # x = 'local x'
    # print(x)
    print(z)

# test()
test('local z')

print(min([5, 1, 4, 2, 3]))

def outer():
    x = 'outer x'

    def inner():
        # nonlocal x
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
print(x)