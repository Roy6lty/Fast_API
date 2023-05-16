import json

students = """
{
"people": [
    { 
        "name":"john smith",
        "phone": "0703351758",
        "emails": [
            "olowleru@gmail.com","john-smith@work-place.com"
            ],
        "has_lincenced": false
    },
    {
        "name": "jane Doe",
        "phone": "09033520960",
        "emails":null,
        "has_lincense":true
    }

  ]
}

"""
#loading a json string to python object
data = json.loads(students)
for i in data['people']:
    print(i['name'])

for i in data['people']:
    del i['phone']

#converting the json obj(python dict) to string
new_string = json.dumps(data, indent=2, sort_keys = True)
print(new_string)



#Loading json file to pyhton object 

{
    "states":[
        {
            "name":"Alabama",
            "Abbreviation":"AL",
            "area_codes":["205","251","256","334","938"]
        },
        {
            "name":"Arizona",
            "Abbreviation":"AZ",
            "area_codes":["480","520","623","938"]
        },
        {
            "name":"New york",
            "Abbreviation":"NY", 
            "area_codes":["280","678","612","338"]   
        },
        {
            "name":"Califonia",
            "Abbreviation":"Ca",
            "area_codes":["123","456","791","110"]
        }
    ]
}

#Loading json file to pyhton object 

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state['Abbreviation'],state['name'])

for state in data['states']:
    del state['Abbreviation']

#loading to json file

with open('new_states', 'w') as f:
    json.dump(data, f, indent=2)


#students


students = """{
"id": [
        {
            "id" :"1",
            "name":"John",
            "Age": 24,
            "sex": "male",
            "School":"Futa",
            "level":300,
            "maritalStatus": "single"
        },
        {
            "id" : "2",
            "name":"Sarah",
            "Age": 20,
            "sex": "female",
            "School":"uniben",
            "level":100,
            "maritalStatus": "single"

        },
        {
            "id" : "3",
            "name":"Amaka",
            "Age": 23,
            "sex": "female",
            "School":"Futpre",
            "level":500,
            "maritalStatus": "married"
        },
        { 
            "id" : "4",
            "name":"Samason",
            "Age": 19,
            "sex": "male",
            "School":"Futa",
            "level":200,
            "maritalStatus": "Single"
        },
        {
            "id" : "5",
            "name":"Fola",
            "Age": 23,
            "sex": "female",
            "School":"uniport",
            "level":500,
            "maritalStatus": "Single"
        }
    ]
}
"""
student_data = json.loads(students)
print(student_data)

for i in student_data['id']:
    print(i['name'])

test_json = {
    1:{
        "name:":"john",
        "age" : 50,
        "sex": "male"
    },
    2:{
        "name:":"john",
        "age" : 50,
        "sex": "male"
    },
    3:{
        "name:":"john",
        "age" : 50,
        "sex": "male"
    }
}


print(test_json[1]["name"])