import tarfile
import os

def create_test_tar(tar_path):
    base_dir = "test_dir"
    os.makedirs(os.path.join(base_dir, "home", "user"), exist_ok=True)
    
    with open(os.path.join(base_dir, "home", "user", "file1.txt"), 'w') as f:
        f.write("Content of file1.txt")
        
    with open(os.path.join(base_dir, "home", "user", "file2.txt"), 'w') as f:
        f.write("Content of file2.txt")
    
    with tarfile.open(tar_path, "w") as tar:
        tar.add(base_dir, arcname=os.path.basename(base_dir))

if __name__ == "__main__":
    create_test_tar("vfs.tar")
