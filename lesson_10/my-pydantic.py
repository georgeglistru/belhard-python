from pydantic import BaseModel
from typing import Optional
import json

class Employee(BaseModel):
    id : int
    name: str
    age: int
    interests: Optional[list] = []
    salary: float

emps = []
def add_employee(id, name, age, interests, salary):
    emp = Employee(id=id, name=name, age=age, interests=interests, salary=salary)
    emps.append(emp)
    return emp

def get_all():
    res = []
    for emp in emps:
        emp_dict = {'id': emp.id, 'name': emp.name}
        res.append(emp_dict)
    return res

def get_by_index(ind):
    return emps[ind]

emp1 = add_employee(1, "John", 30, ["java", "python"], 1000.0)
emp2 = add_employee(2, "Mark", 40, ["SQL", "C#"], 1500.0)
emp3 = add_employee(3, "Paul", 35, ["AI", "Mongodb"], 2000.5)
emp4 = add_employee(4, "Mary", 25, ["Design", "Word"], 900.0)
emp5 = add_employee(5, "Nancy", 20, ["java", "python"], 1010.0)

print(emp1)
print(emps)
print(get_all())
print(get_by_index(2))

def add_emp_json(id, name, age, interests, salary):
    emp = Employee(id=id, name=name, age=age, interests=interests, salary=salary)
    with open("file.json", "r") as json_file:
        emps_json = json.load(json_file)
        emps_json.append(emp.dict())
        print(emps_json)
    with open("file.json", "w") as json_file:
        json.dump(emps_json, json_file, indent=4)

# add_emp_json(6, "Larry", 55, ["Oracle", "SQL"], 16000.0)

def get_all_from_json():
    with open("file.json", "r") as json_file:
        return json.load(json_file)

print(get_all_from_json())

def get_by_index_from_json(ind):
    with open("file.json", "r") as json_file:
        return json.load(json_file)[ind]

print(get_by_index_from_json(5))