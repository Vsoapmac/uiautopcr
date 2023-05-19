import yaml


class YamlUtils:
    """yaml工具类"""

    @classmethod
    def loadYamlFile(cls, file_path: str, encoding="UTF-8") -> dict:
        """
        加载yaml文件

        Args:
            file_path: yaml文件路径
            encoding: 编码，默认为uft-8

        Returns:
            yaml转换后的数据

        Examples:
            >>> load_data = YamlUtils.loadYamlFile("example.yml")
            >>> load_data["test"]
            >>> load_data.get("test")
        """
        with open(file_path, mode="r", encoding=encoding) as f:
            load_data = yaml.safe_load(f)
        return load_data

    @classmethod
    def dumpDataToYaml(cls, file_path: str, dict_data: dict, encoding="UTF-8"):
        """
        将数据写入yaml文件
        !!!注意该方法会覆盖yaml中的全部数据!!!

        Args:
            file_path: yaml文件路径
            dict_data: 字典数据
            encoding: 编码，默认为uft-8
        """
        dump_data = yaml.safe_dump(dict_data)
        with open(file_path, mode="w", encoding=encoding) as f:
            f.write(dump_data)

    @classmethod
    def getValue(cls, dict_data: dict, key: str):
        """
        获取字典中的值

        Args:
            dict_data: 字典数据
            key: key

        Returns:
            对应key的value

        Examples:
            >>> load_data = YamlUtils.loadYamlFile("example.yml")
            >>> value = YamlUtils.getValue(load_data)
        """
        return dict_data[key]
