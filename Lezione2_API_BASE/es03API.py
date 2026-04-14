from pydantic import BaseModel

class User(BaseModel):
    username:str
    password:str
    patrimonio:float = 0

user = User(username="federico", password="roda")

print(user)
print(user.model_dump())
print(user.model_dump_json())
