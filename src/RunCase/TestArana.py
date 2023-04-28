from Common.ClientBasic import *


class TestArana(ClientBasic):
    """竞技场"""
    __page_dict = page_info.arana_dict

    def test_arana(self, arana_page):
        """竞技场,开始:冒险,结束:冒险"""
        try:
            wait(Template(r"arana_defend_success.png", record_pos=(-0.163, -0.082), resolution=(1280, 720), threshold=0.9), timeout=2) # 防守成功
            self.logger.info("检测到防守成功，取消页面")
        except:
            pass
        else:
            CommonButton.cancel()
        # 收取竞技场金币
        self.logger.info("收取竞技场金币")
        touch(Template(self.shot_path + self.__page_dict["colloct_arana_coin"], record_pos=(-0.192, 0.073), resolution=(1280, 720))) # 收取
        try:
            wait(Template(self.shot_path + page_info.common_button_dict["white_comfirm"], threshold=0.9, record_pos=(-0.001, 0.216), resolution=(1280, 720)), timeout=2)  # 白色确认按钮
            touch(Template(self.shot_path + page_info.common_button_dict["white_comfirm"], threshold=0.9, record_pos=(-0.001, 0.216), resolution=(1280, 720)))  # 白色确认按钮
            sleep(2)
            self.logger.info("收取竞技场金币完成")
        except:
            self.logger.info("没有竞技场金币")
        self.logger.info("点击竞技场第一个人")
        touch([0.612 * self.w, 0.302 * self.h])  # 点击第一个人
        sleep(2)
        """
        首先判断挑战次数
        """
        reach_maximum_limit = False
        try:
            wait(Template(self.shot_path + self.__page_dict["challenge_count_maximum_limit"], record_pos=(-0.005, -0.07), resolution=(1280, 720), threshold=0.9), timeout=2)  # 今天的挑战次数已经达到上限
            reach_maximum_limit = True
        except:
            pass
        else:
            self.logger.info("今天的挑战次数已经达到上限，返回")
            CommonButton.cancel()
        """
        然后判断是否冷却中
        """
        if not reach_maximum_limit:
            in_coding = False
            try:
                wait(Template(self.shot_path + self.__page_dict["target_in_coding"], record_pos=(-0.005, -0.008), resolution=(1280, 720), threshold=0.9), timeout=2)  # 目标处于冷却时间
                in_coding = True
            except:
                pass
            else:
                self.logger.info("竞技场正在冷却中，返回")
                CommonButton.cancel()
            """
            一切正常则开始战斗
            """
            if not in_coding:
                self.logger.info("开始战斗")
                CommonButton.start_battle()
                wait(Template(self.shot_path + page_info.common_button_dict["next"], threshold=0.9, record_pos=(0.351, 0.23), resolution=(1280, 720)), timeout=100)  # 下一步
                touch(Template(self.shot_path + page_info.common_button_dict["next"], threshold=0.9, record_pos=(0.351, 0.23), resolution=(1280, 720)))  # 下一步
                self.logger.info("战斗结束")
                sleep(2)
                try:
                    wait(Template(self.shot_path + self.__page_dict["arana_rank_promot"], threshold=0.9, record_pos=(-0.099, 0.113), resolution=(1280, 720)), timeout=2) # 排名晋升
                    self.logger.info("排名晋升，取消页面")
                except:
                    pass
                else:
                    CommonButton.white_comfirm()

    def test_princess_arana(self, princess_arana_page):
        """公主竞技场,开始:冒险,结束:冒险"""
        # TODO:增加防守成功后提示框的取消逻辑
        # self.logger.info("检测到防守成功，取消页面")
        # 收取竞技场金币
        self.logger.info("收取公主竞技场金币")
        touch(Template(self.shot_path + self.__page_dict["colloct_arana_coin"], record_pos=(-0.192, 0.073), resolution=(1280, 720)))  # 收取
        try:
            wait(Template(self.shot_path + page_info.common_button_dict["white_comfirm"], threshold=0.9, record_pos=(-0.001, 0.216),
                         resolution=(1280, 720)), timeout=2) # 白色确认按钮
            touch(Template(self.shot_path + page_info.common_button_dict["white_comfirm"], threshold=0.9, record_pos=(-0.001, 0.216),
                         resolution=(1280, 720))) # 白色确认按钮
            sleep(2)
            self.logger.info("收取公主竞技场金币完成")
        except:
            self.logger.info("没有公主竞技场金币")
        self.logger.info("点击公主竞技场第一个人")
        touch([0.612*self.w,0.302*self.h]) # 点击第一个人
        sleep(2)
        """
        首先判断挑战次数
        """
        reach_maximum_limit = False
        try:
            wait(Template(self.shot_path + self.__page_dict["challenge_count_maximum_limit"], record_pos=(-0.005, -0.07), resolution=(1280, 720), threshold=0.9), timeout=2)  # 今天的挑战次数已经达到上限
            reach_maximum_limit = True
        except:
            pass
        else:
            self.logger.info("今天的挑战次数已经达到上限，返回")
            CommonButton.cancel()
        """
        然后判断是否冷却中
        """
        if not reach_maximum_limit:
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
                self.logger.info("开始战斗")
                CommonButton.start_battle()
                wait(Template(self.shot_path + page_info.common_button_dict["next"], threshold=0.9, record_pos=(0.351, 0.23), resolution=(1280, 720)), timeout=100) # 下一步
                touch(Template(self.shot_path + page_info.common_button_dict["next"], threshold=0.9, record_pos=(0.351, 0.23), resolution=(1280, 720))) # 下一步
                self.logger.info("战斗结束")
                # TODO:增加进攻成功后，排名晋升提示框的取消逻辑(CommonButton.white_comfirm())
            else:
                self.logger.info("公主竞技场正在冷却中，返回")
                CommonButton.cancel()

    @pytest.fixture
    def arana_page(self):
        """竞技场"""
        self.logger.info("开始进入竞技场页面")
        try:
            wait(Template(self.shot_path + self.__page_dict["arana_battle_history"], record_pos=(-0.384, 0.164), resolution=(1280, 720), threshold=0.9), timeout=2) # 对战覆历
            wait(Template(self.shot_path + self.__page_dict["arana_defend_setting"], record_pos=(-0.231, 0.165), resolution=(1280, 720), threshold=0.9), timeout=2) # 防守设定
            wait(Template(self.shot_path + self.__page_dict["arana_tag"], threshold=0.9, record_pos=(-0.362, -0.252), resolution=(1280, 720)), timeout=2) # 竞技场标签
            self.logger.info("检测到已经在公主竞技场页面，无需进入")
        except:
            Page.arana_page()
            self.logger.info("进入竞技场完毕")

    @pytest.fixture
    def princess_arana_page(self):
        """公主竞技场"""
        self.logger.info("开始进入公主竞技场页面")
        try:
            wait(Template(self.shot_path + self.__page_dict["pricess_arana_battle_history"], record_pos=(-0.385, 0.175), resolution=(1280, 720), threshold=0.9), timeout=2)  # 对战覆历
            wait(Template(self.shot_path + self.__page_dict["pricess_defend_setting"], record_pos=(-0.231, 0.175), resolution=(1280, 720), threshold=0.9), timeout=2)  # 防守设定
            wait(Template(self.shot_path + self.__page_dict["pricess_arana_tag"], threshold=0.9, record_pos=(-0.361, -0.252), resolution=(1280, 720)), timeout=2) # 公主竞技场标签
            self.logger.info("检测到已经在公主竞技场页面，无需进入")
        except:
            Page.princess_arana_page()
            self.logger.info("进入公主竞技场完毕")

