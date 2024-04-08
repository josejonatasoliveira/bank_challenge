from typing import List
from abc import ABC
import itertools

class OrderController(ABC):

    def in_range(self, dist_max: int, point_a: int, point_b: int) -> bool:
        diff = dist_max - (point_a + point_b)
        return diff
    
    def get_all_approved_requests(self, requests: List[int], n_max: int) -> dict:
        num_requests = range(len(requests))
        
        # Duas requisicoes por viagem
        all_combinations = list(itertools.combinations(num_requests, 2))

        combinations = dict()

        for req_a, req_b in all_combinations:
            diff = self.in_range(n_max, requests[req_a], requests[req_b])
            if diff >= 0: # Esta dentro do intervalo permitido
                combinations[(req_a, req_b)] = diff
            
        return combinations
                
    def combine_orders(self, requests: List[int], n_max: int) -> int:

        approved_req = self.get_all_approved_requests(requests, n_max)
        
        index_combined = set()
        travel_counter = 0
        for (index_a, index_b), dif_n_max in sorted(approved_req.items(), key=lambda dif: dif[1]):
            order_not_combined = index_a not in index_combined and index_b not in index_combined
            if order_not_combined:
                travel_counter += 1
                index_combined.add(index_a)
                index_combined.add(index_b)

        odd_requests = len(requests) % 2
        if odd_requests:
            travel_counter += 1

        return travel_counter