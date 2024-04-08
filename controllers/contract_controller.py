from typing import List
from abc import ABC

from models.contract import Contract

class ContractController(ABC):
    def get_top_N_open_contracts(self, op_contracts: List[Contract],
                                 rg_contracts: List[int], top_n: int) -> List[int]:
        
        contracts_no_rg = [c for c in op_contracts if c.id not in rg_contracts]
        sorted_contracts = sorted(contracts_no_rg, key=lambda contract: -contract.debt)
        return [c.id for c in sorted_contracts][:top_n]