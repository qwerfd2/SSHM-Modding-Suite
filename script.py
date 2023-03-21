import sys
import os

if len(sys.argv) < 3:
    print("Command line invalid.\nUsage: python", sys.argv[0], "pack.pak output_dir")
    quit()

file_name = sys.argv[1]
save_path = sys.argv[2]
if file_name[-4:] != '.pak':
    print("Input file name invalid.\nUsage: python", sys.argv[0], "pack.pak output_dir")
    quit()

print("Opening the file.")

with open(file_name, 'rb') as f:
    offset = 0
    print("File opened.\nDetecting number of files.")
    line = f.readline()
    file_num = int(line.decode().strip())
    offset += len(line)
    print(str(file_num),"file(s) detected.\nAcquiring file metadata.")
    file_list = []
    for i in range(file_num):
        line = f.readline()
        offset += len(line)
        file_info = line.decode().strip().split('|')
        path, start, length = file_info
        file_object = {'name': path, 'start': int(start), 'end': int(length)}
        file_list.append(file_object)

print("All file metadata acquired.\nExtracting file(s) to '", save_path, "' directory.")

for file in file_list:
    file_path = os.path.join(save_path, file["name"])
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_name, 'rb') as f:
        f.seek(file['start'] + offset)
        content = f.read(file['end'])
        with open(file_path, 'wb') as out:
            out.write(content)

print("All file(s) exported to '", save_path, "' directory.")
