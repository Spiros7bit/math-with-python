'''
A module to deal with mathematical objects matrices  
'''
'''
        result = [[0]*other.columns]*self.rows (1a method to initialize a list) create bugs.
        This peculiar functioning is because Python uses shallow lists which we will try to understand.
        In method 1a, Python doesn’t create 5 integer objects but creates only one integer object and 
        all the indices of the array result point to the same int object. 

        arr = [[0 for i in range(cols)] for j in range(rows)] this method doesn't create bugs
    '''
#Class for matrices
class Matrix:
    
    #initializer
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len( matrix )
        self.columns = len( matrix[0] )
    
    def __str__(self):
        st = "\n"+"-"*60
        for i in range( self.rows ):
            st += "\n"
            for j in range( self.columns ):
                st += "\t\t"+str( round(self.matrix[i][j],2) )+""
        return st

    def __eq__(self, other):
        if isinstance(other, Matrix) and (self.rows == other.rows) and (self.columns == other.columns):
            for i in range(self.rows):
                for j in range(self.columns):
                    if self[i][j] == other[i][j]:
                        return True
            return False
    
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
                        matrix[i][j] = (self.matrix[i][k] * other.matrix[k][j]) + matrix[i][j] 
                    
        return Matrix(matrix)
    def __rmul__(self, other):
        #method __mul__ throw error, for that i call __mul__ from __rmul__ and workd :D
        return self.__mul__(other)

    def len(matrix):
        #This method return a "list" of 2 ints, the rows and the columns of a 2D matrix
        return matrix.rows, matrix.columns

    def swap_rows(self, i, k):
        #This method swap 2 rows of a matrix
        self.matrix[i], self.matrix[k] = self.matrix[k], self.matrix[i]
        
    def multiply_rows(self, i):
        #This method divide an element with its inverse (used in guass jordan elimination)
        factor = 1/self.matrix[i][i]
        for j in range(0, self.columns):
            self.matrix[i][j] = self.matrix[i][j]*factor
            
    
    def add_row_multiple(self, i, k, factor):
        #This method zero the other values of the same column in a matrix (used in guass jordan elimination)
        for j in range(0, self.columns):
            self.matrix[k][j] = self.matrix[k][j]-factor*self.matrix[i][j]

    def g_j_elimination(self):
        '''
            Gauss-Jordan algorithm:
                This algorithm solve square linear systems
        '''
        i = 0 #counter for rows
        j = 0 #counter for columns
        while (i < self.rows) and (j < self.columns):
            k = i #k has the value of i-st row
            while (k < self.rows) and (self.matrix[k][j] != 0):
                
                if k < self.rows:
                    self.multiply_rows(i)
                    for k in range(self.rows):
                        if k != i:
                            self.add_row_multiple(i, k, self.matrix[k][j])
                    i = i+1
                    k = k+1
            j = j+1
        return self
    
