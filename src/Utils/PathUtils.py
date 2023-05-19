import pathlib
from Utils.YamlUtils import YamlUtils


class PathUtils:
    """文件目录工具类"""

    @classmethod
    def transferPathUrl(cls, file_path: str) -> str:
        """
        将文件路径中的\转换成/，一般用于兼容linux、windows等平台

        Args:
            file_path: 文件路径

        Returns:
            转换后的文件路径
        """
        return file_path.replace("\\","/") if file_path[-1] != "/" or file_path[-1] != "\\" else file_path.replace("\\","/") + "/"

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
