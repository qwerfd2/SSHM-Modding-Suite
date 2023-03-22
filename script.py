import sys
import os
import traceback

if len(sys.argv) < 3:
    print("Command line variable invalid.\nUsage: python", sys.argv[0], "pack.pak/all output_dir")
    quit()

file_name = sys.argv[1]
save_path = sys.argv[2]
if file_name[-4:] != '.pak' and file_name != 'all':
    print("Input file name invalid. Must end with .pak or be 'all'.\nUsage: python", sys.argv[0], "pack.pak/all output_dir")
    quit()

def extract(file_name):

    print("Opening", file_name, ".")

    try:
        with open(file_name, 'rb') as f:
            offset = 0
            print(file_name, "opened.\nDetecting number of files.")
            line = f.readline()
            num_files = int(line.decode().strip())
            offset += len(line)
            print(str(num_files),"file(s) detected.\nAcquiring file metadata.")
            file_list = []
            for i in range(num_files):
                line = f.readline()
                offset += len(line)
                file_info = line.decode().strip().split('|')
                path, start, length = file_info
                file_object = {'name': path, 'start': int(start), 'length': int(length)}
                file_list.append(file_object)

            print("All file metadata acquired.\nExtracting file(s) to '", save_path, "' directory.")

            for file in file_list:
                file_path = os.path.join(save_path, file["name"])
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                f.seek(file['start'] + offset)
                content = f.read(file['length'])
                with open(file_path, 'wb') as out:
                    out.write(content)

            print("All file(s) exported to '", save_path, "' directory.\n")

    except FileNotFoundError as e:
        print(file_name, "not found. Make sure it is in the same folder as the script itself. Traceback:\n", traceback.format_exc())
        quit()
    except ValueError as e:
        print(file_name, "is deformed - is it a Secret Society Hidden Mystery .pak file? Traceback:\n", traceback.format_exc())
        quit()
    except:
        print("An unknown error occurred at the step above. Please go to https://github.com/qwerfd2/SSHM-Pak-Extractor and let the developer know. Traceback:\n", traceback.format_exc())
        quit()

if file_name == 'all':
    for file in os.listdir(os.path.dirname(__file__)):
        if file.endswith(".pak"):
            extract(file)
else:
    extract(file_name)
