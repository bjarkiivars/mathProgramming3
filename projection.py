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

def vector_sum(vector):
    """Helper function designed to return the sum of a given vector."""
    #Create a sum variable
    v_sum = 0

    for component in vector:
        v_sum += component
    
    return v_sum


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
    
    #Here we use list comprehension to return a resulting vector list
    #By creating a zip() => which turns each iterable object into a paired tuple:
    #  V1 = [1,2,3] , V2 = [4,5,6] zip(V1, V2) = (1,4), (2,5), (3,6)
    #This way we can multiply each component pair in the tuple with each other and return the resulting list
    return [v1 * v2 for v1, v2 in zip(vector1, vector2)]


print(projection([1,2,3], [0,0,0]))