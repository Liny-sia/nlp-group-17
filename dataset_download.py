import kagglehub

# Download latest version

path = kagglehub.dataset_download(
    "mehmetisik/amazon-review",
    output_dir="/Users/liny/nlp-group-17/dataset", # Change the path
)

print("Path to dataset files:", path)