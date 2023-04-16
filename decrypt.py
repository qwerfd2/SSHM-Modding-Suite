import os

char_map = [{"as": "a", "bs": "p"}, {"as": "A", "bs": "P"}, {"as": "b", "bs": "s"}, {"as": "B", "bs": "S"}, {"as": "1", "bs": " "},
            {"as": "c", "bs": "r"}, {"as": "C", "bs": "R"}, {"as": "d", "bs": "u"}, {"as": "D", "bs": "U"}, {"as": "2", "bs": "#"},
            {"as": "e", "bs": "t"}, {"as": "E", "bs": "T"}, {"as": "f", "bs": "w"}, {"as": "F", "bs": "W"}, {"as": "3", "bs": "\""},
            {"as": "g", "bs": "v"}, {"as": "G", "bs": "V"}, {"as": "h", "bs": "y"}, {"as": "H", "bs": "Y"}, {"as": "4", "bs": "%"},
            {"as": "i", "bs": "x"}, {"as": "I", "bs": "X"}, {"as": "j", "bs": "{"}, {"as": "J", "bs": "["}, {"as": "5", "bs": "$"},
            {"as": "k", "bs": "z"}, {"as": "K", "bs": "Z"}, {"as": "l", "bs": "}"}, {"as": "L", "bs": "]"}, {"as": "6", "bs": "'"},
            {"as": "m", "bs": "|"}, {"as": "M", "bs": "\\"}, {"as": "n", "bs": "\x7f"}, {"as": "N", "bs": "_"}, {"as": "7", "bs": "&"},
            {"as": "o", "bs": "~"}, {"as": "O", "bs": "^"}, {"as": "q", "bs": "`"}, {"as": "Q", "bs": "@"}{"as": "8", "bs": ")"},
            {"as": "9", "bs": "("}, {"as": "0", "bs": "!"}, {"as": ",", "bs": "="}, {"as": "-", "bs": "<"}, {"as": ":", "bs": "+"},
            {"as": ".", "bs": "?"},  {"as": "/", "bs": ">"}]

folder_path = os.path.dirname(os.path.abspath(__file__))
save_file = "player.prf"
file_path = os.path.join(folder_path, save_file)

if not os.path.exists(file_path):
    print("Error: 'player.prf' does not exist under the same directory.")
    quit()

print("Decrypting 'player.prf' to 'plaintext.prf'...")

char_dict = {}
for mapping in char_map:
    char_dict[mapping["as"]] = mapping["bs"]
    char_dict[mapping["bs"]] = mapping["as"]

with open(save_file, "rb") as input_file:
    text = input_file.read()

output_data = bytearray()
for byte in text:
    char = chr(byte)
    if char in char_dict:
        output_data.append(ord(char_dict[char]))
    else:
        output_data.append(byte)
        print("Warning: Undocumented character", byte, ", left as-is.")

with open("plaintext.prf", "w") as output_file:
    print("Decryption complete. Writing file...")
    output_file.write(output_data.decode("latin-1"))

print("'plaintext.prf' saved to the same directory.")
