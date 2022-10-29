import os
os.chdir('test')
for f in os.listdir():
    # print(f)
    f_name, f_ext = os.path.splitext(f)
    f_title, f_num = f_name.split(' ')
    new_name = f'{f_num.zfill(2)} - {f_title}{f_ext}'
    os.rename(f, new_name)

