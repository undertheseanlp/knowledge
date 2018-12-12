import json
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