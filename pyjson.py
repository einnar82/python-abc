# parsing json
import json

userJson = '{"first_name": "john", "last_name": "doe", "age": 30}'

user = json.loads(userJson)
# parsing dictionaries from json
print(user['first_name'])
print(user)

car = {'make': 'ford', 'model': 'mustang', 'year': 1970}

carJson = json.dumps(car)

print(carJson)
