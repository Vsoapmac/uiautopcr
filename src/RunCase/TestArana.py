from Common.ClientBasic import *


class TestPreArana(ClientBasic):
    """竞技场"""
    __page_dict = page_info.arana_dict

    def test_arana(self, arana_page):
        """竞技场,开始:冒险,结束:冒险"""
        touch(Template(self.shot_path + self.__page_dict["colloct_arana_coin"], record_pos=(-0.192, 0.073), resolution=(1280, 720))) # 收取
        touch(0.612*self.w,0.302*self.h) # 点击第一个人
        CommonButton.start_battle()
        # TODO:增加执行逻辑

    def test_princess_arana(self, princess_arana_page):
        """公主竞技场,开始:冒险,结束:冒险"""
        touch(Template(self.shot_path + self.__page_dict["colloct_arana_coin"], record_pos=(-0.192, 0.073), resolution=(1280, 720)))  # 收取
        touch(0.612*self.w,0.302*self.h) # 点击第一个人
        # touch(Template(self.shot_path + self.__page_dict["pricess_arana_battle_team_1"], record_pos=(-0.398, -0.189), resolution=(1280, 720))) # 队伍1(备份)
        touch(Template(self.shot_path + self.__page_dict["pricess_arana_battle_team_3"], record_pos=(-0.152, -0.19), resolution=(1280, 720))) # 队伍3
        CommonButton.start_battle()
        # TODO:增加执行逻辑

    @pytest.fixture
    def arana_page(self):
        """竞技场"""
        try:
            wait(Template(self.shot_path + self.__page_dict["arana_battle_history"], record_pos=(-0.384, 0.164), resolution=(1280, 720), threshold=0.9), timeout=2) # 对战覆历
            wait(Template(self.shot_path + self.__page_dict["arana_defend_setting"], record_pos=(-0.231, 0.165), resolution=(1280, 720), threshold=0.9), timeout=2) # 防守设定
        except:
            Page.arana_page()

    @pytest.fixture
    def princess_arana_page(self):
        """公主竞技场"""
        try:
            wait(Template(self.shot_path + self.__page_dict["pricess_arana_battle_history"], record_pos=(-0.385, 0.175), resolution=(1280, 720), threshold=0.9), timeout=2)  # 对战覆历
            wait(Template(self.shot_path + self.__page_dict["pricess_defend_setting"], record_pos=(-0.231, 0.175), resolution=(1280, 720), threshold=0.9), timeout=2)  # 防守设定
        except:
            Page.princess_arana_page()