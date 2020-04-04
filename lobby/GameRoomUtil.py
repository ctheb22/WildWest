import random

def generateCode(stringLength=5):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(letters) for i in range(stringLength))