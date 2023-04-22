from Common.ClientBasic import *


class TestArana(ClientBasic):
    """竞技场"""
    __page_dict = page_info.arana_dict

    def test_arana(self, arana_page):
        """竞技场,开始:冒险,结束:冒险"""
        try:
            wait(Template(r"arana_defend_success.png", record_pos=(-0.163, -0.082), resolution=(1280, 720), threshold=0.9), timeout=2) # 防守成功
            touch(Template(r"arana_defend_success.png", record_pos=(-0.163, -0.082), resolution=(1280, 720))) # 防守成功
            CommonButton.cancel()
        except:
            pass
        # 收取竞技场金币
        touch(Template(self.shot_path + self.__page_dict["colloct_arana_coin"], record_pos=(-0.192, 0.073), resolution=(1280, 720))) # 收取
        try:
            wait(Template(self.shot_path + page_info.common_button_dict["white_comfirm"], threshold=0.9, record_pos=(-0.001, 0.216), resolution=(1280, 720)), timeout=2)  # 白色确认按钮
            touch(Template(self.shot_path + page_info.common_button_dict["white_comfirm"], threshold=0.9, record_pos=(-0.001, 0.216), resolution=(1280, 720)))  # 白色确认按钮
            sleep(2)
        except:
            pass
        touch([0.612 * self.w, 0.302 * self.h])  # 点击第一个人
        sleep(2)
        # TODO:增加全部次数用完之后，无法继续进行的逻辑
        in_coding = False
        try:
            wait(Template(self.shot_path + self.__page_dict["target_in_coding"], record_pos=(-0.005, -0.008), resolution=(1280, 720), threshold=0.9), timeout=2)  # 目标处于冷却时间
            in_coding = True
        except:
            pass
        if not in_coding:
            CommonButton.start_battle()
            wait(Template(self.shot_path + page_info.common_button_dict["next"], threshold=0.9, record_pos=(0.351, 0.23), resolution=(1280, 720)), timeout=100)  # 下一步
            touch(Template(self.shot_path + page_info.common_button_dict["next"], threshold=0.9, record_pos=(0.351, 0.23), resolution=(1280, 720)))  # 下一步
            # TODO:增加进攻成功后，排名晋升提示框的取消逻辑(CommonButton.white_comfirm())
        else:
            CommonButton.cancel()

    def test_princess_arana(self, princess_arana_page):
        """公主竞技场,开始:冒险,结束:冒险"""
        # TODO:增加防守成功后提示框的取消逻辑
        # 收取竞技场金币
        touch(Template(self.shot_path + self.__page_dict["colloct_arana_coin"], record_pos=(-0.192, 0.073), resolution=(1280, 720)))  # 收取
        try:
            wait(Template(self.shot_path + page_info.common_button_dict["white_comfirm"], threshold=0.9, record_pos=(-0.001, 0.216),
                         resolution=(1280, 720)), timeout=2) # 白色确认按钮
            touch(Template(self.shot_path + page_info.common_button_dict["white_comfirm"], threshold=0.9, record_pos=(-0.001, 0.216),
                         resolution=(1280, 720))) # 白色确认按钮
            sleep(2)
        except:
            pass
        touch([0.612*self.w,0.302*self.h]) # 点击第一个人
        sleep(2)
        # TODO:增加全部次数用完之后，无法继续进行的逻辑
        in_coding = False
        try:
            wait(Template(self.shot_path + self.__page_dict["target_in_coding"], record_pos=(-0.005, -0.008), resolution=(1280, 720), threshold=0.9), timeout=2) # 目标处于冷却时间
            in_coding = True
        except:
            pass
        if not in_coding:
            # touch(Template(self.shot_path + self.__page_dict["pricess_arana_battle_team_1"], record_pos=(-0.398, -0.189), resolution=(1280, 720))) # 队伍1(备份)
            touch(Template(self.shot_path + self.__page_dict["pricess_arana_battle_team_3"], record_pos=(-0.152, -0.19), resolution=(1280, 720))) # 队伍3
            sleep(1)
            CommonButton.start_battle()
            wait(Template(self.shot_path + page_info.common_button_dict["next"], threshold=0.9, record_pos=(0.351, 0.23), resolution=(1280, 720)), timeout=100) # 下一步
            touch(Template(self.shot_path + page_info.common_button_dict["next"], threshold=0.9, record_pos=(0.351, 0.23), resolution=(1280, 720))) # 下一步
            # TODO:增加进攻成功后，排名晋升提示框的取消逻辑(CommonButton.white_comfirm())
        else:
            CommonButton.cancel()

    @pytest.fixture
    def arana_page(self):
        """竞技场"""
        try:
            wait(Template(self.shot_path + self.__page_dict["arana_battle_history"], record_pos=(-0.384, 0.164), resolution=(1280, 720), threshold=0.9), timeout=2) # 对战覆历
            wait(Template(self.shot_path + self.__page_dict["arana_defend_setting"], record_pos=(-0.231, 0.165), resolution=(1280, 720), threshold=0.9), timeout=2) # 防守设定
            wait(Template(self.shot_path + self.__page_dict["arana_tag"], threshold=0.9, record_pos=(-0.362, -0.252), resolution=(1280, 720)), timeout=2) # 竞技场标签
        except:
            Page.arana_page()

    @pytest.fixture
    def princess_arana_page(self):
        """公主竞技场"""
        try:
            wait(Template(self.shot_path + self.__page_dict["pricess_arana_battle_history"], record_pos=(-0.385, 0.175), resolution=(1280, 720), threshold=0.9), timeout=2)  # 对战覆历
            wait(Template(self.shot_path + self.__page_dict["pricess_defend_setting"], record_pos=(-0.231, 0.175), resolution=(1280, 720), threshold=0.9), timeout=2)  # 防守设定
            wait(Template(self.shot_path + self.__page_dict["pricess_arana_tag"], threshold=0.9, record_pos=(-0.361, -0.252), resolution=(1280, 720)), timeout=2) # 公主竞技场标签
        except:
            Page.princess_arana_page()


