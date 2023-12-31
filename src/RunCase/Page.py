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
        try:
            wait(Template(cls.__shot_path + cls.__page_dict["gift"], record_pos=(0.448, 0.177), resolution=(1280, 720), threshold=0.9),
                 timeout=2)
            wait(Template(cls.__shot_path + cls.__page_dict["shop"], record_pos=(0.142, 0.175), resolution=(1280, 720), threshold=0.9),
                 timeout=2)
            wait(Template(cls.__shot_path + cls.__page_dict["union"], record_pos=(0.22, 0.174), resolution=(1280, 720), threshold=0.9),
                timeout=2)
            wait(Template(cls.__shot_path + cls.__page_dict["mission"], record_pos=(0.371, 0.175), resolution=(1280, 720), threshold=0.9),
                 timeout=2)
        except:
            # 重置状态
            touch(Template(cls.__shot_path + cls.__page_dict["main_menu"], record_pos=(0.409, 0.264), resolution=(1280, 720))) # 主菜单
            sleep(3)
            touch(Template(cls.__shot_path + cls.__page_dict["main"], record_pos=(-0.407, 0.266), resolution=(1280, 720)))  # 我的主页
            sleep(3)
        """
        为了保证容错再检查一次
        """
        if exists(Template(cls.__shot_path + cls.__page_dict["mission"], record_pos=(0.371, 0.175), resolution=(1280, 720), threshold=0.9)) == False:
            touch(Template(cls.__shot_path + cls.__page_dict["main"], record_pos=(-0.407, 0.266),
                           resolution=(1280, 720)))  # 我的主页
            sleep(3)

    @classmethod
    def mission_page(cls):
        """任务"""
        cls.main_page()
        touch(Template(cls.__shot_path + cls.__page_dict["mission"], record_pos=(0.371, 0.175),
                       resolution=(1280, 720)))  # 任务
        sleep(3)

    @classmethod
    def gift_page(cls):
        """礼物"""
        cls.main_page()
        touch(Template(cls.__shot_path + cls.__page_dict["gift"], record_pos=(0.448, 0.177),
                       resolution=(1280, 720)))  # 礼物
        sleep(3)

    @classmethod
    def shop_page(cls):
        """商店"""
        cls.main_page()
        touch(Template(cls.__shot_path + cls.__page_dict["shop"], record_pos=(0.142, 0.175),
                       resolution=(1280, 720)))  # 商店
        sleep(3)

    @classmethod
    def union_page(cls):
        """行会"""
        cls.main_page()
        touch(Template(cls.__shot_path + cls.__page_dict["union"], record_pos=(0.22, 0.174),
                       resolution=(1280, 720)))  # 行会
        sleep(3)
    
    @classmethod
    def department_page(cls):
        """公会之家"""
        # 检测是否在公会之家页面
        try:
            wait(Template(cls.__shot_path + page_info.department_dict["deparment_level_2"], record_pos=(-0.438, -0.141),
                           resolution=(1280, 720)),timeout=2)  # 2层
            wait(Template(cls.__shot_path + page_info.department_dict["deparment_level_3"], record_pos=(-0.438, -0.191),
                           resolution=(1280, 720)),timeout=2)  # 3层
        except:
            touch(Template(cls.__shot_path + cls.__page_dict["department"], record_pos=(0.148, 0.265), resolution=(1280, 720))) # 公会之家
            # 等待公会之家进入完毕
            wait(Template(cls.__shot_path + cls.__page_dict["main"], record_pos=(-0.407, 0.266),
                               resolution=(1280, 720)))  # 我的主页
            sleep(3)
    
    @classmethod
    def adventure_page(cls):
        """冒险"""
        try:
            wait(Template(cls.__shot_path + cls.__page_dict["search"], record_pos=(0.266, -0.094), resolution=(1280, 720), threshold=0.9),
                 timeout=2)
            wait(Template(cls.__shot_path + cls.__page_dict["arana"], record_pos=(0.105, 0.168), resolution=(1280, 720), threshold=0.9),
                 timeout=2)
            wait(Template(cls.__shot_path + cls.__page_dict["princess_arana"], record_pos=(0.36, 0.166), resolution=(1280, 720), threshold=0.9),
                timeout=2)
            wait(Template(cls.__shot_path + cls.__page_dict["invest"], record_pos=(0.267, 0.05),resolution=(1280, 720), threshold=0.9),
                 timeout=2)
        except:
            # 重置状态
            touch(Template(cls.__shot_path + cls.__page_dict["main_menu"], record_pos=(0.409, 0.264), resolution=(1280, 720))) # 主菜单
            sleep(3)
            touch(Template(cls.__shot_path + cls.__page_dict["adventure"], record_pos=(-0.002, 0.264),
                           resolution=(1280, 720)))  # 冒险
            sleep(3)
        """
        为了保证容错再检查一次
        """
        if exists(Template(cls.__shot_path + cls.__page_dict["search"], record_pos=(0.266, -0.094), resolution=(1280, 720), threshold=0.9)) == False:
            touch(Template(cls.__shot_path + cls.__page_dict["adventure"], record_pos=(-0.002, 0.264),
                           resolution=(1280, 720)))  # 冒险
            sleep(3)

    @classmethod
    def invest_page(cls):
        """调查"""
        cls.adventure_page()
        touch(Template(cls.__shot_path + cls.__page_dict["invest"], record_pos=(0.267, 0.05),
                       resolution=(1280, 720)))  # 调查
        sleep(3)

    @classmethod
    def search_page(cls):
        """探索"""
        cls.adventure_page()
        touch(Template(cls.__shot_path + cls.__page_dict["search"], record_pos=(0.266, -0.094),
                       resolution=(1280, 720)))  # 探索
        sleep(3)

    @classmethod
    def arana_page(cls):
        """战斗竞技场"""
        cls.adventure_page()
        touch(Template(cls.__shot_path + cls.__page_dict["arana"], record_pos=(0.105, 0.168),
                       resolution=(1280, 720)))  # 战斗竞技场
        sleep(3)

    @classmethod
    def princess_arana_page(cls):
        """公主竞技场"""
        cls.adventure_page()
        touch(Template(cls.__shot_path + cls.__page_dict["princess_arana"], record_pos=(0.36, 0.166), resolution=(1280, 720)))  # 公主竞技场
        sleep(3)

    @classmethod
    def dungeons_page(cls):
        """地下城"""
        cls.adventure_page()
        touch(Template(cls.__shot_path + cls.__page_dict["dungeons_page"], record_pos=(0.415, -0.094), resolution=(1280, 720))) # 地下城


    @classmethod
    def detect_limit_shop_open(cls, option="buy_all"):
        """
        检测是否开启限定商城

        :param option: 开启限定商城后的操作
        """
        try:
            wait(Template(cls.__shot_path+page_info.shop_dict["limit_shop_open"], record_pos=(-0.01, -0.193), resolution=(1280, 720), threshold=0.9), timeout=5) # 限定商店开启
            if option == "buy_all":
                touch(Template(cls.__shot_path+page_info.shop_dict["click_all_limit_shop"], record_pos=(0.183, -0.152), resolution=(1280, 720), threshold=0.9)) # 点击全部
                sleep(1)
                touch(Template(cls.__shot_path+page_info.shop_dict["chose_all_limit_shop"], record_pos=(0.395, -0.151), resolution=(1280, 720), threshold=0.9)) # 点击全选
                sleep(1)
                touch(Template(cls.__shot_path+page_info.shop_dict["buy_all_by_one_click"], record_pos=(0.353, 0.213), resolution=(1280, 720))) # 一键购买
                sleep(1)
                touch(Template(cls.__shot_path+page_info.common_button_dict["blue_comfirm"], record_pos=(0.114, 0.103), resolution=(1280, 720))) # 蓝色确认按钮
                sleep(3)
                touch(Template(cls.__shot_path+page_info.common_button_dict["blue_comfirm"], record_pos=(0.114, 0.103), resolution=(1280, 720))) # 蓝色确认按钮
                sleep(3)
                touch(Template(cls.__shot_path+page_info.common_button_dict["cancel"], record_pos=(-0.114, 0.216), resolution=(1280, 720))) # 取消
            sleep(3)
        except:
            pass


    @classmethod
    def detect_union_battle_open(cls):
        """检测是否开启公会战页面"""
        pass

