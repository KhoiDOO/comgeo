from ....core.vertex import Vertex, Vertex2D, Vertex3D

def is_ccw_2d(
    v1: Vertex2D, 
    v2: Vertex2D, 
    v3: Vertex2D
) -> bool:
    return (v2.x - v1.x) * (v3.y - v1.y) > (v2.y - v1.y) * (v3.x - v1.x)

def is_ccw_3d(
    v1: Vertex3D, 
    v2: Vertex3D, 
    v3: Vertex3D
) -> bool:
    raise NotImplementedError("is_ccw_3d not implemented")

def is_ccw(
    v1: Vertex | Vertex2D | Vertex3D, 
    v2: Vertex | Vertex2D | Vertex3D, 
    v3: Vertex | Vertex2D | Vertex3D
) -> bool:
    
    # same vertex type only
    assert type(v1) == type(v2) == type(v3), "All vertices must be of the same type"
    
    if isinstance(v1, Vertex2D):
        return is_ccw_2d(v1, v2, v3)
    
    if isinstance(v1, Vertex3D):
        return is_ccw_3d(v1, v2, v3)
    
    raise NotImplementedError("is_ccw not implemented for " + str(type(v1)))