#!/usr/bin/python3

import sys
import hashlib
import binascii
import os


def hash_password(password):
    ''' Hash a password for storing. '''
    # Create the salt, see https://en.wikipedia.org/wiki/Salt_(cryptography)
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    # Calculate the password hash including the salt, 100 000 iterations for security :)
    pwdhash = hashlib.pbkdf2_hmac(
        'sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    # The salt is stored separately. It is used every
    # time we check if user's password matches with the stored one.
    return (salt + pwdhash).decode('ascii')


def main():
    if len(sys.argv) != 2:
        print("Invalid arguments!")
        sys.exit(2)

    password = sys.argv[1]
    print(hash_password(password))


if __name__ == '__main__':
    main()
