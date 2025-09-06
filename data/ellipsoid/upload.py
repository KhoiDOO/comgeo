from datasets import Dataset, DatasetDict
from comgeo.functional.mesh.io.load import load_mesh
from comgeo.core.mesh.triangle_mesh import TriangleMesh3D

from tqdm import tqdm

import os
import numpy as np


if __name__ == "__main__":

    repo_id = "kohido/ellipsoid_1024pts"

    raw_data_dir = os.path.join(os.getcwd(), 'ellipsoid_simple')

    train_indices = range(50000)
    val_indices = range(50000, 60000)

    data_dct = {}

    for split, indices in zip(['train', 'val'], [train_indices, val_indices]):
        data = []
        for i in tqdm(indices):
            obj_path = os.path.join(raw_data_dir, f'ellipsoid_{i:05d}.obj')
            mesh = TriangleMesh3D.from_file_path(obj_path)
            pointcloud = mesh.point_cloud_sampling(1024)
            points = [[v.x, v.y, v.z] for v in pointcloud]
            data.append({'points': points})

        data_dct[split] = Dataset.from_list(data)
    
    dataset = DatasetDict(data_dct)
    # dataset.save_to_disk(os.path.join(os.getcwd(), 'ellipsoid_1024pts'))

    # Verify
    # print(f"Number of training samples: {len(dataset['train'])}")
    # print(f"Number of validation samples: {len(dataset['val'])}")
    # sample = np.array(dataset['train'][0]['points'])
    # print(f"Example data point shape (first training sample):\n{sample.shape}, type: {type(sample)}")

    dataset.push_to_hub(repo_id)