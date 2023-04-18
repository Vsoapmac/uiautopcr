import yaml


class YamlUtils:
    """yaml工具类"""

    @classmethod
    def loadYamlFile(cls, file_path, encoding="UTF-8"):
        """
        加载yaml文件

        :param file_path: yaml文件路径
        :param encoding: 编码，默认为uft-8
        :return: yaml转换后的数据，格式为字典
        """
        with open(file_path, mode="r", encoding=encoding) as f:
            load_data = yaml.safe_load(f)
        return load_data

    @classmethod
    def dumpDataToYaml(cls, file_path, dict_data, encoding="UTF-8"):
        """
        将数据写入yaml文件
        !!!注意该方法会覆盖yaml中的全部数据!!!

        :param file_path: yaml文件路径
        :param dict_data: 字典数据
        :param encoding: 编码，默认为uft-8
        :return:
        """
        dump_data = yaml.safe_dump(dict_data)
        with open(file_path, mode="w", encoding=encoding) as f:
            f.write(dump_data)

    @classmethod
    def getValue(cls, dict_data, key):
        """
        获取字典中的值
        可以配合`loadYamlFile`方法使用

        :param dict_data: 字典数据
        :param key: key
        :return: 对应key的值

        :Examples:
        >>> load_data = YamlUtils.loadYamlFile("example.yml")
        >>> value = YamlUtils.getValue(load_data)
        """
        return dict_data[key]
