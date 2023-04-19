import pathlib

__project_name = "uiautopcr"
parent = pathlib.Path().absolute().parent
root = str(parent).replace("\\", "/")
root = root[0:root.find(__project_name)+len(__project_name)] # 切割到项目根目录
print(root)