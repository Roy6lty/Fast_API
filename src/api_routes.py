
from src import app, Path, Query,Body
from pydantic import  Field, BaseModel, validator
import string
import json

from typing import Optional
"""
Gey: Request information from a server
Put: Modify or change an existing information
Post: Insert/summit/Create information into a server/database
Delete:  Delete from server
"""


class Students(BaseModel):
    #every time an abject is created it is initialized
    id : int  #unique field id
    name:str
    Age:int
    School: str
    level: int
    MaritalStatus:str

    @validator('name')
    @classmethod
    def name_valid(cls, value):
        if any(p in value for p in string.punctuation):
            raise ValueError('Username must not include punctuation')
        else:
            return value

    @validator('Age')
    @classmethod
    def age_valid(cls, value):
        if value < 0:
            raise ValueError('Age cannot be less than zero')
        else:
            return value
    
    @validator('level')
    @classmethod
    def level_valid(cls, value):
        if value < 100:
            raise ValueError('level cannot be less than 100')
        else:
            return value

class StudentUpdate(BaseModel):
    name:Optional[str] = None
    School:Optional[str] = None
    MaritalStatus:Optional[str] = None
    level: Optional[int] = None
    Age: Optional[int] = None
    sex:Optional[str] =  None

        


students = """{
       "id": [ {
            "id" : 1,
            "name":"John",
            "Age": 24,
            "sex": "male",
            "School":"Futa",
            "level":300,
            "MaritalStatus": "single"
        },
        {
            "id" : 2,
            "name":"Sarah",
            "Age": 20,
            "sex": "female",
            "School":"uniben",
            "level":100,
            "MaritalStatus": "single"

        },
        {
            "id" : 3,
            "name":"Amaka",
            "Age": 23,
            "sex": "female",
            "School":"Futpre",
            "level":500,
            "MaritalStatus": "married"
        },
        { 
            "id" : 4,
            "name":"Samason",
            "Age": 19,
            "sex": "male",
            "School":"Futa",
            "level":200,
            "MaritalStatus": "Single"
        },
        {
            "id" : 5,
            "name":"Fola",
            "Age": 23,
            "sex": "female",
            "School":"uniport",
            "level":500,
            "MaritalStatus": "Single"
        }
    ]
}
"""



json_users =[Students(**u) for u in json.loads(students)['id']]
for i in range(5):
    if  json_users[i].id == 5:
           print( json_users[i].name)


@app.get('/')
def index():
    return {"name":"First Data"} #returning data in json

@app.get('/get-students/{student_id}')
def get_student(student_id:int = Path(description='Student Identification Number',gt=0, lt=20))-> Students: #request student_id of type int
    for id in range(len(json_users)):
        if  json_users[id].id == student_id:
            return json_users[id]
    return {"No match found"}
        

@app.get('/get-by-name/')
async def get_by_name(student_name:Optional[str] = Query(...,min_length=2, max_length=20)):
    for student_id in range(len(json_users)):
        if json_users[student_id].name == student_name:
            return json_users[student_id]
    return 'Data not Found'

@app.post('/create_student/{student_id}')
def create_student(student_id:int, student:Students) :
    for i in range(len(json_users)):
        if json_users[i].id == student_id:
            return 'Error: Student already in database'

    json_users.append(student)   
    return json_users[student_id - 1]

@app.put('/update_students/{student_id}')
async def update_students(student_id:int, student:StudentUpdate):
    if student_id not in students:
        return 'Error: Student not in database'
    
    
    if student.name != None:
        students[student_id]['name'] = student.name
        
    if student.MaritalStatus != None:
        students[student_id]['MaritalStatus'] = student.MaritalStatus
    
    if student.sex != None:
        students[student_id]['sex'] = student.sex
    
     
    if student.School != None:
        students[student_id]['School'] = student.School
    
     
    if student.level != None:
        students[student_id]['level'] = student.level
    
     
    if student.Age != None:
        students[student_id]['Age'] = student.Age
    
    return students[student_id]


# Query parameters

@app.get('/multiple_query/')
def get_object(item_no:list[str] = Query(['Apple','Orange'])):

    results = {'item1': 'Apple'},{'item2': 'pineapple'},{'item3': 'Orange'}

    return results


@app.get('/multiple_params/')
def get_mulitiple_objects(
               item_no: int = Query(gt=0, lt=20, title= 'Item Number', description='The item number'),
               item_name:str = Query(None,max_length=30),
               item_complete = Body(...)
               ):

    results = {'item1': 'Apple','item2': 'pineapple','item3': 'Orange'}
    results.update({('item'+str(item_no)):item_name})

    return results



 

