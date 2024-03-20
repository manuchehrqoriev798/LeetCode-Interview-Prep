why defaultdict is better here. rather than just dictionary. 
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        rows = len(mat)
        cols = len(mat[0])
        

        for i in range(rows):
            for j in range(cols):
                d[i - j].append(mat[i][j])
        

        for key in d:
            d[key].sort()
        

        for i in range(rows):
            for j in range(cols):
                mat[i][j] = d[i - j].pop(0)
        
        return mat




class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = {}
        rows = len(mat)
        cols = len(mat[0])

        # Populate the dictionary with elements from the matrix based on their diagonal indices
        for i in range(rows):
            for j in range(cols):
                diagonal_index = i - j
                if diagonal_index not in d:
                    d[diagonal_index] = []
                d[diagonal_index].append(mat[i][j])

        # Sort the elements in each diagonal group
        for key in d:
            d[key].sort()

        # Reconstruct the matrix with sorted diagonal elements
        for i in range(rows):
            for j in range(cols):
                diagonal_index = i - j
                mat[i][j] = d[diagonal_index].pop(0)

        return mat
