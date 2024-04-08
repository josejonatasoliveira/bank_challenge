from typing import List
from pydantic import BaseModel

class OrderDTO(BaseModel):
    requests: List[int]
    n_max: int