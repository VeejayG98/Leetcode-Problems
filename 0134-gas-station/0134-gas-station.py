class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        current_gas = 0
        total_gas = 0
        start_index = 0
        for i in range(len(cost)):
            if current_gas < 0:
                current_gas = 0
                start_index = i
            current_gas = current_gas + gas[i] - cost[i]
            total_gas = total_gas + gas[i] - cost[i]

        return start_index if total_gas >= 0 else -1
