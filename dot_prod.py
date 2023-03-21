#1. V * W C R^3
    #The resulting vector should be part of R^3
#2. V * W == W * V
    #Doesn't matter if we do V first or second.
#3. V * 0 == 0 * v = 0
    #So if either vector is 0, we return 0 as a result.
#4. v * v = ||v||^2
    #So if we have the same vector twice, the result is the length squared.
#5. (kv) * w == k(v * w) == v * (kw) for all scalar k's

#6. u * (v +- w) == u * v +- u * w 

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
    
    #Here we use list comprehension to return a resulting vector list
    #By creating a zip() => which turns each iterable object into a paired tuple:
    #  V1 = [1,2,3] , V2 = [4,5,6] zip(V1, V2) = (1,4), (2,5), (3,6)
    #This way we can multiply each component pair in the tuple with each other and return the resulting list
    return [v1 * v2 for v1, v2 in zip(vector1, vector2)]
    

print(dot_product([1,2,3], [4,5,6]))