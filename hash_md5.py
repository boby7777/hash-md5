import hashlib
import sys

def md5_hash(string):
    md5_hasher = hashlib.md5()
    md5_hasher.update(string.encode('utf-8'))
    hashed_string = md5_hasher.hexdigest()
    return hashed_string

# Check if the input string is provided as a command-line argument
if len(sys.argv) > 1:
    input_string = sys.argv[1]
else:
    input_string = input("Enter the input string: ")

hashed_string = md5_hash(input_string)
print("Input string:", input_string)
print("MD5 hash:", hashed_string)
