from Common.ClientBasic import *


class TestPreArana(ClientBasic):
    """竞技场"""
    __page_dict = page_info.arana_dict

    def test_arana(self):
        """竞技场,开始:冒险,结束:冒险"""
        touch(0.612*self.w,0.302*self.h) # 点击第一个人
        touch(Template(self.shot_path + self.__page_dict["colloct_arana_coin"], record_pos=(-0.192, 0.073), resolution=(1280, 720))) # 收取
        touch(Template(self.shot_path + self.__page_dict["arana_battle_history"], record_pos=(-0.384, 0.164), resolution=(1280, 720))) # 对战覆历
        touch(Template(self.shot_path + self.__page_dict["arana_defend_setting"], record_pos=(-0.231, 0.165), resolution=(1280, 720))) # 防守设定


    def princess_arana(self):
        """公主竞技场,开始:冒险,结束:冒险"""
        touch(0.612*self.w,0.302*self.h) # 点击第一个人
        touch(Template(self.shot_path + self.__page_dict["pricess_arana_battle_history"], record_pos=(-0.385, 0.175), resolution=(1280, 720))) # 对战覆历
        touch(Template(self.shot_path + self.__page_dict["pricess_defend_setting"], record_pos=(-0.231, 0.175), resolution=(1280, 720))) # 防守设定
        touch(Template(self.shot_path + self.__page_dict["pricess_arana_battle_team_1"], record_pos=(-0.398, -0.189), resolution=(1280, 720))) # 队伍1
        touch(Template(self.shot_path + self.__page_dict["pricess_arana_battle_team_3"], record_pos=(-0.152, -0.19), resolution=(1280, 720))) # 队伍3

