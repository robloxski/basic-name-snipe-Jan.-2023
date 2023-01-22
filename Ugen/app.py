import requests
import json
import string
import random 

NOU = int(input("number of usernames to generate: "))
NOL = int(input("number of letters: "))

def Generate():
    username = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(NOL))
    api = f"https://auth.roblox.com/v1/usernames/validate?request.username={username}&request.birthday=1981-08-08"
    r = requests.get(api).json()
    if r['code'] != 0:
        print(username, 'invalid')
    else:
        print(username, 'valid')

for i in range(NOU):
    Generate()