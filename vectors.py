## template for the programming assignment 3


class Matrix:
    def __init__(self, matrix:list) -> None:
        #Expected list of list [[a,b,c],[d,e,f]]
        self.matrix = matrix
        
        #Take the amount of rows
        self.row_len = len(self.matrix)

        #If the matrix is not empty, get the first row and count the columns
        if self.row_len > 0:
            self.col_len = len(self.matrix[0])
        else:
            #If the matrix has no rows, then we have no columns
            self.col_len = 0
        
        #The expected size of our matrix R x C, e.g. 3 x 3 = 9
        self.expected_size = self.row_len * self.col_len


    def __mul__(self, B): #Override the multiplication of the Matrix class, this is when A x B
        
        #B has to be an instance of Matrix for this to work
        if(isinstance(B, Matrix) == False):
            return 0

        #Check if the sizes of our matricies add up
        valid_A = self.validateMatrix()
        valid_B = B.validateMatrix()
        
        if(valid_A and valid_B):
            #If either Matricies are empty, return 0
            if self.row_len == 0 or B.row_len == 0:
                return 0
            #If the rows of A are not the same as the columns of B, we return 0
            elif self.col_len != B.row_len:
                return 0
            #If the validation is ok, perform multiplication
            AB = self.matrix_multiplication(B)
            return AB

        return 0

    #def __rmul__(self, A): #Override the multiplication, this is when B x A (Reverse)
        #AB = self.matrix_multiplication(A)
        #return AB
    
    def matrix_multiplication(self, B):
        """This function takes as input a matrix 𝐴 of size 𝑛×𝑚 and a 
        matrix 𝐵 of size 𝑚×𝑟, and it returns the matrix 𝐴𝐵. If the matrix dimensions do not 
        match or if the matrices are otherwise invalid, it should return the number 0. Matrices 
        are given as two-dimensional lists.
        """
        #Create a return Matrix
        AB = []

        for row in range(self.row_len):
            #List for a new row to be inserted into our new result Matrix
            new_row = []
            for col in range(B.col_len):
                #Variable that adds up the matrix multiplication
                coefficient = 0
                for B_col in range(B.row_len):
                    coefficient += (self.matrix[row][B_col] * B.matrix[B_col][col])
                new_row.append(coefficient)
            AB.append(new_row)
        return AB
    
    def validateMatrix(self) -> bool:
        """Matrix is expected to be an instance of matrix, to access the properties."""
        #Return the size of the matrix, by counting the columns in each row
        size = self.get_size()

        #Only returns None for data types that are not int or float
        if size == None:
            return False

        #Check if our expected size is equals to the actual size of the matrix
        if size != self.expected_size:
            return False

        #If all checks are okay, we return True
        return True
    
    def get_size(self):
        """Returns the size of the matrix, R x C"""
        size = 0
        for row in self.matrix:
            for column in row:
                #If we detect a non int or float in our matrix, return None
                if isinstance(column, int) or isinstance(column, float):
                    size += 1
                else:
                    return None
        return size
            
        

def squareroot(x):
   return x**0.5


## matrix multiplication:

# This function takes as input a matrix A of size n×m and a matrix B 
# of size m×r, and it returns the matrix AB. If the matrix dimensions 
# do not match or if the matrices are otherwise invalid, it should 
# return the number 0.
def matrix_multiplication(A, B):
    # Check that the matrices can be multiplied
    m_A = Matrix(A)
    m_B = Matrix(B)
    AB = m_A * m_B
    return AB

# This function takes as input two lists that represent vectors vector1 and vector2 
# of R^3 and returns the dot product of vector1 and vector2.
def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Both vectors must be of the same length.")
    if len(vector1) < 1:
        raise ValueError("Vectors must have at least one coordinate.")
    
    return 0


# This function takes as input two lists that represent vectors vector1 and vector2 
# of R^3 and returns the cross product of vector1 and vector2.
def cross_product(vector1, vector2):
    if len(vector1) != 3 or len(vector2) != 3:
        raise ValueError("Both vectors must be of length 3.")
    
    return [0, 0, 0]

# This function takes as input two vectors vector and direction 
# of R^3 and returns the projection of vector on direction. Vectors are given as lists. 
# If direction=0, then the function should return the number 0. 
def projection(vector,direction):
   
   return vector
   
      
# This function takes as input four distinct points A,B,C,D. 
# The three points B,C,D define a plane Π, in that there is a unique 
# plane Π that has all three points, as long as they are not on the same line. 
# The function returns the point P on Π that is the closest to A. Like vectors, 
# points are given as lists of their coordinates. If B,C,D are on the same line, 
# if A,B,C,D are not distinct, or if the input is not valid for another reason, 
# then the function should return 0.
def closest_point_on_plane(A,B,C,D):
   
   return A

A = [[1,2,3],
    [4,5,6],
    [7,8,9]]

B = [[9,8,7],
    [6,5,4],
    [3,2,1]]

B_mod = [[9,8],
        [7,6],
        [5,4]]
B_1 = [[9],[8],[7]]
print(matrix_multiplication(A,B_1)) #Expected [[30, 24, 18], [84, 69, 54], [138, 114, 90]]
