def dot(u, v):
    return sum(ui * vi for ui, vi in zip(u, v))

def subtract(u, v):
    return [ui - vi for ui, vi in zip(u, v)]

def cross(u, v):
    return [
        u[1] * v[2] - u[2] * v[1],
        -(u[0] * v[2] - u[2] * v[0]),
        u[0] * v[1] - u[1] * v[0]
    ]

def are_collinear(p1, p2, p3):
    u = subtract(p2, p1)
    v = subtract(p3, p1)
    cross_product = cross(u, v)
    return abs(cross_product[0]) < 1e-9 and abs(cross_product[1]) < 1e-9 and abs(cross_product[2]) < 1e-9


def closest_point_on_plane(p0, p1, p2, p3):
    if len(set(tuple(p) for p in [p0, p1, p2, p3])) != 4 or are_collinear(p1, p2, p3):
        return 0
    
    normal = cross(subtract(p2, p1), subtract(p3, p1))
    t = dot(normal, subtract(p1, p0)) / dot(normal, normal)
    
    closest_point = [p0i + t * normali for p0i, normali in zip(p0, normal)]
    return closest_point





print(closest_point_on_plane([98.998, -11.621, 2.612], [-55.431, -75.053, -6.379], [-47.893, 4.822, 90.054], [-364.48899999999986, -3349.928, -3960.132]))