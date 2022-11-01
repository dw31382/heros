import random

table = open("ascii_table.txt", "r")

print(table.read())

ascii = [chr(i) for i in range(32, 127)]
hex = [hex(i) for i in range(0x20, 0x7e)]

ascii_hex = dict(zip(ascii, hex))

# put this in a loop

def random_ascii():
    key = random.choice(list(ascii_hex.keys()))
    user_input = input("What is the hex value of {}? ".format(key))
    if user_input == ascii_hex[key]:
        print("Correct!")
    else:
        print("Incorrect!")

# do that quiz again but ask about the ascii value instead of the hex value

def random_hex():
    key = random.choice(list(ascii_hex.keys()))
    user_input = input("What is the ascii value of {}? ".format(ascii_hex[key]))
    if user_input == key:
        print("Correct!")
    else:
        print("Incorrect!")

# set the quiz to ask a random mix of ascii and hex questions

def quiz():
    while True:
        if random.choice([True, False]):
            random_ascii()
        else:
            random_hex()

quiz()