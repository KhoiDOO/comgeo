import numpy as np
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_ellipsoid_samples(sample_files, out_path=None):
    fig = plt.figure(figsize=(20, 10))
    for i, file in enumerate(sample_files):
        data = np.load(file)['arr_0']
        ax = fig.add_subplot(2, 5, i+1, projection='3d')
        x, y, z = data[:, 0], data[:, 1], data[:, 2]
        rgb = (data[:, 3:6] + 0.5) # convert to [0,1] for matplotlib
        ax.scatter(x, y, z, c=rgb, s=2)
        ax.set_title(os.path.basename(file), fontsize=8)
        ax.set_axis_off()
    plt.tight_layout()
    if out_path:
        plt.savefig(out_path)
    else:
        # Save PDF to same folder as this script
        pdf_path = os.path.join(os.path.dirname(__file__), "ellipsoid_samples.pdf")
        plt.savefig(pdf_path)
    # plt.show()

if __name__ == "__main__":
    # Change these paths as needed
    base_dir = os.path.join(os.path.dirname(__file__), "src", "simple", "train")
    files = sorted([os.path.join(base_dir, f) for f in os.listdir(base_dir) if f.endswith('.npz')])[:10]
    plot_ellipsoid_samples(files)
