## template for the programming assignment 3

#I decided to implement both the Matrix solution and Vector solutions as classes

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
        """Takes two Matricies and we use triple nested for loops to iterate
        in a way that allows us to multiply e.g. the first row and each column in A
        with Matrix B each row column in index 0, then we iterate back to the first index in A
        in row 0, and iterate through the first column but second row in B, and iterate each row in B
        This way we're performing:
            |(A), (B), (C)|  |(A2), B2, C2|
        A = | D,   E,   F| * |(D2), E2, F2| = (A * A2) + (B * D2) + (C * G2)... and so on
            | G,   H,   I|   |(G2), H2, I2|
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
            
class Vector:
    def __init__(self, vector = []):
        """Takes a vector paragram in R3 [x, y, z]"""
        if isinstance(vector, list):
            raise ValueError('The vector parameter has to be of type list.')
        self.vector = vector
        #How many items we have in our vector
        self.size = len(vector)
        #What the length property of our axis is
        self.len = 0

    def __mul__(self, w):
        """Performs matrix multiplication"""
        #Checks if the W parameter is of the instance Vector
        if(isinstance(w, Vector) == False):
            raise ValueError("Both vectors have to be of the instance Vector")
        
        #Check if both vectors are the same size
        if w.size != self.size:
            raise ValueError('Both matricies have to have equal length for multiplication')

        
        #Checks if both vectors contain only numbers (int / float)
        self.validateEachAxis()
        w.validateEachAxis()

        #Will raise error if it's not ok, no need for a return value
        self.validateVectors(w)

        WV = self.dot_product(w)
        return WV
        
    def dot_product(self, w):
        """Performs the dot product vector multiplication"""
        VW = []
        for axis in range(self.size):
            mult_axis = 0
            #Multiply each axis, x1 * x2, y1 * y2 and turns it into a list
            mult_axis = self.vector[axis] * w.vector[axis]
            VW.append(mult_axis)
        return VW

    def validateVectors(self, w):
        """Checks if the vectors are valid."""
        if self.size != w.size:
            raise ValueError("Both vectors must be of the same length.")
        if self.size < 1:
            raise ValueError("Vectors must have at least one coordinate.")
        return
    
    def validateEachAxis(self):
        """Validates each axis: x, y, z to check if they're numbers."""
        for axis in self.vector:
            if(isinstance(axis, int)):
                return
            elif(isinstance(axis, float)):
                return
            raise ValueError("Each axis must be an integer or a float.")

    def __vector_length_recur(self, index):
        """Recursive method that calculates the length of the vector: 
        ||V|| by doing square root on each axis squared,
        returns the length of the vector"""
        #Base case, we have finished calculating all the items, we are not out of bounds
        if index == self.size:
            return 0 #So we can have the call stack add the numbers up without breaking
        #Get the squared number = power of 2
        squared = self.vector[index] * self.vector[index]
        sq_rt = 0.5
        #Do a square root on the squared number
        result = squared ** sq_rt
        #Return both the result and continue the recursion
        return result + self.__vector_length_recur(index+1)
        

    def length(self):
        """Calculates the length of the vector = ||V||"""
        self.len = self.__vector_length_recur(0)

    def divide_vector(self, number):
        """Take a number parameter to divide with each axis in the vector"""
        result = []
        for index in range(self.size):
            result.append(self.vector[index] / number)
        return result

    def vector_sum(self, vector, index):
        """Takes a parameter vector and index, sums up the numbers in recursion"""
        #Base case, if we are out of bounds
        if index == self.size:
            return 0 #0 for callstack addition
        #Add the numbers in the call stack and make a method call again to repeat recursion
        return vector[index] + self.vector_sum(vector, index+1)

    def projection(self, d):
        """projection(v,d): This function takes as input two vectors 𝑣 and 𝑑 of ℝ3and returns the 
        projection of 𝑣 on 𝑑. Vectors are given as lists. If 𝑑 =0⃗ , then the function should return 
        the number 0.  """
        #Let's write cases:

        #v and d can not be equal to 0
        if self.size == 0 or d.size == 0:
            return 0

        #formula is proj(d)(v) = ((v dot d) / ||d|||^2) dot d
        #First find the dot product of v * d
        v_dot_d = self.dot_product(d)

        #Get the sum of the v * d dot product
        sum1 = self.vector_sum(v_dot_d, 0)

        #Now to find ||d||^2, we will do this by doing d * d
        d_dot_d = d.dot_product(d)

        #Get the second sum of the dot product of d * d
        sum2 = self.vector_sum(d_dot_d, 0)

        #Divide the summation of the dot products:
        divide_sums = sum1 / sum2 

        #Finally multiply the divide_sums with each item in Vector d:
        #Create a new list for the projection results of divide_sums * d
        projection_result = []
        for axis in d.vector:
            #Multiply each item in d with the divide_sums result
            projection_result.append(divide_sums * axis)
        
        #Finally return the result
        return projection_result
    
    def cross(self, w):
        """
        This is all under the assumption we are working with Euclidean space R3.
        We use the formula provided by the DMA Eighth Ed. for vector cross products.
        """
        cross_result = []

        #Let's define each axis in both Vectors:
        #X1:
        X1 = self.vector[0]
        Y1 = self.vector[1]
        Z1 = self.vector[2]
        #X2:
        X2 = w.vector[0]
        Y2 = w.vector[1]
        Z2 = w.vector[2]

        #Let's create the result from our formula 
        x_axis = (Y1 * Z2) - (Y2 * Z1)
        y_axis = -((X1 * Z2) - (X2 * Z1))
        z_axis = (X1 * Y2) - (X2 * Y1)

        #Finally append the result in to our result list
        cross_result.append(x_axis)
        cross_result.append(y_axis)
        cross_result.append(z_axis)

        return cross_result

    def subtract(self, V2):
        """Performs vector subtraction of each axis, x1-x2, y1-y2, z1-z2"""
        #For readability: Let's make self.vector = V1
        V1 = self.vector
        

        #The zip() function creates a tuple of items with the same index,
        #So we use that to take indexes of both vectors and put them in a tuple:
        zipped = zip(V1, V2.vector)

        #Create a list to return the results
        subtract_result = []

        #Iterate the tuple, subtract each pair and append the result
        for V1i, V2i in zipped: 
            subtract_result.append(V1i - V2i)

        return subtract_result

    def are_collinear(self, B, C, D):
        """A function that checks if the given points are collinear (Meaning they lie on the same line)"""
        
        #Let's start by getting the u and v vector's, we subtract C - B and D - B
        u = C.subtract(B)
        v = D.subtract(B)

        #By getting the cross product of u and v, we get a vector that is perpendicular to both u and v
        cross_product = Vector(u).cross(Vector(v))

        #Lastly, we check if the u and v are collinear, 
        #To do this we check wether the cross product of u and v is the zero vector.
        #Using the absolute value function to get the absolute value of each component (axis)
        #Then check wether each component (axis) is less than 1e-9,
        #1e-9 is a small tolerance value used to account for floating point calculations, 
        #although it's not exact, because we can't expect it to be exactly 0.
        #Lastly we are doing equality checks on each component, if all are less than 1e-9, 
        #We return True, else we return False is any component is greater.
        return abs(cross_product[0]) < 1e-9 and abs(cross_product[1]) and abs(cross_product[2]) < 1e-9
    
    def closest_point_on_plane(self, A, B, C, D):
        """Takes 4 Vector class parameters, checks if they are collinear and if not,
            returns their closest point on the plane."""
        #Start by checking if the points B, C and D are collinear:
        collinear = self.are_collinear(B, C, D)

        if collinear:
            return 0

        #To find the normal N, we use the formula: (B-C) x (D-B)
        #One is a regular list, the other is an instance of Vector to make use of the methods.
        normal = Vector((B.subtract(C))).cross(Vector(D.subtract(B)))
        n = Vector(normal)
        #Next to find our t, we use the following formula:
       
        #     n dot (B - A)
        #   ----------------- <- Division
        #        n dot n
        
        
        upper_half = n.dot_product(Vector(B.subtract(A)))
        lower_half = n.dot_product(n)
        t = sum(upper_half) / sum(lower_half)

        #Create our resulting list, which we will fill with our closes point
        closest_point = []

        #Here we populate the closest point, by using the following:
        # Ax + t * Nx = x axis,
        # Ay + t * Ny = y axis,
        # Az + t * Nz = z axis
        for i in range(A.size):
            axis = A.vector[i] + t * n.vector[i]
            closest_point.append(axis)
        
        return closest_point




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
    v = Vector(vector1)
    w = Vector(vector2)
    VW = v * w
    return VW


# This function takes as input two lists that represent vectors vector1 and vector2 
# of R^3 and returns the cross product of vector1 and vector2.
def cross_product(vector1, vector2):
    v1 = Vector(vector1)
    v2 = Vector(vector2)
    if v1.size != 3 or v2.size != 3:
        raise ValueError("Both vectors must be of length 3.")
    
    return v1.cross(v2)

# This function takes as input two vectors vector and direction 
# of R^3 and returns the projection of vector on direction. Vectors are given as lists. 
# If direction=0, then the function should return the number 0. 
def projection(vector,direction):
   v = Vector(vector)
   d = Vector(direction)

   return v.projection(d)
   
      
# This function takes as input four distinct points A,B,C,D. 
# The three points B,C,D define a plane Π, in that there is a unique 
# plane Π that has all three points, as long as they are not on the same line. 
# The function returns the point P on Π that is the closest to A. Like vectors, 
# points are given as lists of their coordinates. If B,C,D are on the same line, 
# if A,B,C,D are not distinct, or if the input is not valid for another reason, 
# then the function should return 0.
def closest_point_on_plane(A,B,C,D):
   closest_point = Vector()
   A1 = Vector(A)
   B1 = Vector(B)
   C1 = Vector(C)
   D1 = Vector(D)
   return closest_point.closest_point_on_plane(A1, B1, C1, D1)




#print(closest_point_on_plane([98.998, -11.621, 2.612], [-55.431, -75.053, -6.379], [-47.893, 4.822, 90.054], [-364.48899999999986, -3349.928, -3960.132]))