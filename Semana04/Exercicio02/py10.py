import os
from datetime import datetime

print(dir(os))
print(os.getcwd())

os.chdir('/home/gabriel/Desktop')
print(os.getcwd())
os.mkdir('Teste1')
os.makedirs('Teste2/Teste3')
print(os.listdir())

os.rmdir('Teste1')
os.removedirs('Teste2/Teste3')
print(os.listdir())

# os.rename('teste.txt', 'demo.txt')
print(os.listdir())
print(os.stat('demo.txt'))
print(datetime.fromtimestamp(os.stat('demo.txt').st_mtime))

for dirpath, dirname, filenames in os.walk('.'):
    print(dirpath, dirname, filenames)

print(os.environ.get('HOME') + 'test.txt')

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

print(os.path.basename('tmp/test.txt'), os.path.dirname('tmp/test.txt'), os.path.split('tmp/test.txt'), os.path.exists('tmp/test.txt'), os.path.splitext('tmp/test.txt'))