import requests
import string
import random
from random import randint

def id_genertaor(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def phone_genertaor(size=6,phones=string.digits):
    return ''.join(random.choice(phones) for _ in range(size))    

for i in range(30000000000000):
    
    randSize = randint(8, 20)
    raName = randint(8,12)
    name = id_genertaor(raName)
    emil = id_genertaor(randSize)
    passw = id_genertaor(randSize)
    phone = phone_genertaor(randSize)
    # send Request attack
    file = {
# Data
#EX
#       'name' : (None, name),
    }
    print('-----------------------------')
    print("Request number: {}".format(i))
    print("Name:{}".format(name))
    response = requests.post('URL', files=file,headers = {'User-agent': 'your bot 0.1'}),
    print(response)