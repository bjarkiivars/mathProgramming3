# This function takes as input four distinct points A,B,C,D.
# The three points B,C,D define a plane Π, in that there is a unique
# plane Π that has all three points, as long as they are not on the same line.
# The function returns the point P on Π that is the closest to A. Like vectors,
# points are given as lists of their coordinates. If B,C,D are on the same line,
# if A,B,C,D are not distinct, or if the input is not valid for another reason,
# then the function should return 0.
def closest_point_on_plane(A,B,C,D):
    #First, let's check if B, C and D are collinear (on the same line)
    collinear = are_collinear(B, C, D)
   
    #If so, return 0
    if collinear:
        return 0
    
    #To find the normal N, we use the formula: (B-C) x (D-B)
    sub_B_C = sub(B,C)
    sub_D_B = sub(D, B)
    normal = cross_product(sub_B_C, sub_D_B)

    lower_half = dot_product(normal, normal)

    t = dot_product(sub(A, D), normal) / lower_half


    # Calculate the components of the closest point using the formula A - t * N
    closest_point = [A[i] - t * normal[i] for i in range(3)]
    return closest_point

def are_collinear(B, C, D):
    """Helper function that checks if the points B, C and D are collinear (meaning they are on the same line.)"""
    
    #Let's start by getting the u and v vector's, we subtract C - B and D - B
    u = sub(C, B)
    v = sub(D, B)

    #By getting the cross product of u and v, we get a vector that is perpendicular to both u and v
    cross_result = cross_product(u, v)

    #Lastly, we check if the u and v are collinear, 
    #To do this we check wether the cross product of u and v is the zero vector.
    return cross_result == [0,0,0]

def sub(v, w):
    """Helper function that subtracts each component of two vectors v and w"""
    #Again utilize the zip() function to make tuples of v and w iteratable objects
    #Subtract each tuple pair and return a vector list of the subtracted result
    return [vi - wi for vi, wi in zip(v, w)]


# This function takes as input two lists that represent vectors vector1 and vector2
# of R^3 and returns the cross product of vector1 and vector2.
def cross_product(vector1, vector2):
    if len(vector1) != 3 or len(vector2) != 3:
        raise ValueError("Both vectors must be of length 3.")
    
    #Check if either vector is a zero vector:
    if vector1 == [0,0,0] or vector2 == [0,0,0]:
        return 0

    #Using the formula:
    # (Y1 * Z2) - (Y2 * Z1)
    #-((X1 * Z2) - (X2 * Z1))
    # (X1 * Y2) - (X2 * Y1)
    x_component = (vector1[1] * vector2[2]) - (vector2[1] * vector1[2])
    y_component = -((vector1[0] * vector2[2]) - (vector2[0] * vector1[2]))
    z_component = (vector1[0] * vector2[1]) - (vector2[0] * vector1[1])

    #Uf the resulting vector is a zero vector [0,0,0], then the two are parallel
    return [x_component, y_component, z_component]

# This function takes as input two lists that represent vectors vector1 and vector2 
# of R^3 and returns the dot product of vector1 and vector2.
def dot_product(vector1, vector2):
    """Returns the dot product of two vector lists, returns 0 if either one is of value 0"""
    #To improve time complexity, we store the length values in variables so as to not reapet the iteration:
    len_v1 = len(vector1)
    len_v2 = len(vector2)
    #If either vectors are non-R^3, return 0
    if len_v1 != len_v2:
        raise ValueError("Both vectors must be of the same length.")
    #Check if the vectors contain no components
    if len_v1 < 1:
        raise ValueError("Vectors must have at least one coordinate.")

    #Rule 3. V * 0 == 0 * v = 0
    #So if either vector is 0, we return 0 as a result.
    if vector1 == [0, 0, 0] or vector2 ==  [0, 0, 0]:
        return 0
    
    #Lastly we sum each component in both vectors together to form a dot sum.
    dot_sum = 0
    for i in range(len_v1):
        dot_sum += vector1[i] * vector2[i]
    return dot_sum

# This function takes as input two vectors vector and direction
# of R^3 and returns the projection of vector on direction. Vectors are given as lists.

# If direction=0, then the function should return the number 0.
def projection(vector,direction):
    if direction == [0,0,0]:
        return 0
    #To find the magnitude we start by getting the dot product of the vector and the direction
    v_d = dot_product(vector, direction)
    #Then we divide that by the dot product of direction * direction, so ||d||^2
    d_squared = dot_product(direction, direction)
    
    #finally we divide the v * d by ||d||^2 to get the magnitude
    magnitude = v_d / d_squared

    #Lastly to get the projection we multiply the magnitude * direction for each direction component
    v_projection = [magnitude * direction[component] for component in range(len(direction))]
    return v_projection


