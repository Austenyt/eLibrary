from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    age: int
    company: str


payload = User(id=1, name='Ivan', age=0, company='asasa')
print(payload.id)
