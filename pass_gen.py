import random
import sys

chars = []

for ascii in range(33,127):
    chars.append(chr(ascii))

def gen_pass(length):
    password = []
    for i in range(length):
        password.append(random.choice(chars))
    return "".join(password)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        length = int(sys.argv[1])
        print("Generated the following password : " + gen_pass(length))
    else:
        print("Enter a length")
