import unittest

from models.contract import Contract
from controllers.contract_controller import ContractController


class Test_ContractController(unittest.TestCase):
    def test_contracts(self):
        contracts = [
            Contract(1, 1),
            Contract(2, 2),
            Contract(3, 3),
            Contract(4, 4),
            Contract(5, 5)
        ]
        renegotiated = [3]
        top_n = 3

        actual_open_contracts = ContractController().get_top_N_open_contracts(contracts, renegotiated, top_n)

        expected_open_contracts = [5, 4, 2]
        self.assertEqual(expected_open_contracts, actual_open_contracts)

    def test_contracts(self):
        contracts = [
            Contract(1, 200),
            Contract(2, 600),
            Contract(3, 900),
            Contract(4, 100),
            Contract(5, 500),
            Contract(6, 5),
            Contract(7, 10),
        ]
        renegotiated = [3, 5]
        top_n = 4

        actual_open_contracts = ContractController().get_top_N_open_contracts(contracts, renegotiated, top_n)

        expected_open_contracts = [2, 1, 4, 7]
        self.assertEqual(expected_open_contracts, actual_open_contracts)

    def test_contracts_top_n_bigger_than_list(self):
        contracts = [
            Contract(1, 200),
            Contract(2, 600),
            Contract(3, 900),
            Contract(4, 100),
            Contract(5, 500),
            Contract(6, 5),
            Contract(7, 10),
        ]
        renegotiated = [3, 5]
        top_n = 20

        actual_open_contracts = ContractController().get_top_N_open_contracts(contracts, renegotiated, top_n)

        expected_open_contracts = [2, 1, 4, 7, 6]
        self.assertEqual(expected_open_contracts, actual_open_contracts)


if __name__ == '__main__':
    unittest.main()
