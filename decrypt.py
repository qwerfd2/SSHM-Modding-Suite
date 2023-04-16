import os

char_map = [{"as": "a", "bs": "p"}, {"as": "A", "bs": "P"}, {"as": "1", "bs": " "}, {"as": "b", "bs": "s"}, {"as": "B", "bs": "S"}, {"as": "2", "bs": "#"},
            {"as": "c", "bs": "r"}, {"as": "C", "bs": "R"}, {"as": "3", "bs": "\""}, {"as": "d", "bs": "u"}, {"as": "D", "bs": "U"}, {"as": "4", "bs": "%"},
            {"as": "e", "bs": "t"}, {"as": "E", "bs": "T"}, {"as": "5", "bs": "$"}, {"as": "f", "bs": "w"}, {"as": "F", "bs": "W"}, {"as": "6", "bs": "'"},
            {"as": "g", "bs": "v"}, {"as": "G", "bs": "V"}, {"as": "7", "bs": "&"}, {"as": "h", "bs": "y"}, {"as": "H", "bs": "Y"}, {"as": "8", "bs": ")"},
            {"as": "i", "bs": "x"}, {"as": "I", "bs": "X"}, {"as": "9", "bs": "("}, {"as": "j", "bs": "{"}, {"as": "J", "bs": "["}, {"as": "0", "bs": "!"},
            {"as": "k", "bs": "z"}, {"as": "K", "bs": "Z"}, {"as": ",", "bs": "="}, {"as": "l", "bs": "}"}, {"as": "L", "bs": "]"}, {"as": "-", "bs": "<"},
            {"as": "m", "bs": "|"}, {"as": "M", "bs": "\\"},{"as": ":", "bs": "+"}, {"as": "n", "bs": "\x7f"}, {"as": "N", "bs": "_"}, {"as": ".", "bs": "?"}, 
            {"as": "o", "bs": "~"}, {"as": "O", "bs": "^"}, {"as": "/", "bs": ">"}, {"as": "q", "bs": "`"}, {"as": "Q", "bs": "@"}]

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

with open(save_file, "r") as input_file:
    text = input_file.read()

new_text = ""
for char in text:
    new_char = char_dict.get(char, char)
    new_text += new_char

#remove this line to encrypt player.prf, it should work (havn't test it, as of 4/23 game can read plaintext prf)
new_text = new_text[1:-2]

with open("plaintext.prf", "w") as output_file:
    print("Decryption complete. Writing file...")
    output_file.write(new_text)

print("'plaintext.prf' saved to the same directory.")
