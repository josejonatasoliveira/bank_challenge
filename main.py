from typing import Union

from fastapi import FastAPI

from DTO.contract_dto import ContractDTO
from DTO.order_dto import OrderDTO
from controllers.contract_controller import ContractController
from controllers.order_controller import OrderController

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})

@app.get("/")
def index():
    return {"Hello": "World"}

@app.post("/contracts")
def get_n_open_contracts(contract: ContractDTO):
    contract_controller = ContractController()
    
    n_contracts = contract_controller.get_top_N_open_contracts(
        contract.op_contracts,
        contract.rg_contracts,
        contract.top_n
    )
    
    return {"contracts": n_contracts}

@app.post("/orders")
def get_orders_for_travel(orders: OrderDTO):
    order_controller = OrderController()
    
    n_travels = order_controller.combine_orders(
        orders.requests,
        orders.n_max
    )
    
    return {"n_travels": n_travels}