import json

json_data = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_data)
print("Name:", data['name'])
print("Age:", data['age'])
print("City:", data['city'])
