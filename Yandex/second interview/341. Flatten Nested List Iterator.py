class NestedIterator:
    def __init__(self, nestedList):
        self.flatList = []
        self.iterator = 0
        self.flattenList(nestedList)
    
    def flattenList(self, nestedList):
        for ele in nestedList:
            if ele.isInteger():
                self.flatList.append(ele.getInteger())
            else:
                self.flattenList(ele.getList())
    
    def next(self):
        if self.hasNext():
            val = self.flatList[self.iterator]
            self.iterator += 1
            return val
        else:
            return None
    
    def hasNext(self):
        return self.iterator < len(self.flatList)