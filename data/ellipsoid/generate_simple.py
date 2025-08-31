from tqdm import tqdm

import numpy as np
import os
import argparse

np.random.seed(42)

TRAIN_ABC_RANGE = (0.1, 0.4)
VALID_ABC_RANGE = (0.4, 0.5)

N_COLORS = 50
COLORS_PALETTE = np.random.uniform(-0.5, 0.5, (N_COLORS, 3))

RATIO = 0.9
N_REGIONS_TRAIN = round(N_COLORS * RATIO)
N_REGIONS_VALID = N_COLORS - N_REGIONS_TRAIN

TRAIN_PALETTE = COLORS_PALETTE[:N_REGIONS_TRAIN]
VALID_PALETTE = COLORS_PALETTE[N_REGIONS_TRAIN:N_REGIONS_TRAIN + N_REGIONS_VALID]

NUM_CLOUDS = 200000
NUM_POINTS = 4096

VERBOSE = False

def generate_ellipsoid_point_cloud(a, b, c, num_points):
    """
    Generate a point cloud for an ellipsoid centered at the origin with radii a, b, c.
    """
    # Sample points uniformly on the ellipsoid surface
    u = np.random.uniform(0, 2 * np.pi, num_points)
    v = np.random.uniform(0, np.pi, num_points)
    x = a * np.cos(u) * np.sin(v)
    y = b * np.sin(u) * np.sin(v)
    z = c * np.cos(v)
    points = np.stack([x, y, z], axis=1)
    return points

num_clouds = NUM_CLOUDS
num_points = NUM_POINTS
out_dir = os.path.join(os.path.dirname(__file__), "src", "simple")
num_train = round(num_clouds * RATIO)
num_valid = num_clouds - num_train

for split, n_split, palette, a_range, n_regions in zip(
    ['train', 'valid'],
    [num_train, num_valid],
    [TRAIN_PALETTE, VALID_PALETTE],
    [TRAIN_ABC_RANGE, VALID_ABC_RANGE],
    [N_REGIONS_TRAIN, N_REGIONS_VALID]
):
    split_dir = os.path.join(out_dir, split)
    os.makedirs(split_dir, exist_ok=True)
    for i in tqdm(range(n_split), desc=f"Generating {split} ellipsoids"):
        a, b, c = np.random.uniform(a_range[0], a_range[1], 3)
        points = generate_ellipsoid_point_cloud(a, b, c, num_points)
        
        theta = np.random.uniform(0, 2 * np.pi)
        phi = np.random.uniform(0, 2 * np.pi)
        psi = np.random.uniform(0, 2 * np.pi)
        Rz = np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta),  np.cos(theta), 0],
            [0, 0, 1]
        ])
        Ry = np.array([
            [np.cos(phi), 0, np.sin(phi)],
            [0, 1, 0],
            [-np.sin(phi), 0, np.cos(phi)]
        ])
        Rx = np.array([
            [1, 0, 0],
            [0, np.cos(psi), -np.sin(psi)],
            [0, np.sin(psi),  np.cos(psi)]
        ])
        R = Rz @ Ry @ Rx
        points_rot = points @ R.T
        
        # Shift points so all coordinates are in [-0.5, 0.5]
        min_xyz = points_rot.min(axis=0)
        max_xyz = points_rot.max(axis=0)
        shift = (min_xyz + max_xyz) / 2
        points_shifted = points_rot - shift
        points_shifted = np.clip(points_shifted, -0.5, 0.5)
        
        # Divide points into n_regions by their polar angle v with random region sizes
        v = np.arccos(points_shifted[:,2] / np.linalg.norm(points_shifted, axis=1))
        if n_regions > 1:
            thresholds = np.sort(np.random.uniform(0, np.pi, n_regions-1))
            thresholds = np.concatenate(([0], thresholds, [np.pi]))
            region_ids = np.zeros_like(v, dtype=int)
            for r in range(n_regions):
                region_ids[(v >= thresholds[r]) & (v < thresholds[r+1])] = r
        else:
            region_ids = np.zeros_like(v, dtype=int)
        colors = palette[region_ids]
        points_colored = np.hstack([points_shifted, colors])
        np.savez_compressed(os.path.join(split_dir, f"ellipsoid_{i}_a{a:.2f}_b{b:.2f}_c{c:.2f}.npz"), points_colored)
        # np.save(os.path.join(split_dir, f"ellipsoid_{i}_a{a:.2f}_b{b:.2f}_c{c:.2f}.npy"), points_colored)
        if VERBOSE:
            print(f"[{split}] Saved ellipsoid point cloud with radii (a={a:.2f}, b={b:.2f}, c={c:.2f}) to ellipsoid_{i}_a{a:.2f}_b{b:.2f}_c{c:.2f}.npy in {split_dir}")
