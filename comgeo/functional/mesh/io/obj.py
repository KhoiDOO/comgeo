def read_obj(file_path: str) -> tuple[list[list[float]], list[list[float]], list[list[int]]]:
    vertices = []
    vertices_normal = []
    faces = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            strip = line.strip()
            strip = ' '.join(strip.split())

            if len(strip) == 0 or strip[0] == "#":
                continue

            split = strip.split()
            
            if split[0] == "v":
                vertices.append([float(coord) for coord in split[1:]])
            elif split[0] == "vn":
                vertices_normal.append([float(coord) for coord in split[1:]])
            elif split[0] == "f":
                faces.append([int(face) - 1 for face in split[1:]])

    return vertices, vertices_normal, faces