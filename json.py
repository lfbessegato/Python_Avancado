import json

data = {
	'nome' : 'marcos',
	'idade' : 30,
	'peso' : 85
}

json_str = json.dumps(data)
print(json_str)
print(type(json_str))
data = json.loads(json_str)
print(data)
print(type(data))