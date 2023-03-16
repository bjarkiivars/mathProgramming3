## template for the programming assignment 3


def squareroot(x):
   return x**0.5


## matrix multiplication:

# This function takes as input a matrix A of size n×m and a matrix B 
# of size m×r, and it returns the matrix AB. If the matrix dimensions 
# do not match or if the matrices are otherwise invalid, it should 
# return the number 0.
def matrix_multiplication(A, B):
  # Check that the matrices can be multiplied

  return 0

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



