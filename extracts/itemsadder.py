import os
import glob
import shutil
from utils.utils import Utils

class ItemsAdder:
    def __init__(self):
        self.armors_rendering = {}
        self.furnace_data = {"items": {}}
        self.item_ids = Utils.load_yaml("ItemsAdder/storage/items_ids_cache.yml")

    def extract(self):
        os.makedirs("output/itemsadder", exist_ok=True)
        datas = [data for file in glob.glob("ItemsAdder/contents/**/*.yml", recursive=True) if (data := Utils.load_yaml(file)) is not None]

        for data in datas:
            self.armors_rendering.update(data.get("armors_rendering", {}))
            namespace = data.get("info", {}).get("namespace", "")
            for equip_id, equip_data in data.get("equipments", {}).items():
                if equip_data.get("type") == "armor" or "layer_1" in equip_data:
                    self.armors_rendering[f"{namespace}:{equip_id}" if namespace else equip_id] = {"layer_1": equip_data.get("layer_1", ""), "layer_2": equip_data.get("layer_2", "")}

        for data in datas:
            namespace = data.get("info", {}).get("namespace", "")
            for item_id, item_data in data.get("items", {}).items():
                armor_type, layer = self.get_armor((item_data.get("specific_properties", {}).get("armor", {}).get("slot") or item_data.get("equipment", {}).get("slot")), item_data)
                if not armor_type: continue
                material = item_data.get("resource", {}).get("material", f"LEATHER_{armor_type}")
                if f"{namespace}:{item_id}" not in self.item_ids.get(material, {}): continue  
                texture_path = self.get_texture(item_data, namespace, layer)
                if not texture_path: continue  
                texture_files = glob.glob(f"ItemsAdder/contents/**/textures/{texture_path}.png", recursive=True)
                if not texture_files: continue  
                output_path = f"output/itemsadder/textures/models/{texture_path}.png"
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                shutil.copy(texture_files[0], output_path)
                self.furnace_data["items"].setdefault(f"minecraft:{material}".lower(), {}).setdefault("custom_model_data", {})[str(self.item_ids[material][f"{namespace}:{item_id}"])] = {
                    "armor_layer": {
                        "type": armor_type.lower(),
                        "texture": f"textures/models/{texture_path}",
                        "auto_copy_texture": False
                    }
                }
        Utils.save_json("output/itemsadder/furnace.json", self.furnace_data)

    def get_armor(self, slot, item_data):
        slot_map = {
            "head": ("HELMET", "layer_1"),
            "chest": ("CHESTPLATE", "layer_1"),
            "legs": ("LEGGINGS", "layer_2"),
            "feet": ("BOOTS", "layer_1")
        }
        if slot:
            result = slot_map.get(slot.lower())
            if result: return result
        for armor in slot_map.values():
            material = item_data.get("resource", {}).get("material") or ""
            if armor[0] in material: return armor
        return None, None

    def get_texture(self, item_data, namespace, layer):
        armor_data = item_data.get("specific_properties", {}).get("armor", {})
        if "custom_armor" in armor_data:
            custom_armor = armor_data["custom_armor"]
            if custom_armor in self.armors_rendering:
                return self.armors_rendering[custom_armor].get(layer)
            
        equipment_id = item_data.get("equipment", {}).get("id")
        if equipment_id:
            if ":" not in equipment_id and namespace:
                equipment_id = f"{namespace}:{equipment_id}"
            if equipment_id in self.armors_rendering:
                return self.armors_rendering[equipment_id].get(layer)
        return item_data.get("resource", {}).get("model_path")
