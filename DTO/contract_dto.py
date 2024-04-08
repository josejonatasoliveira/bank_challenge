from pydantic import BaseModel
from typing import List

from models.contract import Contract

class ContractDTO(BaseModel):
    op_contracts: List[Contract]
    rg_contracts: List[int]
    top_n: int
    