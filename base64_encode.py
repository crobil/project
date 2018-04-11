from base64 import b64encode, b64decode

def to_base_64(string):
    return b64encode(string).replace("=", '')

def from_base_64(string):
    return b64decode(string + "==")
