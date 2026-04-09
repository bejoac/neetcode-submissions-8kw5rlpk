class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.insert(0, val) 

        if not self.min_stack:
            self.min_stack.append(val)
        elif val <= self.min_stack[0]:
            self.min_stack.insert(0, val)
        else:
            self.min_stack.insert(1, val)
        
    def pop(self) -> None:
        val = self.stack[0]
        self.min_stack.remove(val)

        self.stack.pop(0)
        
    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.min_stack[0]
