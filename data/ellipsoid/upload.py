from huggingface_hub import HfApi

# Initialize the API client
api = HfApi()

# Upload the folder
api.upload_large_folder(
    folder_path="./src/simple",
    repo_id="kohido/ellipsoid-pointclouds",
    repo_type="dataset",
    num_workers=16
)

print("🚀 Successfully uploaded the dataset!")