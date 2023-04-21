import pathlib
from Utils.YamlUtils import YamlUtils


class PathUtils:
    """文件目录工具类"""

    @classmethod
    def getRootPath(cls):
        """
        获取项目根目录绝对路径
        
        :return: 项目根目录绝对路径
        """
        # 获取project_name
        project_name = "uiautopcr"
        # 获取根目录
        parent = pathlib.Path().absolute().parent
        root = str(parent).replace("\\", "/")
        root = root[0:root.find(project_name)+len(project_name)] # 不同未知的py文件的父目录是不同的，预防这个情况切割字符串拿到项目根目录
        return root + "/"

    @classmethod
    def getConfigPath(cls):
        """
        获取项目config文件夹绝对路径

        :return: config文件夹绝对路径
        """
        root = cls.getRootPath()
        return root + "config/"

    @classmethod
    def getOutPutPath(cls):
        """
        获取项目output文件夹绝对路径

        :return: output文件夹绝对路径
        """
        root = cls.getRootPath()
        return root + "output/"

    @classmethod
    def getResourcesPath(cls):
        """
        获取项目resources文件夹绝对路径

        :return: resources文件夹绝对路径
        """
        root = cls.getRootPath()
        return root + "resources/"

    @classmethod
    def getScriptShotPath(cls):
        """
        获取项目scriptshot文件夹绝对路径

        :return: scriptshot文件夹绝对路径
        """
        resources_path = cls.getResourcesPath()
        return resources_path + "scriptshot/"

    @classmethod
    def getRunCasePath(cls):
        """
        获取项目RunCase文件夹绝对路径

        :return: RunCase文件夹绝对路径
        """
        root = cls.getRootPath()
        return root + "src/RunCase/"

    @classmethod
    def getPluginsPath(cls):
        """
        获取项目Plugins文件夹绝对路径

        :return: Plugins文件夹绝对路径
        """
        root = cls.getRootPath()
        return root + "src/Plugins/"
