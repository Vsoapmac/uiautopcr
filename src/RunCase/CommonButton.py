from Utils.PathUtils import PathUtils
import RunCase.PageInfo as page_info
from airtest.core.api import *


class CommonButton:
    """公共按钮"""
    __page_dict = page_info.common_button_dict
    __shot_path = PathUtils.getScriptShotPath()
    __default_timeout = 5

    @classmethod
    def next(cls):
        """下一步"""
        wait(Template(cls.__shot_path+cls.__page_dict["next"], record_pos=(0.351, 0.23), resolution=(1280, 720)), timeout=cls.__default_timeout) # 下一步
        touch(Template(cls.__shot_path+cls.__page_dict["next"], record_pos=(0.351, 0.23), resolution=(1280, 720))) # 下一步

    @classmethod
    def back(cls):
        """返回"""
        wait(Template(cls.__shot_path+cls.__page_dict["back"], record_pos=(-0.468, -0.248), resolution=(1280, 720)), timeout=cls.__default_timeout) # 返回
        touch(Template(cls.__shot_path+cls.__page_dict["back"], record_pos=(-0.468, -0.248), resolution=(1280, 720))) # 返回

    @classmethod
    def cancel(cls):
        """取消"""
        wait(Template(cls.__shot_path+cls.__page_dict["cancel"], record_pos=(-0.114, 0.216), resolution=(1280, 720), threshold=0.9), timeout=cls.__default_timeout) # 取消
        touch(Template(cls.__shot_path+cls.__page_dict["cancel"], record_pos=(-0.114, 0.216), resolution=(1280, 720), threshold=0.9)) # 取消

    @classmethod
    def close(cls):
        """关闭"""
        wait(Template(cls.__shot_path+cls.__page_dict["close"], threshold=0.9, record_pos=(0.0, 0.218), resolution=(1280, 720)), timeout=cls.__default_timeout) # 关闭
        touch(Template(cls.__shot_path+cls.__page_dict["close"], threshold=0.9, record_pos=(0.0, 0.218), resolution=(1280, 720))) # 关闭

    @classmethod
    def white_comfirm(cls):
        """白色确认按钮"""
        wait(Template(cls.__shot_path+cls.__page_dict["white_comfirm"], record_pos=(-0.001, 0.216), resolution=(1280, 720), threshold=0.9), timeout=cls.__default_timeout) # 白色确认按钮
        touch(Template(cls.__shot_path+cls.__page_dict["white_comfirm"], record_pos=(-0.001, 0.216), resolution=(1280, 720), threshold=0.9)) # 白色确认按钮

    @classmethod
    def blue_comfirm(cls):
        """蓝色确认按钮"""
        wait(Template(cls.__shot_path+cls.__page_dict["blue_comfirm"], record_pos=(0.114, 0.103), resolution=(1280, 720), threshold=0.9), timeout=cls.__default_timeout) # 蓝色确认按钮
        touch(Template(cls.__shot_path+cls.__page_dict["blue_comfirm"], record_pos=(0.114, 0.103), resolution=(1280, 720), threshold=0.9)) # 蓝色确认按钮

    @classmethod
    def start_battle(cls):
        """战斗开始"""
        wait(Template(cls.__shot_path+cls.__page_dict["start_battle"], record_pos=(0.373, 0.191), resolution=(1280, 720)), timeout=cls.__default_timeout)  # 战斗开始
        touch(Template(cls.__shot_path+cls.__page_dict["start_battle"], record_pos=(0.373, 0.191), resolution=(1280, 720)))  # 战斗开始

