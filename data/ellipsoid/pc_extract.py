from datasets import Dataset, DatasetDict
from comgeo.core.mesh.triangle_mesh import TriangleMesh3D

from tqdm import tqdm

import os
import numpy as np


if __name__ == "__main__":

    repo_id = "kohido/ellipsoid_1024pts"

    raw_data_dir = os.path.join(os.getcwd(), 'ellipsoid_simple')
    save_pc_dir = os.path.join(os.getcwd(), 'ellipsoid_1024pts')
    os.makedirs(save_pc_dir, exist_ok=True)

    train_indices = range(50000)
    val_indices = range(50000, 60000)

    data_dct = {}

    for split, indices in zip(['train', 'val'], [train_indices, val_indices]):
        data = []
        for i in tqdm(indices):
            obj_path = os.path.join(raw_data_dir, f'ellipsoid_{i:05d}.obj')
            mesh = TriangleMesh3D.from_file_path(obj_path)
            pointcloud = mesh.point_cloud_sampling(1024)
            points = np.array([[v.x, v.y, v.z] for v in pointcloud])
            np.save(os.path.join(save_pc_dir, f'ellipsoid_{i:05d}.npy'), points)