import os
import tarfile
import tempfile

class VirtualFileSystem:
    def __init__(self, tar_path):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.mount_point = self.temp_dir.name 
        self.file_owners = {}
        self._extract_tar(tar_path)
    
    def _extract_tar(self, tar_path):
        with tarfile.open(tar_path, 'r') as tar:
            tar.extractall(self.mount_point)
            for member in tar.getmembers():
                if member.isfile():
                    self.file_owners[member.name] = "root"

    def list_dir(self, current_dir):
        current_dir = current_dir.lstrip("/")
        path = os.path.join(self.mount_point, current_dir) 
        
        if os.path.isdir(path):
            return os.listdir(path)
        else:
            raise NotADirectoryError(f"{path} is not a directory")


    def change_dir(self, current_dir, new_dir):
        current_dir = current_dir.lstrip("/")
        new_dir = new_dir.lstrip("/")

        new_path = os.path.normpath(os.path.join(self.mount_point, current_dir, new_dir))
        
        if os.path.isdir(new_path):
            return os.path.relpath(new_path, self.mount_point)
        else:
            raise FileNotFoundError(f"Directory {new_dir} not found")

    def change_owner(self, file, new_owner):
        file = file.lstrip("/")


        file_path = os.path.normpath(os.path.join(self.mount_point, file))
        
        if os.path.isfile(file_path):
            self.file_owners[os.path.relpath(file_path, self.mount_point)] = new_owner
            print(f"Changed owner of '{file}' to '{new_owner}'")
        else:
            raise FileNotFoundError(f"File '{file}' not found")

    def get_owner(self, file):
        file = file.lstrip("/")
        file_path = os.path.normpath(file)
        return self.file_owners.get(file_path, "Unknown")

