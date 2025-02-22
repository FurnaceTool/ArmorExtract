import os
import shutil
import yaml, json

class Utils:
    @staticmethod
    def load_yaml(file_path: str, default = None) -> dict:
        if not os.path.exists(file_path):
            return default
        with open(file_path, "r") as f:
            return yaml.safe_load(f)
    
    @staticmethod
    def load_json(file_path: str, default = None) -> dict:
        if not os.path.exists(file_path):
            return default
        with open(file_path, "r") as f:
            return json.load(f)
    
    @staticmethod
    def save_json(file_path: str, data: dict) -> None:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def clear_old_convert(*paths):
        for path in paths:
            shutil.rmtree(path, ignore_errors=True) if os.path.exists(path) else None