from Utils.PathUtils import PathUtils
import RunCase.PageInfo as page_info
from airtest.core.api import *


class CommonButton:
    """公共按钮"""
    __page_dict = page_info.common_button_dict
    __shot_path = PathUtils.getScriptShotPath()

    @classmethod
    def next(cls):
        """下一步"""
        pass

    @classmethod
    def back(cls):
        """返回"""
        pass

    @classmethod
    def cancel(cls):
        """取消"""
        touch(Template(cls.__shot_path+cls.__page_dict["cancel"], record_pos=(-0.114, 0.216), resolution=(1280, 720))) # 取消

    @classmethod
    def close(cls):
        """关闭"""
        pass

    @classmethod
    def white_comfirm(cls):
        """白色确认按钮"""
        touch(Template(cls.__shot_path+cls.__page_dict["white_comfirm"], record_pos=(-0.001, 0.216), resolution=(1280, 720))) # 白色确认按钮


    @classmethod
    def blue_comfirm(cls):
        """蓝色确认按钮"""
        touch(Template(cls.__shot_path+cls.__page_dict["blue_comfirm"], record_pos=(0.114, 0.103), resolution=(1280, 720))) # 蓝色确认按钮
