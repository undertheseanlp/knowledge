import json
import pandas as pd
from os import remove
from os.path import exists


class Knowledge:
    @staticmethod
    def save(entities, savepath):
        if exists(savepath):
            remove(savepath)
        f = open(savepath, "a")
        for entity in entities:
            content = json.dumps(entity.to_data(), ensure_ascii=False)
            f.write(content + "\n")

    @staticmethod
    def load(savepath):
        entities = []
        for line in open(savepath):
            entity = json.loads(line.strip())
            entities.append(entity)
        return entities

    @staticmethod
    def stats(entities):
        print(f"Total  : {len(entities)}")
        levels = [entity["level"] for entity in entities]
        print(pd.Series(levels).value_counts())