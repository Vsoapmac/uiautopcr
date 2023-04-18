from Utils.PathUtils import PathUtils
import RunCase.PageInfo as page_info
from airtest.core.api import *


class Page:
    """主要页面"""
    __page_dict = page_info.page_dict
    __shot_path = PathUtils.getScriptShotPath()

    @classmethod
    def main_page(cls):
        """主页"""
        touch(Template(cls.__shot_path + cls.__page_dict["main"], record_pos=(-0.407, 0.266),
                       resolution=(1280, 720)))  # 我的主页

    @classmethod
    def mission_page(cls):
        """任务"""
        try:
            wait(Template(cls.__shot_path + cls.__page_dict["gift"], record_pos=(0.448, 0.177), resolution=(1280, 720)),
                 timeout=3)
            wait(Template(cls.__shot_path + cls.__page_dict["shop"], record_pos=(0.448, 0.177), resolution=(1280, 720)),
                 timeout=3)
            wait(Template(cls.__shot_path + cls.__page_dict["union"], record_pos=(0.448, 0.177), resolution=(1280, 720)),
                timeout=3)
            wait(Template(cls.__shot_path + cls.__page_dict["mission"], record_pos=(0.448, 0.177), resolution=(1280, 720)),
                timeout=3)
        except:
            cls.main_page()
            sleep(3)
        touch(Template(cls.__shot_path + cls.__page_dict["mission"], record_pos=(0.371, 0.175),
                       resolution=(1280, 720)))  # 任务

    @classmethod
    def gift_page(cls):
        """礼物"""
        try:
            wait(Template(cls.__shot_path + cls.__page_dict["shop"], record_pos=(0.448, 0.177), resolution=(1280, 720)),
                 timeout=3)
            wait(Template(cls.__shot_path + cls.__page_dict["union"], record_pos=(0.448, 0.177), resolution=(1280, 720)),
                timeout=3)
            wait(Template(cls.__shot_path + cls.__page_dict["mission"], record_pos=(0.448, 0.177),
                         resolution=(1280, 720)),
                timeout=3)
            wait(Template(cls.__shot_path + cls.__page_dict["gift"], record_pos=(0.448, 0.177), resolution=(1280, 720)),
                 timeout=3)
        except:
            cls.main_page()
            sleep(3)
        touch(Template(cls.__shot_path + cls.__page_dict["gift"], record_pos=(0.448, 0.177),
                       resolution=(1280, 720)))  # 礼物

    @classmethod
    def shop_page(cls):
        """商店"""
        try:
            wait(Template(cls.__shot_path + cls.__page_dict["gift"], record_pos=(0.448, 0.177), resolution=(1280, 720)),
                 timeout=3)
            wait(Template(cls.__shot_path + cls.__page_dict["union"], record_pos=(0.448, 0.177), resolution=(1280, 720)),
                timeout=3)
            wait(Template(cls.__shot_path + cls.__page_dict["mission"], record_pos=(0.448, 0.177), resolution=(1280, 720)),
                timeout=3)
            wait(Template(cls.__shot_path + cls.__page_dict["shop"], record_pos=(0.448, 0.177), resolution=(1280, 720)),
                 timeout=3)
        except:
            cls.main_page()
            sleep(3)
        touch(Template(cls.__shot_path + cls.__page_dict["shop"], record_pos=(0.142, 0.175),
                       resolution=(1280, 720)))  # 商店

    @classmethod
    def union_page(cls):
        """行会"""
        try:
            wait(Template(cls.__shot_path + cls.__page_dict["gift"], record_pos=(0.448, 0.177), resolution=(1280, 720)),
                 timeout=3)
            wait(Template(cls.__shot_path + cls.__page_dict["mission"], record_pos=(0.448, 0.177), resolution=(1280, 720)),
                timeout=3)
            wait(Template(cls.__shot_path + cls.__page_dict["shop"], record_pos=(0.448, 0.177), resolution=(1280, 720)),
                 timeout=3)
            wait(Template(cls.__shot_path + cls.__page_dict["union"], record_pos=(0.448, 0.177), resolution=(1280, 720)),
                timeout=3)
        except:
            cls.main_page()
            sleep(3)
        touch(Template(cls.__shot_path + cls.__page_dict["union"], record_pos=(0.22, 0.174),
                       resolution=(1280, 720)))  # 行会

    @classmethod
    def adventure_page(cls):
        """冒险"""
        touch(Template(cls.__shot_path + cls.__page_dict["adventure"], record_pos=(-0.002, 0.264),
                       resolution=(1280, 720)))  # 冒险

    @classmethod
    def invest_page(cls):
        """调查"""
        try:
            wait(Template(cls.__shot_path + cls.__page_dict["search"], record_pos=(0.448, 0.177),
                          resolution=(1280, 720)),
                 timeout=3)
            wait(Template(cls.__shot_path + cls.__page_dict["arana"], record_pos=(0.448, 0.177), resolution=(1280, 720)),
                 timeout=3)
            wait(
                Template(cls.__shot_path + cls.__page_dict["princess_arana"], record_pos=(0.448, 0.177), resolution=(1280, 720)),
                timeout=3)
            wait(Template(cls.__shot_path + cls.__page_dict["invest"], record_pos=(0.448, 0.177),
                          resolution=(1280, 720)),
                 timeout=3)
        except:
            cls.main_page()
            sleep(3)
            cls.adventure_page()
            sleep(3)
        touch(Template(cls.__shot_path + cls.__page_dict["invest"], record_pos=(0.267, 0.05),
                       resolution=(1280, 720)))  # 调查

    @classmethod
    def search_page(cls):
        """探索"""
        try:
            wait(Template(cls.__shot_path + cls.__page_dict["arana"], record_pos=(0.448, 0.177), resolution=(1280, 720)),
                 timeout=3)
            wait(
                Template(cls.__shot_path + cls.__page_dict["princess_arana"], record_pos=(0.448, 0.177), resolution=(1280, 720)),
                timeout=3)
            wait(Template(cls.__shot_path + cls.__page_dict["invest"], record_pos=(0.448, 0.177),
                          resolution=(1280, 720)),
                 timeout=3)
            wait(Template(cls.__shot_path + cls.__page_dict["search"], record_pos=(0.448, 0.177),
                          resolution=(1280, 720)),
                 timeout=3)
        except:
            cls.main_page()
            sleep(3)
            cls.adventure_page()
            sleep(3)
        touch(Template(cls.__shot_path + cls.__page_dict["search"], record_pos=(0.266, -0.094),
                       resolution=(1280, 720)))  # 探索

    @classmethod
    def arana_page(cls):
        """战斗竞技场"""
        try:
            wait(
                Template(cls.__shot_path + cls.__page_dict["princess_arana"], record_pos=(0.448, 0.177), resolution=(1280, 720)),
                timeout=3)
            wait(Template(cls.__shot_path + cls.__page_dict["invest"], record_pos=(0.448, 0.177),
                          resolution=(1280, 720)),
                 timeout=3)
            wait(Template(cls.__shot_path + cls.__page_dict["search"], record_pos=(0.448, 0.177),
                          resolution=(1280, 720)),
                 timeout=3)
            wait(
                Template(cls.__shot_path + cls.__page_dict["arana"], record_pos=(0.448, 0.177), resolution=(1280, 720)),
                timeout=3)
        except:
            cls.main_page()
            sleep(3)
            cls.adventure_page()
            sleep(3)
        touch(Template(cls.__shot_path + cls.__page_dict["arana"], record_pos=(0.105, 0.168),
                       resolution=(1280, 720)))  # 战斗竞技场

    @classmethod
    def princess_arana_page(cls):
        """公主竞技场"""
        try:
            wait(Template(cls.__shot_path + cls.__page_dict["invest"], record_pos=(0.448, 0.177),
                          resolution=(1280, 720)),
                 timeout=3)
            wait(Template(cls.__shot_path + cls.__page_dict["search"], record_pos=(0.448, 0.177),
                          resolution=(1280, 720)),
                 timeout=3)
            wait(
                Template(cls.__shot_path + cls.__page_dict["arana"], record_pos=(0.448, 0.177), resolution=(1280, 720)),
                timeout=3)
            wait(
                Template(cls.__shot_path + cls.__page_dict["princess_arana"], record_pos=(0.448, 0.177),
                         resolution=(1280, 720)),
                timeout=3)
        except:
            cls.main_page()
            sleep(3)
            cls.adventure_page()
            sleep(3)
        touch(Template(cls.__shot_path + cls.__page_dict["princess_arana"], record_pos=(0.36, 0.166),
                       resolution=(1280, 720)))  # 公主竞技场

    @classmethod
    def detect_limit_shop_open(cls, option):
        """
        检测是否开启限定商城

        :param option: 开启限定商城后的操作
        """
        pass

    @classmethod
    def detect_union_battle_open(cls):
        """检测是否开启公会战页面"""
        pass
