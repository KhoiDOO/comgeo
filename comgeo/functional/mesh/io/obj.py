def read_obj(file_path: str, verbose: bool = False) -> tuple[list[list[float]], list[list[float]], list[list[int]]]:
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
            if verbose and split[0] == "v":
                print(f"Vertex found: {split[1:]}")
            if split[0] == "v":
                vertices.append([float(coord) for coord in split[1:]])
            # elif split[0] == "vn":
            #     vertices_normal.append([float(coord) for coord in split[1:]])
            elif split[0] == "f":
                faces.append([int(face.split('/')[0]) - 1 for face in split[1:]])

    return vertices, vertices_normal, faces