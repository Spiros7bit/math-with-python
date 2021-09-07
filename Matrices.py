'''
A module to deal with mathematical objects matrices  
'''

#Class for matrices
class Matrix:
    '''
        result = [[0]*other.columns]*self.rows (1a method to initialize a list) create bugs.
        This peculiar functioning is because Python uses shallow lists which we will try to understand.
        In method 1a, Python doesn’t create 5 integer objects but creates only one integer object and 
        all the indices of the array result point to the same int object. 

        arr = [[0 for i in range(cols)] for j in range(rows)] this method doesn't create bugs
    '''
    #initializer
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len( matrix )
        self.columns = len( matrix[0] )
    
    def __str__(self):
        st = "\n"+"-"*40
        for i in range( self.rows ):
            st += "\n"
            for j in range( self.columns ):
                st += "\t"+str( self.matrix[i][j] )+""

        return st
    
    def __len__(self):
        return 
    
    def __add__(self, other):
        #addition can be only with same rows and columns matrices
        if isinstance(other, Matrix) and (self.rows == other.rows) and (self.columns == other.columns):
            matrix = [[0 for i in range(other.columns)] for j in range(self.rows)]

            #add every [i][j] element with the same [i][j] of other matrix
            for i in range(self.rows):
                for j in range(self.columns):
                    matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return Matrix(matrix)
    
    def __sub__(self, other):
        if isinstance(other, Matrix) and (self.rows == other.rows) and (self.columns == other.columns):
            matrix = [[0 for i in range(other.columns)] for j in range(self.rows)]

            for i in range(self.rows):
                for j in range(self.columns):
                    matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
            return Matrix(matrix)
    
    def __mul__(self, other):
        #multiplication with a number (graded product)
        if isinstance(other, int):
            matrix = [[0 for i in range(other.columns)] for j in range(self.rows)]

            for i in range(self.rows):
                for j in range(self.columns):
                    matrix[i][j] = other * int( self.matrix[i][j] ) 

        #multiplication with a vector\matrix (dot product)
        elif isinstance(other, Matrix) and ((self.rows == other.columns) or (self.columns == other.rows)):
            matrix = [[0 for i in range(other.columns)] for j in range(self.rows)]
            
            for i in range(0, self.rows):
                for j in range(0, other.columns):
                    for k in range(0, len(self.matrix[0]) ):
                        matrix[i][j] = matrix[i][j] + self.matrix[i][k] * other.matrix[k][j]
                    
        return Matrix(matrix)
    def __rmul__(self, other):
        #method __mul__ throw error, for that i call __mul__ from __rmul__ and workd :D
        return self.__mul__(other)