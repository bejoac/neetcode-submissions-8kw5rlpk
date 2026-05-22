class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        num_stations = len(gas)
        start_candidates = []

        for i in range(num_stations):
            if gas[i] >= cost[i]:
                start_candidates.append(i)

        for start_index in start_candidates.copy():
            tmp_gas = gas.copy()
            tmp_cost = cost.copy()
            tmp_gas = tmp_gas + gas[0:start_index]
            tmp_cost = tmp_cost + cost[0:start_index]
            gas_tank = 0
            i = start_index

            while i < len(tmp_cost):
                gas_tank = gas_tank + tmp_gas[i]
                if gas_tank < tmp_cost[i]:
                    start_candidates.remove(start_index)
                    break
                gas_tank = gas_tank - tmp_cost[i]
                i = i + 1

        if start_candidates:
            start_index = start_candidates[0]
        else:
            start_index = -1

        return start_index
