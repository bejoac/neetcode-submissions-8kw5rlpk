class TimeMap:

    def __init__(self):
        self.__store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.__store:
            self.__store[key].append([value, timestamp])
        else:
            self.__store[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.__store:
            key_values = self.__store[key]
        else:
            return ""
        
        L, R = 0, len(key_values) - 1
        
        # Check if it makes sense to search
        if key_values[L][1] > timestamp:
            return ""
        if key_values[R][1] <= timestamp:
            return key_values[R][0]
            
        closest_distance = float("-inf") # Prob smarter to use min allowed value

        while L <= R:
            M = L + (R - L) // 2
            if timestamp < key_values[M][1]:
                R = M - 1
            elif key_values[M][1] == timestamp:
                return key_values[M][0]
            elif timestamp > key_values[M][1]:
                L = M + 1
            
            distance = key_values[M][1] - timestamp
            if (distance > closest_distance and distance < 0):
                closest_distance = distance
                index_closest_distance = M
                
        return key_values[index_closest_distance][0]