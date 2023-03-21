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