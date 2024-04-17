#!/usr/bin/env python3

import random
import string
import hashlib


def pass_generate(
    chars=string.ascii_lowercase
    + string.ascii_uppercase
    + string.digits
    + string.printable,
    size=int(input("How long password you want to generate? ")),
):
    return "".join(random.choice(chars) for _ in range(size))


def add_plain():
    f = open("passwords-plain.txt", "a")
    f.write(password + "\n")
    f.close()


def add_hashed():
    f = open("passwords-hashed.txt", "a")
    f.write(h.hexdigest() + "\n")
    f.close()


password = pass_generate()

h = hashlib.new("sha256")
h.update(password.encode())

if __name__ == "__main__":
    # size = input(int("How long password you want to generate? "))
    password = pass_generate()
    add_plain()
    add_hashed()
