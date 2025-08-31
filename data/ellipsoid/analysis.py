import os
import numpy as np
from tqdm import tqdm

def get_all_files(base_dir):
    files = []
    for split in ['train', 'valid']:
        split_dir = os.path.join(base_dir, split)
        for f in os.listdir(split_dir):
            if f.endswith('.npz'):
                files.append(os.path.join(split_dir, f))
    return files

if __name__ == "__main__":
    base_dir = os.path.join(os.path.dirname(__file__), "src", "simple")
    files = get_all_files(base_dir)
    min_xyz = np.array([np.inf, np.inf, np.inf])
    max_xyz = np.array([-np.inf, -np.inf, -np.inf])
    min_rgb = np.array([np.inf, np.inf, np.inf])
    max_rgb = np.array([-np.inf, -np.inf, -np.inf])
    for file in tqdm(files, desc="Analyzing ellipsoid files"):
        arr = np.load(file)['arr_0']
        xyz = arr[:, :3]
        rgb = arr[:, 3:6]
        min_xyz = np.minimum(min_xyz, xyz.min(axis=0))
        max_xyz = np.maximum(max_xyz, xyz.max(axis=0))
        min_rgb = np.minimum(min_rgb, rgb.min(axis=0))
        max_rgb = np.maximum(max_rgb, rgb.max(axis=0))
    print(f"Position min: {min_xyz}, max: {max_xyz}")
    print(f"Color min: {min_rgb}, max: {max_rgb}")
