from Common.ClientBasic import *


class TestInvest(ClientBasic):
    """调查"""
    __page_dict = page_info.invest_dict

    def test_miracle_survey_level_one(self, miracle_page):
        """圣迹调查关卡1级,开始:圣迹调查,结束:圣迹调查"""
        touch(Template(self.shot_path + self.__page_dict["miracle_survey_level_one"], record_pos=(0.252, 0.071),
                       resolution=(1280, 720), threshold=0.9))  # 圣迹调查关卡1级
        self.__start_invest()

    def test_miracle_survey_level_two(self, miracle_page):
        """圣迹调查关卡2级,开始:圣迹调查,结束:圣迹调查"""
        touch(Template(self.shot_path + self.__page_dict["miracle_survey_level_two"], record_pos=(0.255, -0.043),
                       resolution=(1280, 720), threshold=0.9))  # 圣迹调查关卡2级
        self.__start_invest()

    def test_miracle_survey_level_three(self, miracle_page):
        """圣迹调查关卡3级,开始:圣迹调查,结束:圣迹调查"""
        touch(Template(self.shot_path + self.__page_dict["miracle_survey_level_three"], record_pos=(0.254, -0.159),
                       resolution=(1280, 720), threshold=0.9))  # 圣迹调查关卡3级
        self.__start_invest()

    def test_temple_survey_level_one(self, temple_page):
        """神殿调查关卡1级,开始:神殿调查,结束:神殿调查"""
        touch(Template(self.shot_path + self.__page_dict["temple_survey_level_one"], record_pos=(0.26, -0.042),
                       resolution=(1280, 720), threshold=0.9))  # 神殿调查关卡1级
        self.__start_invest()

    def test_temple_survey_level_two(self, temple_page):
        """神殿调查关卡2级,开始:神殿调查,结束:神殿调查"""
        touch(Template(self.shot_path + self.__page_dict["temple_survey_level_two"], record_pos=(0.262, -0.156),
                       resolution=(1280, 720), threshold=0.9))  # 神殿调查关卡2级
        self.__start_invest()

    @pytest.fixture
    def miracle_page(self):
        """圣迹调查页面"""
        # 首先检测是否在里面了
        is_in_page = True
        try:
            touch(Template(r"tpl1681996607788.png", record_pos=(0.075, -0.13), resolution=(1280, 720))) # 心碎图片
        except:
            is_in_page = False
        # 不在那就直接进去
        if not is_in_page:
            # 做一个稳定性检测，在调查页面里面就直接进去
            try:
                wait(Template(self.shot_path + self.__page_dict["temple"], record_pos=(0.341, 0.064),
                              resolution=(1280, 720), threshold=0.9), timeout=2)  # 神殿调查
                wait(Template(self.shot_path + self.__page_dict["miracle"], record_pos=(0.11, 0.065),
                              resolution=(1280, 720), threshold=0.9), timeout=2)  # 圣迹调查
            except:
                Page.invest_page()  # 否则进入调查页面，再进去
            touch(Template(self.shot_path + self.__page_dict["miracle"], record_pos=(0.11, 0.065),
                           resolution=(1280, 720), threshold=0.9))  # 圣迹调查

    @pytest.fixture
    def temple_page(self):
        """神殿调查页面"""
        # 首先检测是否在里面了
        is_in_page = True
        try:
            # TODO:更换其他的检测方式，检测页面上的星球杯图片而不是文字
            touch(Template(r"tpl1681996645377.png", record_pos=(0.08, -0.127), resolution=(1280, 720))) # 心碎图片
        except:
            is_in_page = False
        # 不在那就直接进去
        if not is_in_page:
            # 做一个稳定性检测，在调查页面里面就直接进去
            try:
                wait(Template(self.shot_path + self.__page_dict["miracle"], record_pos=(0.11, 0.065),
                              resolution=(1280, 720), threshold=0.9), timeout=2)  # 圣迹调查
                wait(Template(self.shot_path + self.__page_dict["temple"], record_pos=(0.341, 0.064),
                              resolution=(1280, 720), threshold=0.9), timeout=2)  # 神殿调查
            except:
                Page.invest_page()  # 否则进入调查页面，再进去
            touch(Template(self.shot_path + self.__page_dict["temple"], record_pos=(0.341, 0.064),
                           resolution=(1280, 720), threshold=0.9))  # 神殿调查

    def __start_invest(self):
        """使用扫荡券扫荡"""
        for i in range(4):
            touch(Template(self.shot_path + self.__page_dict["plus"], record_pos=(0.415, 0.062),
                           resolution=(1280, 720)))  # +号
            sleep(1)
        touch(Template(self.shot_path + self.__page_dict["use_five_tickets"], record_pos=(0.285, 0.062),
                       resolution=(1280, 720)))  # 使用5张
        sleep(1)
        # 检查是否剩余次数
        has_remain = True
        try:
            wait(Template(self.shot_path + self.__page_dict["remain_challenge_zero"], record_pos=(-0.004, -0.016),
                          resolution=(1280, 720)),timeout=2)  # 剩余挑战次数为0
            has_remain = False
        except:
            pass
        """
        有次数则正常扫荡
        """
        if has_remain:
            # 开始扫荡
            CommonButton.blue_comfirm()
            try:
                touch(Template(self.shot_path + self.__page_dict["skip_and_finish"], record_pos=(0.001, 0.216),
                               resolution=(1280, 720)))  # 跳过完毕
            except:
                pass
            # 正常扫荡
            CommonButton.white_comfirm()
            sleep(1)
            Page.detect_limit_shop_open()
        else:
            """
            没有次数则跳过
            """
            CommonButton.cancel()
            sleep(1)
        CommonButton.cancel()
        sleep(1)
