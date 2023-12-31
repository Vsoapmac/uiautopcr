import pytest
import RunCase.PageInfo as page_info
from airtest.core.api import *
from RunCase.Page import Page
from RunCase.CommonButton import CommonButton
from Common.CustomAirtestPlugins import CustomAirtestPlugins
from Utils.YamlUtils import YamlUtils
from Utils.PathUtils import PathUtils
from Utils.LoggerUtils import LoggerUtils
from Utils.DataTimeUtils import DataTimeUtils


class ClientBasic:
    """服务端基础类"""
    # config.yml配置
    config_dict = YamlUtils.loadYamlFile(PathUtils.getConfigPath() + "config.yml")
    # 截图路径
    shot_path = PathUtils.getScriptShotPath()
    # 连接安卓模拟器或真机
    d = init_device(uuid=config_dict["client_url"], cap_method="JAVACAP", ori_method="ADBORI", touch_method="ADBTOUCH")
    w,h = d.get_current_resolution()
    # 设置logging
    LoggerUtils.setAirtestLogLevel()
    LoggerUtils.setBasicLoggingSettings(log_path=PathUtils.getOutPutPath(), encoding="GBK", is_write_log=config_dict["log_output"])
    logger = LoggerUtils.logger