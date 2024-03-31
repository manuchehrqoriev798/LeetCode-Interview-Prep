class ZigzagIteratorK:

    # int[0] is index of vector of vectors list, int[1] is start of a vector, int[2] is end
    q = []

    # no map needed, if move 'vectors' a class variable
    vectors = []

    def __init__(self, vectors):
        self.vectors = vectors
        for i in range(len(vectors)):
            self.q.append([i, 0, len(vectors[i])])

    def next(self):
        current = self.q.pop(0)

        i = current[0]
        start = current[1]
        end = current[2]

        if start + 1 < end:
            self.q.append([i, start + 1, end])

        return self.vectors[i][start]

    def hasNext(self):
        return len(self.q) != 0

############