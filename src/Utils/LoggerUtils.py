import logging, sys, os
from Utils.DataTimeUtils import DataTimeUtils
from Utils.PathUtils import PathUtils


class LoggerUtils:
    """log公共类"""
    logger = logging.getLogger("uiautopcr")  # 用该变量使用 log 模块

    @classmethod
    def setAirtestLogLevel(cls, level=logging.ERROR):
        """
        设置airtest显示log的level

        Args:
            level: log等级，默认error
        """
        logger = logging.getLogger("airtest")
        logger.setLevel(level)

    @classmethod
    def setBasicLoggingSettings(cls, log_path: str, encoding="UTF-8", level=logging.INFO, is_print_log=True, is_write_log=False):
        """
        基础的Log设置

        Args:
            log_path: log日志文件保存目录
            encoding: log文件的字节编码，默认UTF-8
            level: log的level，默认INFO
            is_print_log: 是否打印log文件，默认True
            is_write_log: 是否写入log文件，默认false

        Examples:
            >>> LoggerUtils.setBasicLoggingSettings(log_path = "./", is_write_log=True)
            >>> logger = LoggerUtils.logger
            >>> logger.info("test")
        """
        ## 写入 Log 的基础设置
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')
        cls.logger.setLevel(level)
        if is_write_log:
            today = DataTimeUtils.getDay()
            year = DataTimeUtils.getTimeByPattern(DataTimeUtils.YEAR_PATTERN)
            month = DataTimeUtils.getTimeByPattern(DataTimeUtils.MONTH_PATTERN)
            # 检测 Log 文件是否存在，不存在则创建
            log_path = log_path+"/" if log_path[-1] != "/" else log_path
            path = f"{log_path}log/{year}/{month}月/"
            filename = f"{today}.log"
            # 文件夹不存在则创建
            if not os.path.exists(path):
                os.makedirs(path)
            # 文件不存在则创建
            if not os.path.exists(path + filename):
                with open(path + filename, 'w', encoding=encoding) as f:
                    f.close()
            file_handler = logging.FileHandler(path + filename)
            file_handler.setFormatter(formatter)
            file_handler.setLevel(level)
            cls.logger.addHandler(file_handler)
        if is_print_log:
            ## 打印 Log 的基础设置
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(formatter)  # %(asctime)s
            console_handler.setLevel(level)
            cls.logger.addHandler(console_handler)
