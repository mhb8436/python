import json

data = {
    "name": "John",
    "age": 30,
    "is_student": False,
    "course": ["Math", "Science"],
    "address" : {
        "street": "123 Main st",
        "city" : "New York"
    }
}

with open('../data.json', 'w') as file:
    json.dump(data, file, indent=4)



