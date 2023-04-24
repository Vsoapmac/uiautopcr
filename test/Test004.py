import os

path = "../resources/scriptshot/"
with os.scandir(path) as dir_entitys:
    for entity in dir_entitys:
        print(entity.name)