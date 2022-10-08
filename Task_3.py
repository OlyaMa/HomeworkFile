import os

file1_path = os.path.join(os.getcwd(), '1.txt')
file2_path = os.path.join(os.getcwd(), '2.txt')
file3_path = os.path.join(os.getcwd(), '3.txt')
file4_path = os.path.join(os.getcwd(), '4.txt')

with open(file1_path, 'r', encoding='utf-8') as f1:
    file1 = f1.readlines()
with open(file2_path, 'r', encoding='utf-8') as f2:
    file2 = f2.readlines()
with open(file3_path, 'r', encoding='utf-8') as f3:
    file3 = f3.readlines()
with open(file4_path, 'w', encoding='utf8') as f4:
    if len(file1) < len(file2) and len(file1) < len(file3):
        f4.write('1.txt' + '\n')
        f4.write(str(len(file1)) + '\n')
        f4.writelines(file1)
        f4.write('\n')
    elif len(file2) < len(file1) and len(file2) < len(file3):
        f4.write('2.txt' + '\n')
        f4.write(str(len(file2)) + '\n')
        f4.writelines(file2)
        f4.write('\n')
    elif len(file3) < len(file1) and len(file3) < len(file2):
        f4.write('3.txt' + '\n')
        f4.write(str(len(file3)) + '\n')
        f4.writelines(file3)
        f4.write('\n')

    if len(file2) < len(file1) < len(file3) or len(file2) > len(file1) > len(file3):
        f4.write('1.txt' + '\n')
        f4.write(str(len(file1)) + '\n')
        f4.writelines(file1)
        f4.write('\n')
    elif len(file3) < len(file2) < len(file1) or len(file3) > len(file2) > len(file1):
        f4.write('2.txt' + '\n')
        f4.write(str(len(file2)) + '\n')
        f4.writelines(file2)
        f4.write('\n')
    elif len(file2) < len(file3) < len(file1) or len(file2) > len(file3) > len(file1):
        f4.write('3.txt' + '\n')
        f4.write(str(len(file3)) + '\n')
        f4.writelines(file3)
        f4.write('\n')

    if len(file1) > len(file2) and len(file1) > len(file3):
        f4.write('1.txt' + '\n')
        f4.write(str(len(file1)) + '\n')
        f4.writelines(file1)
        f4.write('\n')
    elif len(file2) > len(file1) and len(file2) > len(file3):
        f4.write('2.txt' + '\n')
        f4.write(str(len(file2)) + '\n')
        f4.writelines(file2)
        f4.write('\n')
    elif len(file3) > len(file1) and len(file3) > len(file2):
        f4.write('3.txt' + '\n')
        f4.write(str(len(file3)) + '\n')
        f4.writelines(file3)
        f4.write('\n')