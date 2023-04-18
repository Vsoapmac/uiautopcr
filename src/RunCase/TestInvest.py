from Common.ClientBasic import *


class TestInvest(ClientBasic):
    """调查"""

    def test_miracle_survey_level_one(self, miracle_page):
        """圣迹调查关卡1级,开始:圣迹调查,结束:圣迹调查"""
        touch(Template(r"tpl1681834142996.png", record_pos=(0.252, 0.071), resolution=(1280, 720))) # 圣迹调查关卡1级
        touch(Template(r"tpl1681834304680.png", record_pos=(0.415, 0.062), resolution=(1280, 720))) # +号
        touch(Template(r"tpl1681834320663.png", record_pos=(0.285, 0.062), resolution=(1280, 720))) # 使用5张
        pass

    def test_miracle_survey_level_two(self, miracle_page):
        """圣迹调查关卡2级,开始:圣迹调查,结束:圣迹调查"""
        touch(Template(r"tpl1681834159258.png", record_pos=(0.255, -0.043), resolution=(1280, 720))) # 圣迹调查关卡2级
        pass

    def test_miracle_survey_level_three(self, miracle_page):
        """圣迹调查关卡3级,开始:圣迹调查,结束:圣迹调查"""
        touch(Template(r"tpl1681834176436.png", record_pos=(0.254, -0.159), resolution=(1280, 720))) # 圣迹调查关卡3级
        pass

    def test_temple_survey_level_one(self, temple_page):
        """神殿调查关卡1级,开始:神殿调查,结束:神殿调查"""
        touch(Template(r"tpl1681834229352.png", record_pos=(0.26, -0.042), resolution=(1280, 720))) # 神殿调查关卡1级
        pass

    def test_temple_survey_level_two(self, temple_page):
        """神殿调查关卡2级,开始:神殿调查,结束:神殿调查"""
        touch(Template(r"tpl1681834242203.png", record_pos=(0.262, -0.156), resolution=(1280, 720))) # 神殿调查关卡2级
        pass

    @pytest.fixture
    def miracle_page(self):
        touch(Template(r"tpl1681834097719.png", record_pos=(0.11, 0.065), resolution=(1280, 720))) # 圣迹调查
        pass

    @pytest.fixture
    def temple_page(self):
        touch(Template(r"tpl1681834117205.png", record_pos=(0.341, 0.064), resolution=(1280, 720))) # 神殿调查
        pass
