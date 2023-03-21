import sys
import json
import os

print("Opening the file.")
with open(sys.argv[1], 'rb') as f:
    print("File opened.")
    print("Detecting number of files.")
    file_num = int(f.readline().decode().strip())
    print(str(file_num),"file(s) detected.")
    file_list = []
    for i in range(file_num):
        file_info = f.readline().decode().strip().split('|')
        path, start, length = file_info
        file_object = {'name': path, 'start': int(start), 'end': int(length)}
        file_list.append(file_object)
    print("All file metadata acquired.")
    contents = f.read()
bytes = list(contents)

temp_storage = ""
temp_index = 0

#step 3: correct offset and extract
print("Extracting file(s) to 'output' directory.")
index = 0
temp_index = 0
temp_storage = []
next_start = file_list[0]["end"]
for byte in bytes:
    index += 1
    temp_storage.append(byte)
    if index >= next_start:
        temp_storage.append(byte)
        filename = "output/"+file_list[temp_index]["name"]
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        newFile = open(filename, "wb")
        fileByteArray = bytearray(temp_storage)
        newFile.write(fileByteArray)
        temp_index += 1
        temp_storage = []
        if temp_index >= file_num:
            break
        next_start = next_start + file_list[temp_index]["end"]

print("All file(s) exported to 'output' directory.")
