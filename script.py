import sys
import json
import os

with open(sys.argv[1], 'rb') as f:
    contents = f.read()
bytes = list(contents)

#Step 1: get the file count (every byte till 1st 0A)
file_num = 0
temp_storage = ""
temp_index = 0

for byte in bytes:
    temp_index += 1
    temp_storage += chr(byte)
    if byte == 10:
        file_num = int(temp_storage)
        break

bytes = bytes[temp_index:]

temp_storage = ""
temp_index = 0

#Step 2: parse file name, start, length until file runs out

file_list = []
file_object = {}
index = 0
deletes = 0
for byte in bytes:
    deletes += 1
    if byte == 124:
        #|
        if temp_index == 0:
            file_object["name"] = temp_storage
            temp_storage = ""
            temp_index += 1
        elif temp_index == 1:
            file_object["start"] = int(temp_storage)
            temp_storage = ""
            temp_index += 1
        else:
            raise Exception('overflow temp_index, aborting.')
            
    elif byte == 10:
        #/n
        file_object["end"] = int(temp_storage)
        temp_storage = ""
        file_list.append(file_object)
        file_object = {}
        index += 1
        temp_index = 0
        if index >= file_num:
            break
    else:
        temp_storage += chr(byte)

bytes = bytes[deletes:]

#step 3: correct offset and extract

index = 0
temp_index = 0
temp_storage = []
next_start = file_list[0]["end"]

for byte in bytes:
    index += 1
    if index < next_start:
        temp_storage.append(byte)
    else:
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

print("All file exported.")
