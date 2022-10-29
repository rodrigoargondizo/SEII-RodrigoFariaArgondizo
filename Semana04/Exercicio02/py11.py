f = open('test.txt', 'r')
print(f.name, f.mode)
f.close()

with open('test.txt', 'r') as f:
    # print(f.read())
    # print(f.readlines())
    # print(f.readline())
    # print(f.readline())

    # for line in f:
    #     print(line, end='')

    # print(f.read(10))
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f.tell())
    f.seek(0)

    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)

print(f.closed)

with open('test2.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R')

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

with open('Screenshot.jpg', 'rb') as rf:
    with open('Screenshot_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while(len(rf_chunk) > 0):
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)



