# Auto Armor Generator For Furnace
This tool allows you automatically generate armor from itemsadder, nexo,... for furnace.

## How to use
### Local
1. Install Python
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Upload content from ItemsAdder / Nexo / ...
- ItemsAdder: zip `content` folder and `storage` folder with `items_ids_cache.yml`. Rename zip to `Content.zip`
- Nexo: zip `items` folder and `pack` folder with `pack.zip`. Rename zip to `Content.zip`
4. Run script
```bash
python extract.py
```

### Github Action
1. Fork / Import to New Repository
  <p align="center">
    <img src="https://qu.ax/TpVxQ.jpeg" width="400"><br>
  </p>
  
3. Upload content from ItemsAdder / Nexo / ... to download link
- ItemsAdder: zip `content` folder and `storage` folder with `items_ids_cache.yml`. Rename zip to `Content.zip`
- Nexo: 🏗
4. Go to Actions -> Extract Armors -> Run workflow -> Input Download URL -> Run
  <p align="center">
    <img src="https://qu.ax/Fbavc.jpeg" width="400"><br>
  </p>
  
5. Wait for the job to finish and download artifact

### Correct file structure for Content.zip 

``` 
🗃️ Content.zip (For ItemsAdder)
└── 📂 ItemsAdder  
    ├── 📂 contents  
    └── 📂 storage  
        └── 📄 items_ids_cache.yml  
```

``` 
🗃️ Content.zip (For Nexo)
└── 📂 Nexo  
    ├── 📂 items  
    └── 📂 pack  
        └── 📦 pack.zip
```

  <p align="center">
    <img src="https://qu.ax/QVBcz.jpeg" width="400">
    <img src="https://qu.ax/irTsr.jpeg" width="400">
  </p>

### Installation Guide
1. Move `furnace.json` into `generated.zip (for ItemsAdder)` or `pack.zip (for Nexo)` and start the conversion
  <p align="center">
    <img src="https://qu.ax/QCGtH.jpeg" width="400">
    <img src="https://qu.ax/nCUyR.jpeg" width="400">
  </p>
  
2. After conversion, move the `textures` folder into the Bedrock resource pack
  <p align="center">
    <img src="https://qu.ax/aQhRh.jpeg" width="400"><br>
  </p>

4. Complete the setup by following this guide [Install the Pack into Geyser](https://furnacetool.github.io/docs/convert/how_to_convert/#step-3-install-the-pack-into-geyser)
