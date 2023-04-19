from Common.ClientBasic import *


class TestInvest(ClientBasic):
    """调查"""
    __page_dict = page_info.invest_dict

    def test_miracle_survey_level_one(self, miracle_page):
        """圣迹调查关卡1级,开始:圣迹调查,结束:圣迹调查"""
        touch(Template(self.shot_path + self.__page_dict["miracle_survey_level_one"], record_pos=(0.252, 0.071), resolution=(1280, 720))) # 圣迹调查关卡1级
        self.__start_invest()

    def test_miracle_survey_level_two(self):
        """圣迹调查关卡2级,开始:圣迹调查,结束:圣迹调查"""
        touch(Template(self.shot_path + self.__page_dict["miracle_survey_level_two"], record_pos=(0.255, -0.043), resolution=(1280, 720))) # 圣迹调查关卡2级
        self.__start_invest()

    def test_miracle_survey_level_three(self):
        """圣迹调查关卡3级,开始:圣迹调查,结束:圣迹调查"""
        touch(Template(self.shot_path + self.__page_dict["miracle_survey_level_three"], record_pos=(0.254, -0.159), resolution=(1280, 720))) # 圣迹调查关卡3级
        self.__start_invest()

    def test_temple_survey_level_one(self, temple_page):
        """神殿调查关卡1级,开始:神殿调查,结束:神殿调查"""
        touch(Template(self.shot_path + self.__page_dict["temple_survey_level_one"], record_pos=(0.26, -0.042), resolution=(1280, 720))) # 神殿调查关卡1级
        self.__start_invest()

    def test_temple_survey_level_two(self):
        """神殿调查关卡2级,开始:神殿调查,结束:神殿调查"""
        touch(Template(self.shot_path + self.__page_dict["temple_survey_level_two"], record_pos=(0.262, -0.156), resolution=(1280, 720))) # 神殿调查关卡2级
        self.__start_invest()

    @pytest.fixture
    def miracle_page(self):
        try:
            wait(Template(self.shot_path + self.__page_dict["temple"], record_pos=(0.341, 0.064), resolution=(1280, 720)), timeout=2) # 神殿调查
            wait(Template(self.shot_path + self.__page_dict["miracle"], record_pos=(0.11, 0.065), resolution=(1280, 720)), timeout=2) # 圣迹调查
        except:
            Page.invest_page()
        touch(Template(self.shot_path + self.__page_dict["miracle"], record_pos=(0.11, 0.065), resolution=(1280, 720))) # 圣迹调查

    @pytest.fixture
    def temple_page(self):
        try:
            wait(Template(self.shot_path + self.__page_dict["miracle"], record_pos=(0.11, 0.065), resolution=(1280, 720)), timeout=2) # 圣迹调查
            wait(Template(self.shot_path + self.__page_dict["temple"], record_pos=(0.341, 0.064), resolution=(1280, 720)), timeout=2) # 神殿调查
        except:
            Page.invest_page()
        touch(Template(self.shot_path + self.__page_dict["temple"], record_pos=(0.341, 0.064), resolution=(1280, 720))) # 神殿调查

    def __start_invest(self):
        """使用扫荡券扫荡"""
        for i in range(5):
            touch(Template(self.shot_path + self.__page_dict["plus"], record_pos=(0.415, 0.062), resolution=(1280, 720))) # +号
            sleep(1)
        touch(Template(self.shot_path + self.__page_dict["use_five_tickets"], record_pos=(0.285, 0.062), resolution=(1280, 720))) # 使用5张
        sleep(2)