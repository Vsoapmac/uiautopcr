from Common.ClientBasic import *


class TestGift(ClientBasic):
    """礼物"""
    __page_dict = page_info.gift_dict

    def test_collect_gift(self):
        """收集礼物奖励,开始:主页,结束:主页"""
        touch(Template(self.shot_path + self.__page_dict["cancel_check_with_gift_energy"], record_pos=(-0.124, 0.214), resolution=(1280, 720))) # 取消勾选
        touch(Template(self.shot_path + self.__page_dict["collect_all_mission_reward"], record_pos=(0.341, 0.215), resolution=(1280, 720))) # 全部收取


