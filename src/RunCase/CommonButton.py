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
        touch(Template(r"tpl1681996727065.png", record_pos=(-0.468, -0.248), resolution=(1280, 720))) # 返回


    @classmethod
    def cancel(cls):
        """取消"""
        touch(Template(cls.__shot_path+cls.__page_dict["cancel"], record_pos=(-0.114, 0.216), resolution=(1280, 720), threshold=0.9)) # 取消

    @classmethod
    def close(cls):
        """关闭"""
        pass

    @classmethod
    def white_comfirm(cls):
        """白色确认按钮"""
        touch(Template(cls.__shot_path+cls.__page_dict["white_comfirm"], record_pos=(-0.001, 0.216), resolution=(1280, 720), threshold=0.9)) # 白色确认按钮


    @classmethod
    def blue_comfirm(cls):
        """蓝色确认按钮"""
        touch(Template(cls.__shot_path+cls.__page_dict["blue_comfirm"], record_pos=(0.114, 0.103), resolution=(1280, 720), threshold=0.9)) # 蓝色确认按钮
