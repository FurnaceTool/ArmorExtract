import os
import glob
import shutil
from utils import Utils

class Nexo:
    def __init__(self):
        self.armors_rendering = {}
        self.furnace_data = {"items": {}}
        self.armors = ["HELMET", "CHESTPLATE", "LEGGINGS", "BOOTS"]

    def find_armor_path(self, armor_texture, armor_type):
        base_path = (f'{armor_texture.replace(":", "/textures/")}.png' if ":" in armor_texture else f'minecraft/textures/{armor_texture}.png')
        layer = "layer_2" if "leggings" in armor_type else "layer_1"
        prefix = base_path.split("/")[-1].split("_")[0]
        return f'{os.path.dirname(base_path)}/{prefix}_armor_{layer}.png'

    def get_armor_type(self, material):
        return next((armor for armor in self.armors if armor in material), None)

    def extract(self):
        os.makedirs("output/nexo", exist_ok=True)
        datas = [Utils.load_yaml(file) for file in glob.glob("pack/Nexo/items/**/*.yml", recursive=True)]

        for data in datas:
            for item_data in data.values():
                material = item_data.get("material")
                if not any(armor in material for armor in self.armors): 
                    continue

                textures = [entry for entry in (item_data.get("Pack", {}).get("textures") or [item_data.get("Pack", {}).get("texture")]) if entry]
                model_id = item_data.get("Pack", {}).get("custom_model_data", "")

                for texture in textures:
                    armor_type = self.get_armor_type(material).lower()
                    texture_path = f"{self.find_armor_path(texture, armor_type)}"

                    if not os.path.exists(f"pack/Nexo/pack/assets/{texture_path}"):
                        print(f"Not found file: {texture_path}")
                        continue
                
                    os.makedirs(os.path.dirname(f"output/nexo/textures/models/{texture_path}"), exist_ok=True)
                    shutil.copy(f"pack/Nexo/pack/assets/{texture_path}", f"output/nexo/textures/models/{texture_path}")
                    self.furnace_data["items"].setdefault(f"minecraft:{material}".lower(), {}).setdefault("custom_model_data", {})[model_id] = {
                        "armor_layer": {
                            "type": armor_type,
                            "texture": f"textures/models/{texture_path}",
                            "auto_copy_texture": True
                        }
                    }

        Utils.save_json("output/nexo/furnace.json", self.furnace_data)