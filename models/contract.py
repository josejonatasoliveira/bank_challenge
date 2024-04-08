from pydantic import BaseModel

class Contract(BaseModel):
    id: int
    debt: float