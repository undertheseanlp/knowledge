import pandas as pd

from knowledge import Knowledge


class Location:
    def __init__(self, name=None, level=None):
        self.name = name
        self.level = level

    def set_name(self, name):
        self.name = name

    def set_level(self, level):
        self.level = level

    def to_data(self):
        data = {}
        data["name"] = self.name
        data["level"] = self.level
        return data


df = pd.read_excel('tmp/Danh sách cấp xã.xls')
locations = []
# xã
for i, row in df.iterrows():
    if (i > 0) and (i % 1000 == 0):
        print(f"Extract {i} entities")
    location = Location(name=row["Tên"], level=row["Cấp"])
    locations.append(location)
# quận, huyện
level1_entities = df["Quận Huyện"].unique()
for name in level1_entities:
    location = Location(name=name, level="Quận Huyện")
    locations.append(location)
# tỉnh, thành phố
level0_entities = df["Tỉnh / Thành Phố"].unique()
for name in level0_entities:
    location = Location(name=name, level="Tỉnh / Thành Phố")
    locations.append(location)
savepath = "data/locations.jl"
Knowledge.save(locations, savepath)
print(f"{len(locations)} entities is saved in {savepath}")
