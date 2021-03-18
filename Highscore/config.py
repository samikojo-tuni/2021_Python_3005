#!/usr/bin/python3

import hashlib
import binascii
import sys

# You can add all kind of config values to this file, e.g. CSV separator and file path
PATH = "/home/<tunnus>/cgi-data/scores.csv"
SEP = ";"
MAX = 10

# this dictionary contains users, which are allowed to add new high score values
# Key: user name, Value: password in hashed format
users = {
    "sovellus": "f13931a8d34c0d538b98f7ff34c6302f5f274d5eac87c2af03011794c392a9a710b4a263127ae049384f27513f019fed4826bbbb8bddab7884cc984177ce8e953418f42d7556ffa083d52d835902988fab83b12dda126bfd9a1d3b9500aa1dc8",
    "testi": "eaf587b5dd521226e3138d9b1383f521f848a64e55efc8fd5fe90ebf2b879adf0e508feafe68ca0bf4ec5cf5ab80526b12d00724fe941ddea8a94129fa8c649cb4b54c96e58bb7b2ee3adadf09b872e842e3fa65eb4bc35505341a6c9868100f"
}


def verify_password(user, provided_password):
  # use the global users variable
  global users
  # Verify a stored password against one provided by user
  if user not in users:
    return False

  stored_password = users[user]
  salt = stored_password[:64]
  stored_password = stored_password[64:]
  pwdhash = hashlib.pbkdf2_hmac('sha512',
                                provided_password.encode('utf-8'),
                                salt.encode('ascii'),
                                100000)
  pwdhash = binascii.hexlify(pwdhash).decode('ascii')
  return pwdhash == stored_password


def main():
  if len(sys.argv) != 3:
    print("Invalid arguments!")
    sys.exit(3)

  user = sys.argv[1]
  password = sys.argv[2]
  isValid = verify_password(user, password)
  if isValid:
    print("Oikea salasana")
  else:
    print("Väärä käyttäjätunnus ja/tai salasana!")


if __name__ == '__main__':
  main()
