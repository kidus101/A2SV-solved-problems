class DataStream:

    def __init__(self, value: int, k: int):
        self.val = value
        self.k = k
        self.stream = deque()
        self.dict_counter= defaultdict(int)
        self.count = 0
        
        

    def consec(self, num: int) -> bool:
        
        self.stream.append(num)
        self.dict_counter[num] += 1
        self.count += 1
        
        if self.count > self.k:
            val =self.stream.popleft()
            self.dict_counter[val] -= 1
            self.count -= 1
            
        if self.count < self.k:
            return False
        
        return self.dict_counter[self.val] == self.k
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)